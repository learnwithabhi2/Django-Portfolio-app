from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import UserImage
from .forms import UserImageForm
import random

def home(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('home')
    else:
        form = UserImageForm()

    images = UserImage.objects.all()
    return render(request, 'main/home.html', {
        'form': form,
        'images': images,
    })
