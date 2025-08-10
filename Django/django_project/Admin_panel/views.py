from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import UserProfile
# Create your views here.
def home(request):
    return render(request, "home.html")
def login(request):
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        print('data')
        form = UserRegistrationForm(request.POST)
        print(form.data, form.is_valid())
        if form.is_valid():
            firstname=form.data.get('firstname')
            username=form.data.get('username')
            password=form.data.get('password')
            date_of_birth=form.data.get('date_of_birth')
            contact_number=form.data.get('contact_number')
            print(firstname,username,password,date_of_birth,contact_number)

            user=User.objects.create_user(username=username, password=password, first_name=firstname)

            UserProfile.objects.create(user=user, date_of_birth=date_of_birth, contact_number=contact_number)
            user.save()

            return redirect("login")
        else:
            form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})