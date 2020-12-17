from handlers.BaseHandler import *
import os
import string
import random

class UploadHandler(BaseHandler):
    async def get(self):
        self.render("upload.html")

    async def post(self):
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        extension = os.path.splitext(original_fname)[1]
        fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        final_filename= fname+extension
        output_file = open("static/uploads/" + final_filename, 'wb')
        output_file.write(file1['body'])
        self.finish("file: " + final_filename + " is uploaded")