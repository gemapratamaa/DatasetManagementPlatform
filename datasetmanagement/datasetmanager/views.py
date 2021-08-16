from django.shortcuts import render

from .models import Document
from .forms import DocumentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST,)
    return render(request, 'upload.html')