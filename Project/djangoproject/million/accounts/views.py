# from django.db.transaction import commit
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib import messages
# from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
# from django.shortcuts import render, redirect
# from home.models import MyUser
# from django.core.mail import send_mail
# from django.core.mail import EmailMessage
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from .utils import token_generator


def accounts(request):
    return HttpResponse("you dont have password")

# def signup(request):
#     return render(request, "html/signup.html")

# def forgot(request):
#     return render(request, "html/forgot.html")

# def guest(request):

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         #if MyUser.objects.filter(email=request.POST['email']).exists():
#         user=MyUser.objects.get(email=email)

#         if user is not None:
#             if user.passwordok:
#                 return HttpResponse("Please login")
#             else:
#                 return HttpResponse("you dont have password")
#         else:
#             user = MyUser.objects.create_user(email=email)
#             user.active = False
#             user.passwordok = False
#             user.save()
#             return HttpResponse("Thanks for registration")
#     else:
#         return HttpResponse("404 not found")

# def demo(request):

#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         email = request.POST.get('phone')
#         #if MyUser.objects.filter(email=request.POST['email']).exists():
#         user=MyUser.objects.get(email=email)

# #33333333333333333333333333333333333333333333333333333333


# # #333333333333333333333333333333333333333333333333333333333

# # def signup(request):
# #     if request.method == 'POST':
# #         email = request.POST.get('email')
# #         if MyUser.objects.filter(email=request.POST['email']).exists():
# #             return HttpResponse("This email has been already taken")
# #         else:
# #             user = MyUser.objects.create_user(email=email)
# #             user.active = False
# #             user.save()
# #             domain = get_current_site(request).domain
# #             email_subject = 'Activate Your Account'
# #             uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
# #             print(uidb64)
# #             print(user.pk)
# #             link = reverse('activate', kwargs={
# #                 'uidb64': uidb64, 'token': token_generator.make_token(user)})
# #             activate_url = 'http://'+domain+link
# #             email_body = 'Hi ' +user.email+ ' please use this link to verify your account '+activate_url
# #             email = EmailMessage(
# #                 email_subject,
# #                 email_body,
# #                 'norep@pep.com',
# #                 [email],
# #             )
# #             email.send(fail_silently=False)

# #             return HttpResponseRedirect(reverse('search'))

# #     else:
# #         return HttpResponse(" 404 not found")
# #         # return render(request, 'html/search.html', context)
# #         # return HttpResponseRedirect(reverse('profile'))


# # def activate(request, uidb64, token):
# #     try:
# #         id = force_bytes(urlsafe_base64_decode(uidb64))
# #         print(id)
# #         user = MyUser.objects.get(pk=id)
# #         print(user)

# #         if not token_generator.check_token(user, token):
# #             return redirect('home'+'message='+'User has already activated')
# #         if user.active:
# #             return HttpResponseRedirect(reverse('search'))
# #         user.active = True
# #         user.save()
# #         messages.success(request, 'Account is activated successfully')
# #         return HttpResponseRedirect(reverse('search'))
# #     except Exception as ex:
# #         pass
# #     return redirect('home')


# # def login(request):
# #     if request.method == 'POST':
# #         email = request.POST.get('email')
# #         password = request.POST.get('password')
# #         user = authenticate(email=email, password=password)
# #         if user is not None:
# #             messages.success(request, "successful logged in")
# #             return redirect("profile")
# #         else:
# #             print("Someone tried to login and failed.")
# #             return HttpResponse("Invalid login details given")
# #     else:
# #         return HttpResponse('404 not found')

# # def changepass(request):
# #     pass
# #     # if request.method == 'POST':
# #     #     password = request.POST.get('password1')
# #     #     password1 = request.POST.get('password2')
# #     #     user = authenticate(email=email, password=password)
# #     #     if user is not None:
# #     #         messages.success(request, "successful logged in")
# #     #         return redirect("profile")
# #     #     else:
# #     #         print("Someone tried to login and failed.")
# #     #         return HttpResponse("Invalid login details given")
# #     # else:
# #     # return HttpResponse('404 not found')

