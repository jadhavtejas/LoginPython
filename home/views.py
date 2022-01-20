from email import message
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request,'home/register.html')


    # view for user registration
def UserRegistration(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password= request.POST['password']
        cpassword= request.POST['cpassword']

        # first we will valiadate that user already exist
        user = User.objects.filter(Email=email)

        if user:
            message = "User Already Exist"
            return render(request,'home/register.html',{'msg' : message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "User register Successfully"
                return render(request,"home/login.html",{'msg' : message})
            else:
                message = "Password and Confirm password Does Not Match"
                return render(request,"home/register.html",{'msg' : message})


#login view
def loginpage(request):
    return render(request,'home/login.html')

def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        #Checking the email id with database
        user = User.objects.get(Email = email)
        if user:
            if user.Password == password:
                # We are getting user data in session
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                return render(request,'home/home.html')
            else:
                message = "Password Does Not Match"
                return render(request,'home/login.html',{'msg':message})
        else:
            message = "User Does Not Exist"
            return render(request,'home/register.html',{'msg':message})

def student(request):
    return redirect('https://studentlearningbca.github.io/T/index.html')
