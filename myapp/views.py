from email.message import Message
from turtle import position
from unicodedata import category, name
from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    return render(request,'index.html')

@login_required(login_url='/login/')
def indexx(request):
    return render(request,'index-hr.html')

def logoutt(request):
    logout(request)
    return redirect('index')


def logins(request):
    form1=LoginForm()
    if request.method=='POST':
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            print(user)
            if user is not None:         
                 login(request,user)
                 if request.user.roles=='admin':
                    return redirect('index')
                 else:
                    return redirect('index_hr')
   
            else:
              return render(request,'login.html',{'form':form1})
        else:
            messages.info(request,'Enter correct username')
            return render(request,'login.html',{'form':form1})
    return render(request,'login.html',{'form':form1})

@login_required(login_url='/login/')
def listt(request):
    uid = User.objects.filter(roles='hr').order_by('first_name')
    return render(request,'list.html',{'uid':uid})

@login_required(login_url='/login/')
def deletes(request,pk):
    uid = User.objects.get(id=pk)
    uid.delete()
    return redirect('list')

@login_required(login_url='/login/')
def edit(request,pk):
    uid = User.objects.get(id=pk)
    form1 = EditForm(instance = uid)
    if request.method == 'POST':
        form=EditForm(request.POST,instance = uid)
        print('hello')
        if form.is_valid():
            print('hi')
            form.save()
            return redirect('list')
        else:
            print('here')
            return redirect('list')
    else:
            return render(request,'edit.html',{'form':form1})

@login_required(login_url='/login/')
def signupp(request):
    form1=SignUp()
    if request.method == 'POST':
        form=SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Create HR Successfully!')
            return redirect('list')
        else:
            print(form.errors)
            messages.error(request,'Error!')
            return redirect('signup')
    else:
        return render(request,'signup.html',{'form':form1})

    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HR >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
@login_required(login_url='/login/')
def indexx(request):
    return render(request,'index-hr.html')

@login_required(login_url='/login/')
def list_job(request):
    uid = JobPost.objects.filter(user=request.user).order_by('address')[::-1]
    return render(request,'list-job.html',{'uid':uid})

@login_required(login_url='/login/')
def job_create(request):
    form1=JobForm()
    if request.method=='POST':
        form=JobForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            f.save()
            messages.success(request,'JOB POST SUCCESSFULLY!')
            return redirect('list-job')
        else:
            print(form.errors)
            return redirect('job-creates')
    else:
        return render(request,'job-create.html',{'form':form1})

@login_required(login_url='/login/')
def job_edit(request,pk):
    uid = JobPost.objects.get(id=pk)
    form1=JobEditForm(instance=uid)
    if request.method == 'POST':
        form=JobEditForm(request.POST,instance=uid)
        if form.is_valid():
            form.save()
            messages.success(request,'SuccessFully Edit!')
            return redirect('list-job')
        else:
            messages.error(request,'Error!')
            return redirect('list-job')
    else:
        return render(request,'job-edit.html',{'form':form1})

@login_required(login_url='/login/')
def job_delete(request,pk):
    uid = JobPost.objects.get(id=pk)
    uid.delete()
    return redirect('list-job')

@login_required(login_url='/login/')
def candidate_view(request,pk):
    post = JobPost.objects.get(id=pk)
    uid = CandidateProfile.objects.filter(company = post)
    return render (request,'list-candidate.html',{'uid':uid})



#<<<<<<<<<<<<<<<<<<<<<<<<<<<< Candidate >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def job_notification(request):
    uid = JobPost.objects.all()
    return render(request,'job-notification.html',{'uid':uid})

def candidate_profile(request,pk):
    uid = JobPost.objects.get(id=pk)
    form1=candidateform()
    if request.method == 'POST':
        form=candidateform(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.company=uid
            f.save()
            messages.info(request,'Thank You For Apply!!')
            return redirect('job-notifications')
        else:
            print(form.errors)
            messages.error(request,'Error!!')
            return redirect('job-notifications')
    else:
        return render(request,'view-job.html',{'app':form1,'uid':uid})



def search_venue(request):
    if request.method=='POST':
        searched = request.POST['searched']
        venues=JobPost.objects.filter(position__icontains=searched or address__icontain==searched)
    return render(request,'search-venue.html',{'searched':searched,'venues':venues})