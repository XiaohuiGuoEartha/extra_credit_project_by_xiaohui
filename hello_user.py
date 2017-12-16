from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

class Handler(RequestHandler):
    def get(self):
        user_name = self.get_argument('user')
        show = "Hello, " + user_name
        self.write(show)

if __name__ == "__main__":
    mapping = [(r'/', Handler),]
    app = Application(mapping)
    app.listen(7777)
    IOLoop.current().start()
