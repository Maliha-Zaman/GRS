import hashlib
import secrets
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from subprocess import Popen

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            verification_token = secrets.token_hex(16)
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
            return render(request, 'email_sent.html')
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
        return render(request, 'email_verified.html')
    except User.DoesNotExist:
        return render(request, 'verification_failed.html')
    
def login(request):
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
                    messages.error(request, 'Invalid login credentials.')
                    print("User does not exist or passwords do not match")
                    return render(request, 'verification_failed.html')
            except User.DoesNotExist:
                messages.error(request, 'Invalid login credentials.')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


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
    # Start the backend script (app.py)
    Popen(["python", "app.py"])
    return render(request, 'start_backend.html')
