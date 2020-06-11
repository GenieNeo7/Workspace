#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import datetime
import json
import logging
import re
import random
import requests
import shutil
from pyquery import PyQuery as pq


def main(username, password):

    logging.basicConfig(filename='imgur2fb.log', level=logging.DEBUG)

    session = requests.session()

    uid, dtsg = login(session, username, password)


def login(session, username, password):

    '''
    Login to Facebook
    '''

    # Navigate to the Facebook homepage
    response = session.get('https://facebook.com')

    # Construct the DOM
    dom = pq(response.text)

    # Get the lsd value from the HTML. This is required to make the login request
    lsd = dom('[name="lsd"]').val()

    # Perform the login request
    response = session.post('https://www.facebook.com/login.php?login_attempt=1', data={
        'lsd': lsd,
        'email': username,
        'pass': password,
        'default_persistent': '0',
        'timezone': '-60',
        'lgndim': '',
        'lgnrnd': '',
        'lgnjs': '',
        'locale':'en_GB',
        'qsstamp': ''
    })

    '''
    Get the users ID and fb_dtsg token. The fb_dtsg token is required when making requests as a logged in user. It
    never changes, so we only need to grab this token once.

    If the login was successful a cookie 'c_user' is set by Facebook. If the login failed, the 'c_user' cookie
    will not be present. This will raise an exception.
    '''
    try:
        uid = session.cookies['c_user']
        dtsg = re.search(r'(type="hidden" name="fb_dtsg" value="([0-9a-zA-Z-_:]+)")', response.text).group(1)

        dtsg = dtsg[dtsg.find("value")+6:]
        dtsg = dtsg[1:-1]

    except KeyError:
        raise Exception('Login Failed!')

    return uid, dtsg

try:
    main(username='nacel777@nate.com', password='*016727a7')
except Exception as e:
    logging.exception(e)
finally:
    pass