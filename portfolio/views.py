from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .forms import getInTouchForm
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    return render(request,'portfolio/home.html')

def abt(request):
    return render(request,'portfolio/about.html')

def work(request):
    return render(request,'portfolio/work.html')

def contact(request):
    if request.method == "POST":
        form = getInTouchForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            name=form['fullname']
            emil = form['email']
            mobile = form['phone']
            msg = form['msg']
            datamsg = "Name"+name+"Email"+emil
            email = EmailMessage('Web Development Client',datamsg,to=['avinashvarpeti1@gmail.com'])
            print(email)
            email.send()
            return render(request,'portfolio/contact.html',{'msg':"Your Message Has Been Sent Successfully.",'form':form})
    else:
        form = getInTouchForm()
        return render(request,'portfolio/contact.html',{'form':form})