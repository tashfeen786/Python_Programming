from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create a FastAPI instance
app = FastAPI(title="Simple Text API", 
              description="A simple API for text processing",
              version="1.0.0")

# Define a Pydantic model for the request body
class TextRequest(BaseModel):
    text: str
    uppercase: Optional[bool] = False

# Define a Pydantic model for the response
class TextResponse(BaseModel):
    processed_text: str
    text_length: int

# Define a route (endpoint)
@app.get("/")
def read_root():
    return {"message": "Welcome to our Text Processing API!"}

# Define a POST endpoint for text processing
@app.post("/process-text/", response_model=TextResponse)
def process_text(request: TextRequest):
    # Get the text from the request
    text = request.text
    
    # Check if the text is empty
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    # Process the text (convert to uppercase if requested)
    processed_text = text.upper() if request.uppercase else text
    
    # Create the response
    response = TextResponse(
        processed_text=processed_text,
        text_length=len(processed_text)
    )
    
    return response
