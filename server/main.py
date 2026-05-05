import os 
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


# ----- CONTROLLER IMPORTS -----

from controllers.AppController import app_controller


# ----- ENVIRONMENT SETUP -----

load_dotenv()

node_env = os.getenv("NODE_ENV", "prod")
port = int(os.getenv("LISTENING_PORT", 8000))
host = os.getenv("HOST", "127.0.0.1")

app = FastAPI()


# ----- CONTROLLER REGISTRY -----
app.include_router(app_controller.router)


# ----- HEADERS & SECURITY -----

allowed_domains = os.getenv("CORS_ALLOWED_DOMAINS", "")
allowed_domains = allowed_domains.split(",") if allowed_domains else [] # split if exists else empty array

# if env mode is dev allow all domains
if node_env == "dev":
    allowed_domains = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_domains,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"]
)

@app.middleware("http")                               # HTTP header configs
async def security_headers(req: Request, call_next):
    res = await call_next(req)

    res.headers["X-Content-Type-Options"] = "nosniff" # prevents the browser from performing "MIME type sniffing"
    res.headers["X-Frame-Options"] = "DENY"           # prevents the web page from being displayed within an <iframe>, <frame>, or <object>.
    res.headers["X-XSS-Protection"] = "1; mode=block" # activates the browser's built-in reflected XSS filter

    csp = os.getenv("CSP_POLICY", "default-src 'none'")    # determines which external sources are allowed to load resources

    res.headers["Content-Security-Policy"] = csp
    return res


# ----- STATIC FILE & ROOT ROUTE -----

root_dir = os.path.dirname(os.path.abspath(__file__))   # delineate the path of server on system
pub_dir = os.path.join(root_dir, "public")              # delineate folder name of static html page

@app.get("/")
async def read_root():
    return FileResponse(os.path.join(pub_dir, "index.html"))

if os.path.exists(pub_dir):
    app.mount("/", StaticFiles(directory=pub_dir, html=True), name="public") # mount pub dir of server to app


# ----- ERROR HANDLER -----

@app.exception_handler(Exception)
async def exc_handler(req: Request, exc: Exception):
    message = str(exc)
    print(f"ERROR: {message}")

    is_validation = any(keyword in message.lower() for keyword in ["required", "invalid", "exceed"])

    return JSONResponse(
        status_code=400 if is_validation else 500,
        content={"error": message}
    )


# ----- SERVER START -----

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        proxy_headers=True, # Tell uvicorn to parse headers
        forwarded_allow_ips="*" # In production restrict this to the proxy's internal IP
    )
