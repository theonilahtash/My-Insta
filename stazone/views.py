from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image
from .forms import StazoneLetterForm


# Create your views here.
def welcome(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'welcome.html',{"images":images})


def stazone_today(request):
    if request.method == 'POST':
        form = StazoneLetterForm(request.POST)
        if form.is_valid():
            print('valid')

    else:
        form = StazoneLetterForm()
    return render(request,'all-stazone/today-stazone.html',{"letterForm":form})

def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("pofile")
        searched_profiles = Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request,'all-stazone/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "Nothing searched"
        return render(request,'all-stazone/search.html',{"message":message})

def profile(request,profile_id):
    try:
        profile = Profile.objects.get(id = profile_id)
    except DoesNotExist:
        raise Http404()
        return render(request,"all-stazone/profile.html", {"profile":profile})

