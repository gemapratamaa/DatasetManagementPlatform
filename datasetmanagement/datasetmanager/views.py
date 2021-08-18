from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.http.response import FileResponse, Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datasetmanagement import settings
from django.contrib.auth.decorators import login_required

import os

def index_page(request):
    return render(request, 'index.html')

def login_page(request):
    arguments = dict()
    arguments['form'] = LoginForm()

    if request.method == 'POST':
        print("[login page] request.post: ", request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Login failed")
            return HttpResponse("Invalid login details given")

    return render(request, 'login.html', arguments)

@login_required
def upload_success(request):
    return render(request, 'upload_success.html')


@login_required
def upload_page(request):
    arguments = dict()
    arguments['form'] = DatasetUploadForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_email = request.user.email # SUKSES
            uploader = User.objects.get(email=user_email)
            print("uploader: ", uploader)
            print("user email/username: ", user_email)

            data_to_submit = form.save(commit=False)
            file_name = request.FILES['file'].name

            data_to_submit.name = file_name
            data_to_submit.uploader = uploader
            print("data_to_submit: ", data_to_submit, type(data_to_submit))
            print("data uploader: ", data_to_submit.uploader, type(data_to_submit.uploader))
            data_to_submit.save()


            
            print("[upload page] request.post: ", request.POST)
            print("[upload page] request.files: ", request.FILES)
            print("[upload page] request.files['file']: ", request.FILES['file'], type(request.FILES['file']))
            print("[upload page] file name: ", request.FILES['file'].name, type(request.FILES['file'].name))
            # return HttpResponse("Upload success") # TODO GANTI
            return redirect('/upload_success')
    else:
        form = DatasetUploadForm()

    return render(request, 'upload.html', arguments)

@login_required
def download_page(request):
    datasets = Dataset.objects.all()
    arguments = {
        'datasets' : datasets
    }
    return render(request, 'download.html', arguments)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/home')