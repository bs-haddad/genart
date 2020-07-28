from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .forms import RegisterForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtForm
from .forms import CustomUserCreationForm
from .genart import *

from .models import * 

def index(request):
    artlist = Art.objects.order_by('-date_created')[:5]
    context = {
        'artlist': artlist,
    }

    return render(request, 'artgen/index.html', context)

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    return render(request, 'artgen/user.html', {'user': user})

def art(request, art_id): 
    art = get_object_or_404(Art, pk=art_id)

    return render(request, 'artgen/art.html', {'art': art})


def handle_uploaded_file(f, id):
    filepath = "/media/images/user/{}".format(id)
    with open(filepath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return filepath

def art_new(request):
    if request.method == "POST":
        form = ArtForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            # form.save()
            art = form.save(commit=True)
            art.creator = request.user
            art.date_created = timezone.now()
            art.save()
            save_path = "./app/media/generated/" + art.title + ".jpg"
            genImage(art.image_1.file.name, art.image_2.file.name, save_path)
            return redirect('/')
        # TODO
        # Run Function for AI
    else: 
        form = ArtForm()

    return render(request, 'artgen/art_edit.html', {'form': form})


def art_edit(request, pk):
    art = get_object_or_404(Art, pk=pk)
    if request.method == "POST":
        form = ArtForm(request.POST, instance=art)
        if form.is_valid():
            art = form.save(commit=False)
            art.creator = request.user
            art.date_created = timezone.now()
            art.save()
            return redirect('art', pk=art.pk)
        # TODO 
        # Run Function for AI
    else:
        form = ArtForm(instance=art)
    return render(request, 'artgen/art_edit.html', {'form': form})

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
