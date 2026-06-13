from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    return HTMLResponse("Welcome to the home page.<br><br><a href='/about'>About</a> | <a href='/services'>Services</a> | <a href='/contact'>Contact</a>")

@app.get("/about")
def about():
    return HTMLResponse("We build clean and modern web applications.<br><br><a href='/'>Home</a> | <a href='/services'>Services</a> | <a href='/contact'>Contact</a>")

@app.get("/services")
def services():
    return HTMLResponse("Providing lightning-fast APIs and premium user interfaces.<br><br><a href='/'>Home</a> | <a href='/about'>About</a> | <a href='/contact'>Contact</a>")

@app.get("/contact")
def contact():
    return HTMLResponse("Reach out to us at hello@example.com.<br><br><a href='/'>Home</a> | <a href='/about'>About</a> | <a href='/services'>Services</a>")

@app.get("/user/{user_id}")
def get_user(user_id: str):
    return HTMLResponse(f"User ID: {user_id}<br><br><a href='/'>Home</a>")
