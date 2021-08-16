from django.shortcuts import render

from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request, 'index.html')



def login(request):
    return render(request, 'login.html')
    
def upload(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            new_dataset = Dataset()



    return render(request, 'upload.html')