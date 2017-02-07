#coding:utf-8
import requests
from django.template import Context, Template
from django.shortcuts import render
class getcap:
    def get_captcha(request):
        CAPTCHA_URL = "http://jw.qdu.edu.cn/academic/getCaptcha.do"
        session = requests.session()
        image = session.get(CAPTCHA_URL)
        request.session['JSESSIONID'] = session.cookies['JSESSIONID']
        print type(image.content)
        return image.content

    def register(request,self):
        if request.method == "GET":
            captcha =self.get_captcha(request)
            return render(request, 'student/register.html', {'captcha': captcha})