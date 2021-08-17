from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


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
    
def upload_page(request):
    arguments = dict()
    arguments['form'] = DatasetUploadForm(request.POST, request.FILES)

    if request.method == 'POST':
        
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("[upload page] request.post: ", request.POST)
            print("[upload page] request.files: ", request.FILES)
            form.save()
           
        #form = DatasetUploadForm(request.POST, request.FILES)
        #if form.is_valid():
        #    new_dataset = Dataset()
    else:
        form = DatasetUploadForm()

    return render(request, 'upload.html', arguments)

def download_page(request):
    return render(request, 'download.html')