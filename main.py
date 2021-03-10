from fastapi import FastAPI, UploadFile, File
from starlette.responses import HTMLResponse
from model import predict
import os
app = FastAPI()


@app.get("/")
def main():
    content = """
    <body>
    <form action="/upload" enctype="multipart/form-data" method="post">
    <input name="image" type="file">
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)


@app.post("/upload")
def upload_file(image: UploadFile = File(...)):
    file_name = os.getcwd() + "/img/test/" + image.filename.replace(" ", "-")
    with open(file_name, 'wb+') as f:
        f.write(image.file.read())
        f.close()
    return predict(file_name)
