# -*- coding: utf-8 -*-

import re
from gevent import monkey; monkey.patch_all()
from web import app as web
from app_sina import app as git_http
from vilya.wsgi import application as django_app


ROUTE_MAP = [(re.compile(r'/[^/]*\.git.*'), git_http),
             (re.compile(r'/[^/]*/([^/]*)\.git.*'), git_http),
             (re.compile(r'/admin'), django_app),
             (re.compile(r'/people'), django_app),
             (re.compile(r'/gist'), django_app),
             (re.compile(r'/register'), django_app),
             (re.compile(r'/login'), django_app),
             (re.compile(r'/logout'), django_app),
             (re.compile(r'/mirrors'), django_app),
             (re.compile(r'/badge'), django_app),
             (re.compile(r'/watch'), django_app),
             (re.compile(r'/watching'), django_app),
             (re.compile(r'/favorites'), django_app),
             (re.compile(r'/m'), django_app),
             (re.compile(r'/praise'), django_app),
             (re.compile(r'/trello'), django_app),
             (re.compile(r'/settings'), django_app),
             #(re.compile(r'/\w+/\w+/?$'), django_app),
             (re.compile(r'/\w+/\w+/watchers'), django_app),
             (re.compile(r'/\w+/\w+/forkers'), django_app),
             (re.compile(r'/\w+/\w+/archive'), django_app),
             (re.compile(r'/\w+/\w+/settings'), django_app),
             (re.compile(r'/\w+/\w+/blob'), django_app),
             (re.compile(r'/\w+/\w+/edit'), django_app),
             (re.compile(r'/\w+/\w+/tree'), django_app),
             (re.compile(r'/\w+/\w+/commits'), django_app),
             (re.compile(r'/\w+/\w+/blame'), django_app),
             (re.compile(r'/\w+/\w+/raw'), django_app),
             (re.compile(r'/\w+/\w+/browsefiles'), django_app),
             (re.compile(r'/\w+/\w+/code_review'), django_app),
             (re.compile(r'/\w+/\w+/comments'), django_app),
             (re.compile(r'/\w+/\w+/compare'), django_app),
             (re.compile(r'/\w+/\w+/issues'), django_app),
             (re.compile(r'/\w+/\w+/issue_comments'), django_app),
             (re.compile(r'/j/'), django_app),
             (re.compile(r'/hub/'), django_app),
             (re.compile(r'/teams/'), django_app),
             (re.compile(r'/vilya'), django_app),
             (re.compile(r'/.*'), web)]


class Application(object):

    def __call__(self, environ, start_response):
        for rule, func in ROUTE_MAP:
            if rule.match(environ['PATH_INFO']):
                return func(environ, start_response)
        return web(environ, start_response)

app = Application()
