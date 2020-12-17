import tornado.web
import os.path

from handlers.ArchiveHandler import ArchiveHandler
from handlers.AuthLoginHandler import AuthLoginHandler
from handlers.AuthLogoutHandler import AuthLogoutHandler
from handlers.AuthCreateHandler import AuthCreateHandler
from handlers.ComposeHandler import ComposeHandler
from handlers.EntryHandler import EntryHandler
from handlers.FeedHandler import FeedHandler
from handlers.HomeHandler import HomeHandler
from handlers.GalleryHandler import GalleryHandler
from handlers.UploadHandler import UploadHandler

class EntryModule(tornado.web.UIModule):
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)

class Application(tornado.web.Application):
    def __init__(self, db):
        self.db = db
        handlers = [
            (r"/", HomeHandler),
            (r"/archive", ArchiveHandler),
            (r"/feed", FeedHandler),
            (r"/entry/([^/]+)", EntryHandler),
            (r"/compose", ComposeHandler),
            (r"/auth/create", AuthCreateHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
            (r"/gallery", GalleryHandler),
            (r"/upload", UploadHandler)
        ]
        settings = dict(
            blog_title=u"Tornado Blog",
            template_path=os.path.join(os.path.dirname(__file__), "../templates"),
            static_path=os.path.join(os.path.dirname(__file__), "../static"),
            ui_modules={"Entry": EntryModule},
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
        )
        super().__init__(handlers, **settings)