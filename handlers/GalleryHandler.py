from handlers.BaseHandler import *

class GalleryHandler(BaseHandler):
    async def get(self):
        #entries = await self.query("SELECT * FROM entries ORDER BY published DESC")
        images = await self.query("SELECT * FROM gallery ORDER BY published ASC")
        #self.render("archive.html", entries=entries)
        self.render("gallery.html", images=images)