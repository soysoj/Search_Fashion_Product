from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .services import search_images, get_image_by_id
from datasets import load_dataset

router = APIRouter()

# 템플릿 설정
templates = Jinja2Templates(directory="app/templates")

# 데이터셋 로드 (이미지 파일)
fashion = load_dataset("ashraq/fashion-product-images-small", split="train")
images = fashion["image"]

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/", response_class=HTMLResponse)
async def search(request: Request, query: str = Form(...)):
    results = search_images(query)
    
    # Convert images to base64 strings
    images_to_display = [get_image_by_id(result["id"], images) for result in results]

    # Pass the base64 images to the template
    return templates.TemplateResponse("index.html", {
        "request": request,
        "results": results,
        "images": images_to_display,
        "zip": zip
    })

