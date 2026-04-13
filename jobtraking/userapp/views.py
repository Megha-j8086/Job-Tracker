from django.shortcuts import render
from django.shortcuts import render
from .models import User
from django.shortcuts import redirect



# Create your views here.
def userHome(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email=email, password=password).first()

        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'loginError': 'Invalid credentials'})

    return render(request, 'login.html')