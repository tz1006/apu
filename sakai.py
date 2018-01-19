#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: sakai.py

from ghost import Ghost, Session
from bs4 import BeautifulSoup

gh = Ghost()
se = Session(gh, wait_timeout=30, display=True, viewport_size=(375, 553), download_images=True)

def login(username, password):
    index()
    se.set_field_value('#username', username)
    se.set_field_value('#password', password)
    se.click('input.btn-submit', expect_loading=True)

def index():
    url = 'https://sakai.apu.edu/portal/pda/?force.login=yes'
    se.open(url)


def get():
    global assignment_list
    assignment_list = []
    index()
    course_list = get_course()
    for i in get_course():
        print(i)
        for l in get_assignment(i):
            assignment_list.append(l)
    print('一共%d个作业' % len(assignment_list))
    index()


def get_course():
    html = se.content
    soup = BeautifulSoup(html, "html.parser")
    source = soup.select('#pda-portlet-site-menu > li > span > a')
    li = []
    for i in source:
        li.append(i.get('href'))
    li.remove(li[0])
    return(li)

def get_assignment(url):
    #print(url)
    se.open(url)
    se.click('li.icon-sakai-assignment-grades-item > span > a', expect_loading=True)
    html = se.content
    soup = BeautifulSoup(html, "html.parser")
    course_code = soup.select('li.currentSiteLink > span > a')[0].text.split('-')[0]
    source = soup.select('tbody > tr')
    if source != []:
        source.remove(source[0])
    li = []
    for i in source:
        title = i.find_all(headers='title')[0].text.strip()
        title = '%s - %s' % (course_code, title)
        opendate = i.find_all(headers='openDate')[0].text.strip()
        duedate = i.find_all(headers='dueDate')[0].text.strip()
        l = [title, opendate, duedate]
        li.append(l)
    return(li)
    
    

login('ztang15', 'Tz999000')
get()
