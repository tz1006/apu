#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: class_notification.py

from ghost import Ghost, Session
from bs4 import BeautifulSoup
import sms

gh = Ghost()
se = Session(gh, wait_timeout=30, display=True, viewport_size=(375, 553), download_images=True)

def login(username, password):
    url = 'https://mobile.apu.edu/app/profile/login'
    se.open(url)
    se.set_field_value('input.input-box', username)
    se.set_field_value('#password', password)
    se.click('#login-btn', expect_loading=True)
    se.sleep(3)


def get_schedule():
    html = se.content
    soup = BeautifulSoup(html, "html.parser")
    source = soup.select('div.active > a')
    schedule = []
    for i in source:
        class_name = i.select('div.section-body')[0].text
        class_code = i.select('div.section-body')[1].text
        class_time = i.select('div.section-body')[1].text
        class_loacation = i.select('div.section-body')[1].text
        schedule.append((class_name, class_code, class_time, class_location))



login('ztang15', 'Tz999000')
