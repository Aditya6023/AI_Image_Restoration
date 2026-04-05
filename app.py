from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import shutil
import os

from model.restore import restore_image

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context={}
    )

@app.post("/restore")
async def restore(file: UploadFile = File(...)):

    input_path = os.path.join(UPLOAD_DIR, file.filename)
    output_path = os.path.join(
        OUTPUT_DIR,
        "restored_" + file.filename
    )

    # save upload
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🔥 AI MODEL CALL
    restore_image(input_path, output_path)

    return FileResponse(output_path, media_type="image/png")