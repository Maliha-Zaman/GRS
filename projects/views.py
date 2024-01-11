import hashlib
import secrets
import re
from django.core.mail import send_mail
from keytotext import pipeline
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from subprocess import Popen
import subprocess
import googletrans
from happytransformer import HappyTextToText
from happytransformer import TTSettings
from googletrans import Translator
nlp = pipeline("k2t")

# keywords = ['Apple', 'Iphone', 'Samsung']
# print(nlp(keywords))
args = TTSettings(num_beams=5, min_length=1)
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
def is_valid_password(password):
    # Check if the password meets the criteria
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return re.match(regex, password)
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            verification_token = secrets.token_hex(16)
            if not is_valid_password(password):
                return render(request, 'registration/signup.html', {'form': form, 'error_message': 'Password must be at least 8 characters long, contain at least one special character, one uppercase letter, and one lowercase letter.'})
            if password != confirm_password:
                return render(request, 'registration/signup.html', {'form': form, 'error_message': 'Passwords do not match.'})

        

            # Check if the email already exists in the database
            if User.objects.filter(email=email).exists():
                return render(request, 'registration/signup.html', {'form': form, 'error_message': 'Email already exists.'})

            # Create a new user instance and save it to the database
            
            hashed_password = make_password(password)
           
            user = User(username=username, email=email, password=hashed_password,verification_token=verification_token)
            user.save()
            verification_url = f"http://127.0.0.1:8000/verify/{verification_token}/"
            send_mail(
                'Verify Your Email',
                f'Click the following link to verify your email: {verification_url}',
                'grs334669@gmail.com',
                [user.email],
                fail_silently=False,
            )
            messages.success(request, 'Verification email has been sent. Please check your email to verify your account.')
            return render(request, 'registration/signup.html', {'form': form})
            
            # Redirect to the login page after successful registration
           
    else:
        form = RegistrationForm()

    return render(request, 'registration/signup.html', {'form': form})

def verify_email(request, verification_token):
    try:
        user = User.objects.get(verification_token=verification_token, is_verified=False)
        # Mark the user as verified
        user.is_verified = True
        user.save()
        return render(request, 'registration/login.html')
    except User.DoesNotExist:
        messages.error(request, 'Email verification failed. Please try again or contact support.')
        return redirect('registration/signup.html')
    
# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
            

#             try:
                
#                 user = User.objects.get(email__iexact=email)
#                 print(f"Entered password: {password}")
#                 print(f"Stored password hash: {user.password}")
#                 if user and check_password(password, user.password) and user.is_verified:
                    
#                     print("correctttt wowho")
#                     # Correct password and verified user
#                     session = Session(session_key=str(user.id))
#                     session.expire_date = timezone.now() + timedelta(days=7)  
#                     session.save()
#                     request.session['user_id'] = user.id
#                     return redirect('home')  # Redirect to the dashboard after successful login
#                 else:
#                     messages.error(request, 'Invalid login credentials.')
#                     print("User does not exist or passwords do not match")
#                     return render(request, 'verificatio_failed.html')
#             except User.DoesNotExist:
#                 messages.error(request, 'Invalid login credentials.')

#     else:
#         form = LoginForm()

#     return render(request, 'registration/login.html', {'form': form})

def login(request):
    error_message = None  # Initialize error_message to None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email__iexact=email)
                print(f"Entered password: {password}")
                print(f"Stored password hash: {user.password}")
                if user and check_password(password, user.password) and user.is_verified:
                    print("correctttt wowho")
                    # Correct password and verified user
                    session = Session(session_key=str(user.id))
                    session.expire_date = timezone.now() + timedelta(days=7)
                    session.save()
                    request.session['user_id'] = user.id
                    return redirect('home')  # Redirect to the dashboard after successful login
                else:
                    error_message = 'Wrong email or password!'  # Set error_message
                    print("User does not exist or passwords do not match")
            except User.DoesNotExist:
                error_message = 'User does not exist'  # Set error_message
                print("User does not exist")
        else:
            error_message = 'Form is not valid. Please check your input.'  # Set error_message for form validation errors
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})


def home(request):
    user = None
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None

    return render(request, 'home.html', {'user': user})

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')




def start_backend(request):
    re = ""
    re1 = ""
    if request.method == 'POST':
        # Check if the button was clicked
        if 'start_button' in request.POST:
            # Start the backend script (app.py)
            # Popen(["python", "app.py"])
            result = subprocess.check_output(['python', 'app.py'], universal_newlines=True)
            result = ' '.join(result.splitlines())
            # re = (nlp(result))
            re = happy_tt.generate_text(result, args=args)
            translator = Translator()
            re1 = translator.translate(re, dest='bn').text
    return render(request, 'start_backend.html',{'gestures_output': re, 'gestures_output_bangla': re1})
def start_backendMultiple(request):
    re = ""
    re1 = ""
    if request.method == 'POST':
        # Check if the button was clicked
        if 'start_button' in request.POST:
            # Start the backend script (app.py)
            # Popen(["python", "app.py"])
            result = subprocess.check_output(['python', 'app.py'], universal_newlines=True)
            result = ' '.join(result.splitlines())
            # re = (nlp(result))
            re = happy_tt.generate_text(result, args=args)
            translator = Translator()
            re1 = translator.translate(re, dest='bn').text
    return render(request, 'start_backendMultiple.html',{'gestures_output': re, 'gestures_output_bangla': re1})
# whisper api
def gestureTest(request):
    re = ""
    re1 = ""
    if request.method == 'POST':
        # Check if the button was clicked
        if 'start_button' in request.POST:
            # Start the backend script (app.py)
            # Popen(["python", "app.py"])
            result = subprocess.check_output(['python', 'app.py'], universal_newlines=True)
            result = ' '.join(result.splitlines())
            # re = (nlp(result))
            re = happy_tt.generate_text(result, args=args)
            translator = Translator()
            re1 = translator.translate(re, dest='bn').text
    return render(request, 'gestureTest.html',{'gestures_output': re, 'gestures_output_bangla': re1})

def send_password_reset_email(user):
    token = secrets.token_urlsafe(20)  # Generate a random token
    user.password_reset_token = token
    user.save()

    reset_link = f"http://127.0.0.1:8000/reset/{token}/"  # Replace with your actual domain
    send_mail(
        'Password Reset Request',
        f'Click the following link to reset your password: {reset_link}',
        'grs334669@gmail.com',
        [user.email],
        fail_silently=False,
    )

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            send_password_reset_email(user)
            messages.success(request, 'Password reset email sent successfully. Check your email.')
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
    return render(request, 'password_reset_request.html')

def password_reset(request, token):
    user = get_object_or_404(User, password_reset_token=token)
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        user.password = make_password(new_password)
        user.password_reset_token = None  # Reset the token after password change
        user.save()
        messages.success(request, 'Password reset successful. You can now log in.')
        return redirect('login')
    return render(request, 'password_reset.html') 

def features(request):
    
    return render(request, 'features.html')

def display_gestures(request):
    # Run your script to get hand gestures
    result = subprocess.check_output(['python', 'app.py'], universal_newlines=True)
    
    # Pass the result to the template
    return render(request, 'gestures.html', {'gestures_output': result})
