from django.shortcuts import render
from .models import Picture

# Create your views here.


def hello(request):
    pictures = Picture.objects.all()
    context = {
        'pictures': pictures
    }
    return render(request, 'hello.html', context)
