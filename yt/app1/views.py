import os
import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv  # For loading environment variables

# Load environment variables from .env file
load_dotenv()

# Configure Google Gemini AI using the API key from .env
API_KEY = os.getenv("GENAI_API_KEY")
if not API_KEY:
    raise ValueError("API Key not found. Make sure to set it in the .env file.")

genai.configure(api_key=API_KEY)

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

def generate_content(prompt):
    """Generates content based on the provided prompt."""
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)
        chat_session = model.start_chat()  # Start chat session properly
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"

def generate_title(request):
    """Handles form submission and generates a YouTube title."""
    if request.method == 'POST':
        description = request.POST.get('description', '').strip()
        if description:
            prompt = f"Generate a catchy YouTube video title for this description: \"{description}\""
            generated_title = generate_content(prompt)
            return JsonResponse({"generated_title": generated_title})
        else:
            return JsonResponse({"error": "Description cannot be empty"}, status=400)
    
    return render(request, 'generate_title.html')
