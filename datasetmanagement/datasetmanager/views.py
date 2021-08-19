from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.http.response import FileResponse, Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datasetmanagement import settings
from django.contrib.auth.decorators import login_required

def index_page(request):
    return render(request, 'index.html')


def login_page(request):
    arguments = dict()
    arguments['form'] = LoginForm()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
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
            data_to_submit = form.save(commit=False)
            user_email = request.user.email
            uploader = User.objects.get(email=user_email)
            file_name = request.FILES['file'].name

            data_to_submit.name = file_name
            data_to_submit.uploader = uploader
            data_to_submit.save()

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


@login_required
def handle_task(request, action: str, task_id: int):
    arguments = dict()
    if request.method == 'GET':
        task = Dataset.objects.get(id=task_id)
        if action == 'book':
            if not task.booker:
                task.booker = request.user
        elif action == 'revoke':
            task.booker = None
        elif action == 'delete':
            task.is_deleted = True
        task.save()

    arguments['datasets'] = Dataset.objects.all()

    return render(request, 'task_list.html', arguments)