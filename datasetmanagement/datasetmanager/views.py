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
def task_list(request):
    datasets = Dataset.objects.all()
    arguments = {
        'datasets' : datasets
    }
    return render(request, 'task_list.html', arguments)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/home')


def handle_task(request, action: str, task_id: int):
    arguments = dict()

    if request.method == 'GET':
        print("[views] handle task, task id: {}, action: {}".format(task_id, action))
        task = Dataset.objects.get(id=task_id)
        print("[handle_task] target task: ", task)
        if action == 'book':
            print("[handle_task] [book] user:", request.user)
            print("[handle_task] bookers before booking:", task.booker.all())
            task.booker.add(request.user)
            print("[handle_task] bookers after booking:", task.booker.all())
        elif action == 'revoke':
            print("[handle_task] [revoke] user:", request.user)
            print("[handle_task] bookers before revoke:", task.booker.all())
            task.booker.remove(request.user) 
            print("[handle_task] bookers after revoke:", task.booker.all())
        elif action == 'delete':
            print("[handle_task] [delete] user:", request.user)
            print("[handle_task] before delete:", task.is_deleted)
            task.is_deleted = True
            print("[handle_task] after delete:", task.is_deleted)

        task.save()

    arguments['datasets'] = Dataset.objects.all()
    return render(request, 'task_list.html', arguments)
        
"""
def revoke_task(request, task_id):
    if request.method == 'GET':
        print("[views] revoke_task")
        task = Dataset.objects.get(id=task_id)
        
    return render(request, 'download.html')
# Soft delete
def delete_task(request, task_id):
    if request.method == 'GET':
        print("[views] delete_task")
        task = Dataset.objects.get(id=task_id)
        
    return render(request, 'download.html')
"""