from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def stazone_today(request):
    images = Image.objects.all()
    print(images)
    return render(request,'all-stazone/today-stazone.html',{"images":images})

def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("pofile")
        searched_profiles = Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request,'all-insta/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "Nothing searched"
        return render(request,'all-stazone/search.html',{"message":message})
