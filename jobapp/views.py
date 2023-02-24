from django.shortcuts import render
from django.shortcuts import render, redirect
import uuid
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from jobportal.settings import EMAIL_HOST_USER
from django.db.models import Q

def index(request):
    return render(request, 'index.html')


def regis(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).first():  # it will get the first object from filter query
            messages.success(request, 'username already taken')
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request, 'email already taken')
            return redirect(regis)
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        auth_token = str(uuid.uuid4())  # uuid module is a special field to store universal unique identifiers
        # uuid4 is randomly generated 128bit identifier that generates a hexadecimal token
        profile_obj = comp.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email, auth_token)
        return redirect(success)
    return render(request, 'compreg.html')


def send_mail_regis(email, token):
    subject = "your account has been verified"
    message = f'paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)


def success(request):
    return render(request, 'success.html')

def error(request):
    return render(request, 'error.html')

def verify(request, auth_token):
    profile_obj = comp.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request, 'your account is already verified')
            return redirect(login)
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request, 'your account has been verified')
        return redirect(login)
    else:
        return redirect(error)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter( Q(email=email) | Q(username=email) ).first()

        print(user_obj)
        if user_obj is None:
            messages.success(request, 'user not found')
            return redirect(login)

        profile_obj = comp.objects.filter(user=user_obj).first()
        print(profile_obj)
        if not profile_obj.is_verified:
            messages.success(request, 'profile not verified check your mail')
            return redirect(login)

        user = authenticate(username=user_obj, password=password)
        print(user)

        if user is None:
            messages.success(request, 'wrong password or username')
            return redirect(login)
        obj = comp.objects.filter(user=user)
        return render(request, 'compprofile.html', {'obj': obj})
    return render(request, 'complogin.html')





def prodisp(request):
    return render(request, 'compprofile.html')


def indexjob(request):
    return render(request, 'indexjob.html')


def postjobdef(request):
    if request.method == 'POST':
        obj = postjobform(request.POST)
        if obj.is_valid():
            cname1 = obj.cleaned_data['cname']
            email1 = obj.cleaned_data['email']
            jtitle1 = obj.cleaned_data['jtitle']
            wtype1 = obj.cleaned_data['wtype']
            expreq1 = obj.cleaned_data['expreq']
            jtype1 = obj.cleaned_data['jtype']
            m = postjob(cname=cname1, email=email1, jtitle=jtitle1, wtype=wtype1, expreq=expreq1, jtype=jtype1)
            m.save()
            return redirect(jobsuces)
        else:
            return HttpResponse("error")
    return render(request, 'indexjob.html')


def jobsuces(request):
    return render(request, 'jobsuccess.html')


def table(request):
    abc = User.objects.all()
    li = []
    email = []
    id = []
    for i in abc:
        idd = i.id
        nm = i.username
        em = i.email

        id.append(idd)
        li.append(nm)
        email.append(em)

    id1 = id[1:]
    li1 = li[1:]
    em1 = email[1:]
    mylist = zip(li1, em1, id1)
    return render(request, 'company.html', {'mylist': mylist})


def sendmaildef(request, id):
    a = User.objects.filter(id=id)

    return render(request, 'sendmailhtml.html', {'a':a})

def sendit(request,id):
    subject=request.GET.get('subject')
    message=request.GET.get('content')
    # print(s1,c1)
    obj = User.objects.get(id=id)
    email_from = EMAIL_HOST_USER
    recipient = [obj.email]
    send_mail(subject, message, email_from, recipient)
    return HttpResponse("Mail sent")

######################################################################

def empregis(request):
    if request.method == 'POST':
        a = formempreg(request.POST)
        if a.is_valid():
            unm = a.cleaned_data['username']
            eml = a.cleaned_data['email']
            dob = a.cleaned_data['dob']
            qul = a.cleaned_data['quali']
            phn = a.cleaned_data['phno']
            psd = a.cleaned_data['password']
            cps = a.cleaned_data['cpassword']
            print(unm,eml,dob,qul,phn,psd,cps)
            if psd == cps:
                b = modelempreg1(username=unm, email=eml, dob=dob, quali=qul, phno=phn, password=psd)
                b.save()
                return HttpResponse("registration success")
            else:
                return HttpResponse("Password incorrect")
        else:
            return HttpResponse("Registration failed")
    return render(request, '1empreg.html')


def emplogin(request):
    if request.method == 'POST':
        a = emplogform(request.POST)
        if a.is_valid():
            mm = a.cleaned_data['m']
            pp = a.cleaned_data['p']
            b = modelempreg1.objects.all()
            for i in b:
                if mm == i.email and pp == i.password:
                    a1=i.username
                    b1=i.email
                    c1=i.dob
                    d1=i.quali
                    e1=i.phno
                    f1=i.id
                    return render(request,'3empprof.html',{'a1':a1,'b1':b1,'c1':c1,'d1':d1,'e1':e1,'f1':f1})
            else:
                return HttpResponse("Login failed")
    return render(request, '2emplogin.html')


def viewjob(request,id):
    b1=modelempreg1.objects.filter(id=id)
    for i in b1:
        x1=i.username
        x2=i.id

    a1=postjob.objects.all()
    l1=[]
    l2=[]
    l3=[]
    for i in a1:
        b1=i.jtitle
        l1.append(b1)
        b2=i.cname
        l2.append(b2)
        b3=i.id
        l3.append(b3)
    list=zip(l1,l2,l3)
    return render(request,'5viewjob.html',{"list":list,"x1":x1,"x2":x2})


def viewmore(request,id,pk):
    a1=postjob.objects.get(id=id)
    b1=modelempreg1.objects.get(id=pk)
    return render(request,'6viewmore.html',{"a1":a1,"b1":b1})

def applynow(request,id,pk):
    a1 = postjob.objects.get(id=id)
    b1 = modelempreg1.objects.get(id=pk)
    if request.method=='POST':
        a=applyform(request.POST,request.FILES)
        if a.is_valid():
            compnm1 = a.cleaned_data['compnm']
            jobtitle1 = a.cleaned_data['jobtitle']
            empname1 = a.cleaned_data['empname']
            empemail1 = a.cleaned_data['empemail']
            empph1 = a.cleaned_data['empph']
            exp1 = a.cleaned_data['exp']
            pdf1=a.cleaned_data['pdf']
            b=applymodel(compnm=compnm1,jobtitle=jobtitle1,empname=empname1,empemail=empemail1,empph=empph1,exp=exp1,pdf=pdf1)
            b.save()
            return HttpResponse("Job application successful")
        else:
            return HttpResponse("error")
    return render(request, '7apply.html', {"a1": a1, "b1": b1})

def editprof(request,id):
    prof=modelempreg1.objects.get(id=id)
    return render(request,'4editprof.html',{'prof':prof})

def updateprof(request,id):
    prof = modelempreg1.objects.get(id=id)
    po = formempreg(request.POST, instance=prof)
    po.save()
    return redirect(emplogin)


