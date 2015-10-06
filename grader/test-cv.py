#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

# Hay que reproducir una autenticación válida
#
# De captura de red con WebDeveloper Tools de Chrome
#
#

import httplib2, urllib, sys
from BeautifulSoup import BeautifulSoup


def r(h, url, method, headers=None, body=None):
    print method, url
    print headers
    if body:
        print body
    print
    resp, content = h.request(url, method, headers=headers, body=body)
    print resp
    print
    return resp, content



h = httplib2.Http(".cache")
h.follow_redirects = False

headers={}
headers['Accept'] = 'text/html, text/*;q=0.5'
headers['Host'] = 'campusvirtual.uclm.es'

resp, content = r(h, 'https://campusvirtual.uclm.es/', 'GET', headers=headers)

if resp['status'] != '303':
    raise 'Se esperaba redirección 303'

headers={}
headers['Accept'] = 'text/html, text/*;q=0.5'
headers['Host'] = 'campusvirtual.uclm.es'
headers['Cookie'] = resp['set-cookie']
headers['Cookie2'] = '$Version="1"'

resp, content = r(h, resp['location'], "GET", headers=headers)

if resp['status'] != '303':
    raise 'Se esperaba redirección 303'

headers['Cookie'] += resp['set-cookie']


resp, content = r(h, resp['location'], "GET", headers=headers)

# Pulsamos botón de ACCESO
resp, content = r(h, "https://campusvirtual.uclm.es/auth/saml/index.php", "GET", headers=headers)

headers['Cookie'] += resp['set-cookie']
cvh = headers

headers={}
headers['Cookie'] = resp['set-cookie']

if resp['status'] != '302':
    raise 'Se esperaba redirección 302'

# SSOService

headers={}
headers['Accept'] = 'text/html, text/*;q=0.5'
headers['Host'] = 'adas.uclm.es'

resp, content = r(h, resp['location'], "GET", headers=headers)

if resp['status'] != '302':
    raise 'Se esperaba redirección 302'

headers={}
headers['Accept'] = 'text/html, text/*;q=0.5'
headers['Host'] = 'adas.uclm.es'

# adas.uclm.es
adasurl = resp['location']
resp, content = r(h, adasurl, "GET", headers=headers)

p = BeautifulSoup(content)
action = p.body.find('form').get('action')
params = {
    'adAS_i18n_theme': 'es',
    'adAS_mode': 'authn',
    'adAS_username': 'francisco.moya@uclm.es',
    'adAS_password': 'Fsasya,46a8088,9',
    'adAS_submit': 'Aceptar'
}

headers = {}
headers['Cookie'] = resp['set-cookie']
headers['Content-type'] = 'application/x-www-form-urlencoded'
headers['Referer'] = adasurl

body = urllib.urlencode(params)

resp, content = r(h, action, "POST", headers=headers, body=body)

headers = {}
headers['Content-type'] = 'application/x-www-form-urlencoded'
headers['Cookie'] = cvh['Cookie']
headers['Cookie2'] = cvh['Cookie2']
headers['Referer'] = action

p = BeautifulSoup(content)
f = p.find(id='formulario1')
action = f.get('action')
params = {}
for i in f('input'):
    params[i.get('name')] = i.get('value')
body = urllib.urlencode(params)

resp, content = r(h, action, "POST", headers=headers, body=body)

headers.pop('Content-type', None)

if resp['status'] != '303':
    raise 'Se esperaba redirección 303'

headers['Cookie'] = resp['set-cookie']

resp, content = r(h, resp['location'], "GET", headers=headers)

if resp['status'] != '302':
    raise 'Se esperaba redirección 302'

headers['Cookie'] += resp['set-cookie']

resp, content = r(h, resp['location'], "GET", headers=headers)

if resp['status'] != '302':
    raise 'Se esperaba redirección 302'

resp, content = r(h, resp['location'], "GET", headers=headers)


print content
