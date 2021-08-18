from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.http.response import FileResponse, Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datasetmanagement import settings
import os
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
            data_to_submit = form.save(commit=False)
            file_name = request.FILES['file'].name
            data_to_submit.name = file_name
            data_to_submit.save()
            print("[upload page] request.post: ", request.POST)
            print("[upload page] request.files: ", request.FILES)
            print("[upload page] request.files['file']: ", request.FILES['file'], type(request.FILES['file']))
            print("[upload page] file name: ", request.FILES['file'].name, type(request.FILES['file'].name))
            #form.save()
            return HttpResponse("Upload success") # TODO GANTI
           
        #form = DatasetUploadForm(request.POST, request.FILES)
        #if form.is_valid():
        #    new_dataset = Dataset()
    else:
        form = DatasetUploadForm()

    return render(request, 'upload.html', arguments)

def download_page(request):
    datasets = Dataset.objects.all()
    arguments = {
        'datasets' : datasets
    }
    return render(request, 'download.html', arguments)

"""
def download_zip(request, zip_id):
    obj = Dataset.objects.get(id=zip_id)
    filename = obj.model_attribute_name.path
    response = FileResponse(open(filename, 'rb'))
    return response
"""

def download(request, path):
    print("[views] masuk download, path = ", path)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        print("os.path.exists({})".format(file_path))
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/datasetupload')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise Http404

"""
def send_file(response):
    img = open('', 'rb')
    response = FileResponse(img)
    return response
"""