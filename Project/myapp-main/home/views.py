from django.db.transaction import commit
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from accounts.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import token_generator
from home.forms import ContactForm
from home.models import ContactInformation
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout
import threading

class EmailThread(threading.Thread):

    def __init__(self, email ):
        self.email = email 
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
 
       

def home(request):

    
    return render(request, "html/home.html")

def SignupPage(request):
    return render(request, "html/signup.html")

def forgot(request):
    return render(request, "html/forgot.html")

def profile(request):
    return render(request, "html/profile.html")


# def password_set2(request):
#    return render(request, "html/password_reset1.html")

def guest(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        #if User.objects.filter(email=request.POST['email']).exists():
        if User.objects.filter(email=request.POST['email']).exists():
            user=User.objects.get(email=email)
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
            # if user.passwordok:
            #     return HttpResponse("Please login")
            # else:
            #     return HttpResponse("you dont have password")
        else:
            user = User.objects.create_user(email=email)
            user.active = True
            user.passwordok = False
            user.save()
            login(request, user)
            domain = get_current_site(request).domain
            email_subject = 'Activate Your Account'
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            link = reverse('activate', kwargs={
                'uidb64': uidb64, 'token': token_generator.make_token(user)})
            activate_url = 'http://'+domain+link
            email_body = 'Hi ' +user.email+ ' please use this link to verify your account '+activate_url
            email = EmailMessage(
                email_subject,
                email_body,
                'norep@pep.com',
                [email],
            )

            EmailThread(email).start()
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        return HttpResponse("404 not found")


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_active:
            print(user.passwordok)
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print("Someone tried to login and failed.")
            return HttpResponse("Invalid login details given")
        

    else:
        return HttpResponse('404 not found')



def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(email=email,password=password)
        user.passwordok=True
        user.active=True
        user.save()
        login(request, user)
        domain = get_current_site(request).domain
        email_subject = 'Activate Your Account'
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        link = reverse('verify', kwargs={
            'uidb64': uidb64, 'token': token_generator.make_token(user)})
        activate_url = 'http://'+domain+link
        email_body = 'Hi ' +user.email+ ' please use this link to verify your account '+activate_url
        email = EmailMessage(
            email_subject,
            email_body,
            'norep@pep.com',
            [email],
        )
        EmailThread(email).start()
        return HttpResponseRedirect(reverse('dashboard'))


def forgot_pass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user is not None:
            domain = get_current_site(request).domain
            email_subject = 'Activate Your Account'
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            link = reverse('password_reset', kwargs={
                'uidb64': uidb64, 'token': token_generator.make_token(user)})
            activate_url = 'http://'+domain+link
            email_body = 'Hi ' +user.email+ ' please use this link to verify your account '+activate_url
            email = EmailMessage(
                email_subject,
                email_body,
                'norep@pep.com',
                [email],
            )
            EmailThread(email).start()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse(" This email does not exist")


def demo(request):
    if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
             obj = ContactInformation() 
             obj.First_Name = form.cleaned_data['First_Name']
             obj.Last_Name = form.cleaned_data['Last_Name']
             obj.Email = form.cleaned_data['Email']
             obj.Phone_Number = form.cleaned_data['Phone_Number']
             obj.save()
             return HttpResponse("you dont have password")
    else:
        return HttpResponse("404 Not Found")
        
        

def activate(request, uidb64, token):
    try:
        id = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)

        print(token_generator.check_token(user, token))
        if not token_generator.check_token(user, token):
            return HttpResponse('account is alrady activated')
        else:
            user.active = True
            user.verified = True
            user.save()
            # messages.success(request, 'Account is activated successfully')
            # return HttpResponseRedirect(reverse('dashboard'))
            return HttpResponse('Account is activated successfully! Please login .')
    except Exception as ex:
        pass
    return HttpResponse("3")



def verifyUserAccount(request, uidb64, token):
    try:
        id = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)

        print(token_generator.check_token(user, token))
        if not token_generator.check_token(user, token):
            return HttpResponse('account is already activated')
        else:
            user.active = True
            user.verified = True
            user.save()
            print(user)
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
    except Exception as ex:
        pass
    return HttpResponse("3")

def get_success_url(self):
    return reverse('mainapp:profile')


def password_reset(request, uidb64, token):
    context = {
        'uidb64':uidb64,
        'token':token
    }
    
    return render(request,'html/password_reset.html',context)

appname='mainapp'   
def password_set(request, uidb64, token):
    if request.method == 'POST':
        context = {
            'uidb64':uidb64,
            'token':token
        }
        password = request.POST.get('password1')
        password1 = request.POST.get('password2')
        print(password)
        if password != password1:
            return HttpResponse('password not matched')
        try:
            id = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            user.set_password(password)
            print(user.check_password)
            user.passwordok=True
            user.save
            return HttpResponse('Password has changed. Please login')

        except DjangoUnicodeDecodeError as identifier:
            return HttpResponse('404 not found')
        
        return render(request,'html/password_reset.html',context)

@login_required(redirect_field_name=None, login_url='home')
def logout(request):
    """logout logged in user"""
    django_logout(request)
    request.session.flush()
    return render(request,'html/home.html')
    
# def password_set1(request):
#     if request.method == 'POST':
#         password = request.POST.get('password1')
#         password1 = request.POST.get('password2')
#         print(password)
#         return HttpResponse('pasword change')
