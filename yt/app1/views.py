import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse

# Configure Google Gemini AI
genai.configure(api_key="AIzaSyANU2neHiRfz-IzCbNfVxD-xZyUaBLZrLk")

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

def generate_content(prompt):
    """This function generates content based on the provided prompt."""
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)
    chat_session = model.start_chat(history=[{"role": "user", "parts": [prompt]}])
    response = chat_session.send_message(prompt)
    return response.text

def generate_title(request):
    """This view handles the form submission and generates a title."""
    if request.method == 'POST':
        description = request.POST.get('description', '')
        if description:
            prompt = f"Generate a catchy YouTube video title for this description: \"{description}\""
            generated_title = generate_content(prompt)
            return JsonResponse({"generated_title": generated_title})
    return render(request, 'generate_title.html')