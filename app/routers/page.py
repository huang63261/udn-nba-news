from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def news_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/{id}", response_class=HTMLResponse)
def news_detail(request: Request):
    return templates.TemplateResponse("detail.html", {"request": request})
