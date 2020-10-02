#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: MitsuhaYuki
import os.path
import logging
import tornado.ioloop
import tornado.httpserver
from tornado.web import RequestHandler

log = logging.getLogger()


def setHeader(request):
    request.set_header("Access-Control-Allow-Origin", "*")
    request.set_header("Access-Control-Allow-Headers", "*")
    request.set_header("Access-Control-Allow-Method", "*")
    request.set_header("Access-Control-Allow-Credentials", "true")


class MainHandler(RequestHandler):
    def get(self):
        self.write('emby validation server successfully start')

    def post(self):
        self.get()


class ValidateDevice(RequestHandler):
    def get(self):
        setHeader(self)
        data = {"cacheExpirationDays": 365, "message": "Device Valid", "resultCode": "GOOD"}
        self.write(data)

    def post(self):
        self.get()


class Validate(RequestHandler):
    def get(self):
        setHeader(self)
        data = {"featId": "", "registered": True, "expDate": "2099-01-01", "key": ""}
        self.write(data)

    def post(self):
        self.get()


class GetStatus(RequestHandler):
    def get(self):
        setHeader(self)
        data = {"deviceStatus": "0", "planType": "Lifetime", "subscriptions": {}}
        self.write(data)

    def post(self):
        self.get()


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/admin/service/registration/validateDevice", ValidateDevice),
        (r"/admin/service/registration/validate", Validate),
        (r"/admin/service/registration/getStatus", GetStatus)
    ])


if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app, ssl_options={
        "certfile": os.path.join(os.path.abspath("."), "cert/server.crt"),
        "keyfile": os.path.join(os.path.abspath("."), "cert/server.key"),
    })
    http_server.listen(443)
    tornado.ioloop.IOLoop.current().start()
