from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image
from .forms import StazoneLetterForm
from .email import send_welcome_email


# Create your views here.
def welcome(request):
    if request.method == 'POST':
        form = StazoneLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = StazoneLetterRecipients(name = name,email = email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('welcome.html')
            print('valid')

    else:
        form = StazoneLetterForm()
    return render(request, 'welcome.html',{"letterForm":form})


def stazone_today(request):
    images = Image.objects.all()
    print(images)
    return render(request,'all-stazone/today-stazone.html',{"images":images})

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

