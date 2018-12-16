from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,StazoneLetterRecipients
from .forms import NewImageForm,StazoneLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


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
        message = "searched"
        return render(request,'all-stazone/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):
    try:
        profile = Profile.objects.get(id = profile_id)
    except DoesNotExist:
        raise Http404()
        return render(request,"all-stazone/profile.html", {"profile":profile})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

