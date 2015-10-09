#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-
'''Este programita pretende comprobar manualmente que las firmas OAuth
son correctas.

Las firmas y los datos de cabecera están sacadas de capturas reales de
grader.py.  Consultar grader.out para más detalles.

La excepción recibida es "Message signature not valid" que se eleva
solo si lti_verify_message devuelve false.  Desgraciadamente esta
función enmascara la causa real de la excepción, así que puede ser por
cualquiera de los motivos por los que pueda elevar excepción la
función handle_oauth_body_post.

Las posibles causas son:

- Que el mensaje tenga Content-type application/x-www-form-urlencoded.
  Como puede verse el Content-type es application/xml así que esta
  causa está en principio descartada.

- Que no encuentre la cabecera oauth_body_hash en Authorization.  Esto
  es poco probable, porque está y porque si no encontrara esa cabecera
  tampoco encontraría la cabecera oauth_consumer_key, y por tanto
  habría elevado antes la excepción "Consumer key is missing".

- Que falle la verificación de la firma HMAC-SHA1 del mensaje.

- Que falle el hash del cuerpo.

El hash del cuerpo es directamente base64(sha1(body)).
'''


import hashlib, base64, urllib, hmac
from blist import sorteddict

def test_my_signature():
    '''Tests OAuth signature made by oauth2 library from log data'''

    params, sig = params_from_authorization('''OAuth realm="https://campusvirtual.uclm.es", oauth_body_hash="n91hSUBANr8df6cTLpTR93mQXkY%3D", oauth_nonce="49873659", oauth_timestamp="1444291721", oauth_consumer_key="clave", oauth_signature_method="HMAC-SHA1", oauth_version="1.0", oauth_signature="pgFqkRraieAI19nhpPxKvCpPq74%3D"''')
    calc = signature('POST',
                     'https://campusvirtual.uclm.es/mod/lti/service.php',
                     params,
                     'shared&')

    print 'SENT signature:      ', sig
    print 'Calculated signature:', calc


def test_reference_signature():
    '''Caso de ejemplo de la RFC5849. Para comprobar el método de cálculo
de la firma voy a aplicarlo al ejemplo de referencia.'''

    base='GET&http%3A%2F%2Fphotos.example.net%2Fphotos&file%3Dvacation.jpg%26oauth_consumer_key%3Ddpf43f3p2l4k3l03%26oauth_nonce%3Dkllo9940pd9333jh%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1191242096%26oauth_token%3Dnnch734d00sl2jdk%26oauth_version%3D1.0%26size%3Doriginal'
    key='kd94hf93k423kf44&pfkkdhi9sl3r4s00'
    sig='tR3+Ty81lMeYAr/Fid0kMTYa/WM='
    calc = base64.b64encode(hmac.new(key,base,hashlib.sha1).digest())

    print 'SENT signature:      ', sig
    print 'Calculated signature:', calc


def test_moodle_launch():
    '''Caso del launch del propio Moodle'''

    params, sig = params_from_postdata('''oauth_version=1.0&oauth_nonce=44e4c87b32e9bf82679dc7383d29d01d&oauth_timestamp=1444319156&oauth_consumer_key=clave%2Fe%C3%B1e&resource_link_id=47&resource_link_title=Prueba+de+launch&resource_link_description=solo+prueba&user_id=34094&roles=Instructor&context_id=12080&context_label=%2812080%29+INFORM%C3%81TICA&context_title=INFORM%C3%81TICA&launch_presentation_locale=es&lis_result_sourcedid=%7B%22data%22%3A%7B%22instanceid%22%3A%2247%22%2C%22userid%22%3A%2234094%22%2C%22launchid%22%3A988482759%7D%2C%22hash%22%3A%22c4d108af94b41b54dc2d2166e573d0496937d11c8445319b4b8ce87003858b36%22%7D&lis_outcome_service_url=https%3A%2F%2Fcampusvirtual.uclm.es%2Fmod%2Flti%2Fservice.php&lis_person_name_given=FRANCISCO&lis_person_name_family=MOYA+FERNANDEZ&lis_person_name_full=FRANCISCO+MOYA+FERNANDEZ&lis_person_contact_email_primary=francisco.moya%40uclm.es&ext_lms=moodle-2&tool_consumer_info_product_family_code=moodle&tool_consumer_info_version=2014051205.01&oauth_callback=about%3Ablank&lti_version=LTI-1p0&lti_message_type=basic-lti-launch-request&tool_consumer_instance_guid=campusvirtual.uclm.es&launch_presentation_return_url=https%3A%2F%2Fcampusvirtual.uclm.es%2Fmod%2Flti%2Freturn.php%3Fcourse%3D12080%26launch_container%3D4%26instanceid%3D47%26sesskey%3DVZoDQsx6RK&oauth_signature_method=HMAC-SHA1&oauth_signature=Gxj4zdtADrly36D1OiOJN5x5Wp4%3D&ext_submit=Press+to+launch+this+activity''')
    calc = signature('POST',
                     'http://161.67.172.69:8088/prueba/lms',
                     params,
                     'shared&')

    print 'SENT signature:      ', sig
    print 'Calculated signature:', calc


def signature(method, url, params, key):
    base = base_string(method, url, params)
    return base64.b64encode(hmac.new(key,base,hashlib.sha1).digest())

def base_string(method, url, params):
    params='&'.join(['='.join((k,params[k])) for k in params])
    return '&'.join(map(percent_encode, [method, url, params]))

def params_from_authorization(auth):
    p = sorteddict()
    for i in auth.split(',')[1:]:
        k,v = i.strip().split('=')
        if k == 'oauth_signature':
            oauth_signature = urllib.unquote(v[1:-1])
            continue
        p[percent_encode(k)] = percent_encode(urllib.unquote(v[1:-1]))
    return p, oauth_signature


def params_from_postdata(data):
    p = sorteddict()
    for i in data.split('&'):
        k,v = i.strip().split('=')
        if k == 'oauth_signature':
            oauth_signature = urllib.unquote(v)
            continue
        p[percent_encode(k)] = percent_encode(urllib.unquote_plus(v))
    return p, oauth_signature

def percent_encode(str):
    return urllib.quote(str,safe='')


test_my_signature()
test_reference_signature()
test_moodle_launch()
