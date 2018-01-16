#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: sakai.py

from ghost import Ghost, Session
from bs4 import BeautifulSoup

gh = Ghost()
se = Session(gh, wait_timeout=30, display=True, viewport_size=(375, 553), download_images=True)

def login(username, password):
    url = 'https://sakai.apu.edu/portal/pda/?force.login=yes'
    se.open(url)
    se.set_field_value('#username', username)
    se.set_field_value('#password', password)
    se.click('input.btn-submit', expect_loading=True)

def 



login('ztang15', 'Tz999000')
