# -*- coding: utf-8 -*-

from tornado.web import Application
from tornado.web import url
from tornado.options import define
from tornado.options import options
from tornado.options import parse_command_line
from tornado.options import parse_config_file
import tornado.ioloop
import logging

from src.handlers import *

define(
    'conf',
    default='/path/to/conf/file.conf',
    help='location of configuration file.',
    type=str
)
define(
    'dev',
    default=False,
    help='Development toggle, enables auto reloading.',
    type=bool
)
define(
    'client_key',
    default=None,
    help='Your magazine\'s client key to the API',
    type=str
)
define(
   'port',
   default=8888,
   help='The port the app runs on.',
   type=int
)

class App(Application):
    def __init__(self):
        handlers = [
            url(r"/webhook/?$", Webhook, name="/webhook"),
        ]

        settings = {
            'client_key': options.client_key,
            'debug': options.dev
        }

        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    try:
        parse_config_file(options.conf)
        logging.info("Loaded conf file from %s" % options.conf)
    except SyntaxError as error:
        logging.error("Error in conf file: %s" % error)
    except IOError as error:
        logging.error("Conf file missing: %s" % error)

    parse_command_line()
    app = App()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
