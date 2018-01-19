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

def get()
    course_list = get_course()
    for i in get_course():
        se.open(i)
        
    
    

def get_course():
    html = se.content
    soup = BeautifulSoup(html, "html.parser")
    sources = soup.select('#pda-portlet-site-menu > li > span > a')
    li = []
    for i in sources:
        li.append(i.get('href'))
    li.remove(li[0])
    return(li)

get_assignment(url):
    se.open(url)



login('ztang15', 'Tz999000')
