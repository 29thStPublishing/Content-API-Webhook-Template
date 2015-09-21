# -*- coding: utf-8 -*-

import tornado.web
import tornado.gen as gen
import tornado.escape
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest

import json
import logging

class Webhook(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")

    def post(self):
        pass