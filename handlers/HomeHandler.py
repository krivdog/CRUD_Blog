from handlers.BaseHandler import *

class HomeHandler(BaseHandler):
    async def get(self):
        entries = await self.query(
            "SELECT * FROM entries ORDER BY published DESC LIMIT 5"
        )
        if not entries:
            self.redirect("/compose")
            return
        self.render("home.html", entries=entries)