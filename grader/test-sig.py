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

oauth_signature="mYQzgz5ldR1bBYeMGs6sZGik7Cc%3D"

auth='''OAuth realm="https://campusvirtual.uclm.es",
 oauth_body_hash="BE%2FkLd6GIiyKwnL%2FPFDG9GEyFzA%3D",
 oauth_nonce="61357020",
 oauth_timestamp="1444249394",
 oauth_consumer_key="clave",
 oauth_signature_method="HMAC-SHA1",
 oauth_version="1.0"'''

p = sorteddict()
for i in auth.split(',\n ')[1:]:
    k,v = i.split('=')
    p[k] = v[1:-1]

params='&'.join(['='.join((k,p[k])) for k in p])
base = '&'.join(map(urllib.quote_plus,
                    ['POST',
                     'https://campusvirtual.uclm.es/mod/lti/service.php',
                     params]))
key='shared&'

print 'SIG :', urllib.unquote(oauth_signature)
print 'CALC:', base64.b64encode(hmac.new(key,base,hashlib.sha1).digest())

'''Caso de ejemplo de la RFC5849. Para comprobar el método de cálculo
de la firma voy a aplicarlo al ejemplo de referencia.'''

base='GET&http%3A%2F%2Fphotos.example.net%2Fphotos&file%3Dvacation.jpg%26oauth_consumer_key%3Ddpf43f3p2l4k3l03%26oauth_nonce%3Dkllo9940pd9333jh%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1191242096%26oauth_token%3Dnnch734d00sl2jdk%26oauth_version%3D1.0%26size%3Doriginal'
key='kd94hf93k423kf44&pfkkdhi9sl3r4s00'

print 'Ref SIG:', base64.b64encode(hmac.new(key,base,hashlib.sha1).digest())
