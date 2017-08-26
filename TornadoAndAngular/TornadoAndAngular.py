import Settings
import tornado.web
import tornado.httpserver
from Handler.MainHandler import MainHandler
from Handler.AjaxHandler import AjaxHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/ajax/", AjaxHandler)

        ]
        settings = {
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    http_server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()