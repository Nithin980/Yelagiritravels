from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user
from .utils import send_otp
from datetime import datetime
import pyotp
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .models import Car


def Travels(request):
    return render(request,'base.html')

def About(request):
    return render(request,'about.html')


def Signup(request):
    form=CreateUserForm()
    if request.method =='POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            error=Otp(request)
            if error is None:
                form.save()
                print('signup successful')
                messages.success(request,'Registration success you can login now')
                return redirect(Signin)
            else:
                return  HttpResponse(
                json.dumps({ "error": error}),
                content_type="application/json"
                )
    
    return render(request,'Signup.html',{'form':form})


def Otp(request):
    print('in otp')
    error_message=None  
    if request.method =='POST':
        otp=request.POST['otp']
        print(otp)
        request.session['username']=request.POST['username']

        otp_secret_key= request.session['otp_secret_key']
        print(otp_secret_key)
        otp_valid_until=request.session['otp_valid_date']
        print(otp_valid_until)
        if otp_secret_key and otp_valid_until is not None:
            valid_until=datetime.fromisoformat(otp_valid_until)
            if valid_until > datetime.now():
                totp=pyotp.TOTP(otp_secret_key,interval=120)
                if totp.verify(otp):
                    #user=get_object_or_404(User,username=username)
                    #Signin(request,user)

                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']
                    error_message=None
                    #messages.error(request,'invalid one time password')
                    
                else:
                    error_message ='invalid one time password'
                    #messages.error(request,'invalid one time password')
            else:
                error_message='otp expired'
                #messages.error(request,'otp expired')
        else:
            error_message='something went wrong'
            #messages.error(request,"something went wrong")

    return error_message


def Signin(request):
    form=LoginForm()
    if request.method =='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect(Dashboard)
        
    return render(request,'Signin.html',{'form':form})

@login_required
def Signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect('/yelagiritravels')

@login_required
def Dashboard(request):  
    
    cars = Car.objects.all()
    return render(request,'dashboard.html',{'cars':cars})


@login_required
def Book(request):
    form=BookForm()
    if request.method =='POST':
        form =BookForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect(success)
    cars = Car.objects.all()
    return render(request,'book.html',{'form':form,'cars':cars})

def Triggerotp(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        print(email)
        print(request.GET.get('subjecttype'))
        send_otp(request)
        response_data = 'successful!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def forgotpass(request):
    form=CreateUserForm()
    if request.method =='POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            error=Otp(request)
            if error is None:
                print('signup successful')
                messages.success(request,'Registration success you can login now')
                return redirect(Signin)
            else:
                return  HttpResponse(
                json.dumps({ "error": error}),
                content_type="application/json"
                )
    
    return render(request,'otp.html',{'form':form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeCustomForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def success(request):
    return render(request,'success.html')


@login_required
def Mybookings(request):
    loggedinuser=get_user(request)
    book = Booking.objects.filter(username=loggedinuser)
    return render(request,'mybookings.html',{'book':book})

