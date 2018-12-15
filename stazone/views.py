from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def stazone_today(request):
    images = Image.objects.all()
    print(images)
    return render(request,'all-stazone/today-stazone.html',{"images":images})
