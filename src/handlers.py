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
        self.set_header("Access-Control-Allow-Headers", "Content-Type")

    def write_error(self, error):
        status_code = error.get('status_code', 500)
        title = error.get('title', 'An Error Occurred')
        detail = error.get('detail', '')

        response_object = {
            "status": str(status_code),
            "title": title,
            "detail": detail
        }
        logging.error(detail)
        self.set_status(status_code)
        self.write(response_object)
        self.finish()
        return

    @gen.coroutine 
    def post(self):
        try:
            body = tornado.escape.json_decode(self.request.body)
        except ValueError as error:
            error_resp = {
                'title': 'JSON Body Error',
                'detail': error.message,
                'status_code': 400
            }
            self.write_error(error_resp)
            return

        # method will be 'POST', 'PUT', or 'DELETE'
        method = body.get('method')
        # The base name of the magazine
        magazine = body.get('magazine')
        # collection will be 'articles', 'issues', 'media', or 'volumes'
        collection = body.get('collection')
        # the entry id
        entry_id = body.get('id')
        # the entry's data
        data = body.get('data')

        return
