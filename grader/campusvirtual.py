#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import httplib2, urllib
from BeautifulSoup import BeautifulSoup

def autenticar_campusvirtual(user, password):
    '''
    user	Usuario de UCLM (eg. 'francisco.moya@uclm.es')
    password	Contraseña de UCLM

    Devuelve las cabeceras a usar en futuras peticiones.
    '''

    h = httplib2.Http(".cache")
    h.follow_redirects = False

    resp, content = rq(h, 'https://campusvirtual.uclm.es/', 'GET')

    if resp['status'] != '303':
        raise 'Se esperaba redirección 303'

    headers={}
    append_cookie(headers, resp)
    resp, content = rq(h, resp['location'], "GET", headers=headers)

    if resp['status'] != '303':
        raise 'Se esperaba redirección 303'

    append_cookie(headers, resp)
    resp, content = rq(h, resp['location'], "GET", headers=headers)

    # Pulsamos botón de ACCESO
    resp, content = rq(h, "https://campusvirtual.uclm.es/auth/saml/index.php", "GET", headers=headers)

    append_cookie(headers, resp)
    cvh = headers

    if resp['status'] != '302':
        raise 'Se esperaba redirección 302'

    # SSOService
    resp, content = rq(h, resp['location'], "GET")

    if resp['status'] != '302':
        raise 'Se esperaba redirección 302'

    # adas.uclm.es
    resp, content = rq(h, resp['location'], "GET")

    p = BeautifulSoup(content)
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
    body = urllib.urlencode(params)
    resp, content = rq(h, action, "POST", headers=headers, body=body)



    headers = {}
    headers['Content-type'] = 'application/x-www-form-urlencoded'
    headers['Cookie'] = cvh['Cookie']

    p = BeautifulSoup(content)
    f = p.find(id='formulario1')
    action = f.get('action')
    params = {}
    for i in f('input'):
        params[i.get('name')] = i.get('value')
    body = urllib.urlencode(params)

    resp, content = rq(h, action, "POST", headers=headers, body=body)

    headers.pop('Content-type', None)

    if resp['status'] != '303':
        raise 'Se esperaba redirección 303'

    append_cookie(headers, resp)

    resp, content = rq(h, resp['location'], "GET", headers=headers)

    if resp['status'] != '303':
        raise 'Se esperaba redirección 303'

    append_cookie(headers, resp)

    resp, content = rq(h, resp['location'], "GET", headers=headers)

    if resp['status'] != '303':
        raise 'Se esperaba redirección 303'

    resp, content = rq(h, resp['location'], "GET", headers=headers)

    return headers


def rq(h, url, method, headers=None, body=None):
    #print method, url
    #print headers
    #if body:
    #    print body
    #print
    resp, content = h.request(url, method, headers=headers, body=body)
    #print resp
    #print
    return resp, content


def normalize_cookie(cookie):
    ret = {}
    cookie = cookie.replace('path=/, ', '').replace('path=/', '')
    cookie = cookie.replace('HttpOnly; ','').replace('HttpOnly, ','')
    cookie = cookie.replace('secure, ', '').replace('; secure', '')
    for c in cookie.split(';'):
        c = c.strip()
        if len(c) < 2 or 0 > c.find('='):
            continue
        k, v = c.split('=')
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
    if not 'Cookie' in headers:
        headers['Cookie'] = get_cookie(resp)
    else:
        headers['Cookie'] += '; ' + get_cookie(resp)
    headers['Cookie'] = normalize_cookie(headers['Cookie'])
