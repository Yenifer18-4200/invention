from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers import products, orders  

#1. Initialize the FastAPI application with metadata
app = FastAPI(
    title="Virtual Store API",
    description="Enterprise-grade architecture for managing inventory and customer orders",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#2. Adding the CORS middleware configuration to allow cross-origin requests from the frotend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows any frontend website to access the API (for development purposes)
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods (GET, POST, PUT, DELETE, etc,)
    allow_headers=["*"], # Allows all custom headers
)

# Register the modular routers to the core application
app.include_router(products.router)
app.include_router(orders.router)


# ---------- HOME ----------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )

# ---------- DASHBOARD ----------

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"request": request}
    )