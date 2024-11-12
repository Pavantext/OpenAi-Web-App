from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
import openai
from django.conf import settings
import os
from openai import OpenAI

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def LoginView(request):
    return render('login.html')
    
def logout_view(request):
    logout(request)
    return redirect('home')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def home_view(request):
    return render(request, 'home.html')

# openai.api_key = settings.OPENAI_API_KEY

# def create_script_view(request):
#     script = None
#     if request.method == 'POST':
#         topic = request.POST.get('topic')
#         if topic:
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant who writes scripts."},
#                     {"role": "user", "content": f"Write a detailed script about {topic}."}
#                 ],
#                 max_tokens=300
#             )
#             script = response['choices'][0]['message']['content'].strip()
           
#     return render(request, 'script.html', {'script': script})

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def create_script_view(request):
    script = None
    if request.method == 'POST':
        topic = request.POST.get('topic')
        if topic:
            try:
                # Use the new client-based approach to call the chat completion API
                response = client.chat.completions.create(
                    messages=[
                        {"role": "user", "content": f"Write a detailed script about {topic}."}
                    ],
                    model="gpt-3.5-turbo"
                )
                # Extract the generated script from the response
                script = response['choices'][0]['message']['content'].strip()
            except Exception as e:
                # Handle any errors with a generic message
                script = f"An error occurred: {str(e)}"
    
    return render(request, 'script.html', {'script': script})