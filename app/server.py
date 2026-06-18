from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import products, orders  # Connects your custom routing modules

#1. Initialize the FastAPI application with metadata
app = FastAPI(
    title="Virtual Store API",
    description="Enterprise-grade architecture for managing inventory and customer orders",
    version="1.0.0",
)

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

@app.get("/")
def read_root():
    return {"message": "Welcome to the enterprise-grade Virtual Store API!"}