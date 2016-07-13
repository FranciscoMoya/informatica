# -*- coding: utf-8; mode: python -*-

from xml.etree import ElementTree as etree
from bs4 import BeautifulSoup
from blist import sorteddict
import oauth2client.file, oauth2client.client, oauth2client.tools, oauth2
import httplib2, hashlib, base64, urllib, hmac

cv_auth_headers = None

def download_marks(course_id):
    global cv_auth_headers
    if not cv_auth_headers:
        raise SystemError('You must call cv_authenticate first')
    
    url = 'https://campusvirtual.uclm.es/grade/export/txt/index.php?id={}'.format(course_id)

    h = httplib2.Http(".cache")
    resp, content = rq(h, url, 'GET', headers = cv_auth_headers)

    p = BeautifulSoup(content, 'lxml')
    action = p.body.find('form').get('action')
    print('action:', action)

    print(content)
    return

    # FIXME: rellenar POST request
    # Descargar attachment
    params = {
        'adAS_i18n_theme': 'es',
        'adAS_mode': 'authn',
        'adAS_username': user,
        'adAS_password': password,
        'adAS_submit': 'Aceptar'
    }

    headers = cv_auth_headers.copy()
    headers['Content-type'] = 'application/x-www-form-urlencoded'
    body = urllib.parse.urlencode(params)
    resp, content = rq(h, action, "POST", headers=headers, body=body)

    # FIXME
    # Extraer key/value pairs y URL de submit
    # Hacer POST con datos


def authenticate(user, password):
    '''
    user	Usuario de UCLM (eg. 'francisco.moya@uclm.es')
    password	Contraseña de UCLM
    '''
    global cv_auth_headers
    
    if cv_auth_headers:
        return cv_auth_headers
    
    h = httplib2.Http(".cache")
    h.follow_redirects = False

    resp, content = rq(h, 'https://campusvirtual.uclm.es/', 'GET')

    if resp['status'] != '303':
        raise IOError('Se esperaba redirección 303')

    headers={}
    append_cookie(headers, resp)
    resp, content = rq(h, resp['location'], "GET", headers=headers)

    if resp['status'] != '303':
        raise IOError('Se esperaba redirección 303')

    append_cookie(headers, resp)
    resp, content = rq(h, resp['location'], "GET", headers=headers)

    # Pulsamos botón de ACCESO
    resp, content = rq(h, "https://campusvirtual.uclm.es/auth/saml/index.php", "GET", headers=headers)

    append_cookie(headers, resp)
    cvh = headers

    if resp['status'] != '302':
        raise IOError('Se esperaba redirección 302')

    # SSOService
    resp, content = rq(h, resp['location'], "GET")

    if resp['status'] != '302':
        raise IOError('Se esperaba redirección 302')

    # adas.uclm.es
    resp, content = rq(h, resp['location'], "GET")

    p = BeautifulSoup(content, 'lxml')
    action = p.body.find('form').get('action')
    params = {
        'adAS_i18n_theme': 'es',
        'adAS_mode': 'authn',
        'adAS_username': user,
        'adAS_password': password,
        'adAS_submit': 'Aceptar'
    }

    headers = {}
    headers['Content-type'] = 'application/x-www-form-urlencoded'
    body = urllib.parse.urlencode(params)
    resp, content = rq(h, action, "POST", headers=headers, body=body)

    headers = {}
    headers['Content-type'] = 'application/x-www-form-urlencoded'
    headers['Cookie'] = cvh['Cookie']

    p = BeautifulSoup(content, 'lxml')
    f = p.find(id='formulario1')
    action = f.get('action')
    params = {}
    for i in f('input'):
        params[i.get('name')] = i.get('value')
    body = urllib.parse.urlencode(params)

    resp, content = rq(h, action, "POST", headers=headers, body=body)

    headers.pop('Content-type', None)

    if resp['status'] != '303':
        raise IOError('Se esperaba redirección 303')

    append_cookie(headers, resp)

    resp, content = rq(h, resp['location'], "GET", headers=headers)

    if resp['status'] != '303':
        raise IOError('Se esperaba redirección 303')

    append_cookie(headers, resp)

    resp, content = rq(h, resp['location'], "GET", headers=headers)

    if resp['status'] != '303':
        raise IOError('Se esperaba redirección 303')

    resp, content = rq(h, resp['location'], "GET", headers=headers)

    if resp['status'] != '200':
        raise SystemError('Failed authentication')

    cv_auth_headers = headers
    return headers


def rq(h, url, method, headers=None, body=None):
    # print (method, url)
    # print (headers)
    # if body:
    #     print (body)
    # print()
    resp, content = h.request(url, method, headers=headers, body=body)
    # print (resp)
    # print()
    return resp, content


def normalize_cookie(cookie):
    ret = {}
    #cookie = cookie.replace('path=/, ', '').replace('path=/', '')
    cookie = cookie.replace('HttpOnly; ','').replace('HttpOnly, ','')
    cookie = cookie.replace('secure, ', '').replace('; secure', '')
    for c in cookie.split(';'):
        c = c.strip()
        if len(c) < 2 or 0 > c.find('='):
            continue
        k, v = c.split('=',1)
        if len(k) > 0 and len(v) > 0 and k != 'path' and k != 'domain':
            ret[k] = v
    cookie = ''
    for k in ret:
        cookie += k + '=' + ret[k] + '; '
    cookie = cookie.strip()
    if cookie.endswith(';'):
        cookie = cookie[:-1]
    return cookie


def get_cookie(resp):
    return normalize_cookie(resp['set-cookie'])


def append_cookie(headers, resp):
    if not 'set-cookie' in resp:
        print ('WARNING! No cookie in resp:')
        return
    if not 'Cookie' in headers:
        headers['Cookie'] = get_cookie(resp)
    else:
        headers['Cookie'] += '; ' + get_cookie(resp)
    headers['Cookie'] = normalize_cookie(headers['Cookie'])





class SignatureMethod_CampusVirtual(oauth2.SignatureMethod_HMAC_SHA1):
    '''
    In CampusVirtual HTTPS traffic is handled by the front load
    balancers.  Backend systems live into the internal intranet and
    use plain HTTP.  Therefore in order to generate a valid OAuth
    signature we must change the protocol in the normlized URL.
    '''
    def signing_base(self, request, consumer, token):
        if not hasattr(request, 'normalized_url') or request.normalized_url is None:
            raise ValueError("Base URL for request is not set.")

        sig = (
            oauth2.escape(request.method),
            oauth2.escape(request.normalized_url),
            #oauth2.escape(request.normalized_url.replace('https', 'http')),
            oauth2.escape(request.get_normalized_parameters()),
        )

        key = '%s&' % oauth2.escape(consumer.secret)
        if token:
            key += oauth2.escape(token.secret)
        raw = '&'.join(sig)
        return key.encode('utf8'), raw.encode('utf8')

message_id = 1234
http = httplib2.Http
normalize = http._normalize_headers

def my_normalize(self, headers):
    ret = normalize(self, headers)
    for i in ret:
        key = i[0].upper()+i[1:]
        ret[key] = ret.pop(i)
    return ret

http._normalize_headers = my_normalize

def submit_mark(url, lis_result_sourcedid, mark, key, secret):
    global cv_auth_headers
    if not cv_auth_headers:
        raise SystemError('You must call cv_authenticate first')
    
    global message_id
    xml = generate_request_xml(str(message_id),
                               'replaceResult',
                               lis_result_sourcedid,
                               mark)
    message_id +=1
    headers = cv_auth_headers.copy()
    headers['Content-Type'] = 'application/xml'
    consumer = oauth2.Consumer(key='clave', secret='shared')
    client = oauth2.Client(consumer)
    #client.set_signature_method(SignatureMethod_CampusVirtual())
    client.set_signature_method(oauth2.SignatureMethod_HMAC_SHA1())

    print(cv_auth_headers)
    print(url)
    print(xml)
    resp, content = client.request(url,
                                   'POST',
                                   body=xml,
                                   headers=cv_auth_headers)
    print (content)
    return resp['status'] == '200'


def generate_request_xml(message_identifier_id, operation,
                         lis_result_sourcedid, score):
    # pylint: disable=too-many-locals
    """
    Generates LTI 1.1 XML for posting result to LTI consumer.

    :param message_identifier_id:
    :param operation:
    :param lis_result_sourcedid:
    :param score:
    :return: XML string
    """
    root = etree.Element('imsx_POXEnvelopeRequest',
                         xmlns='http://www.imsglobal.org/services/ltiv1p1/xsd/imsoms_v1p0')
    header = etree.SubElement(root, 'imsx_POXHeader')
    header_info = etree.SubElement(header, 'imsx_POXRequestHeaderInfo')
    version = etree.SubElement(header_info, 'imsx_version')
    version.text = 'V1.0'
    message_identifier = etree.SubElement(header_info,
                                          'imsx_messageIdentifier')
    message_identifier.text = message_identifier_id
    body = etree.SubElement(root, 'imsx_POXBody')
    xml_request = etree.SubElement(body, '%s%s' % (operation, 'Request'))
    record = etree.SubElement(xml_request, 'resultRecord')

    guid = etree.SubElement(record, 'sourcedGUID')
    sourcedid = etree.SubElement(guid, 'sourcedId')
    sourcedid.text = lis_result_sourcedid
    if score is not None:
        result = etree.SubElement(record, 'result')
        result_score = etree.SubElement(result, 'resultScore')
        language = etree.SubElement(result_score, 'language')
        language.text = 'en'
        text_string = etree.SubElement(result_score, 'textString')
        text_string.text = score.__str__()
    ret = "<?xml version='1.0' encoding='utf-8'?>\n{}".format(
        etree.tostring(root).decode('utf8'))
    return ret
