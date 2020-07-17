from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .forms import RegisterForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtForm
from .forms import CustomUserCreationForm

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


def art_new(request):
    if request.method == "POST":
        form = ArtForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.creator = request.user
            art.date_created = timezone.now()
            art.save()
            return redirect('art', pk=art.pk)
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
    else:
        form = ArtForm(instance=art)
    return render(request, 'artgen/art_edit.html', {'form': form})


# # Create your views here.
# def register(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()

#         return redirect("/")
#     else:
#         form = RegisterForm()

#         return render(response, "artgen/register.html", {"form": form})


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}")
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request,
#                   template_name="main/login.html",
#                   context={"form": form})

# def logout(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("/")


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
