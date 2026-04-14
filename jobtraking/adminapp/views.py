from django.shortcuts import render,redirect
from userapp.models import User
from jobsapp.models import Job
# Create your views here.




def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "admin" and password == "1234":
            request.session['admin'] = True
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin/login.html', {'error': 'Invalid Admin Login'})

    return render(request, 'admin/login.html')

def admin_dashboard(request):
    if not request.session.get('admin'):
        return redirect('login')

    total_users = User.objects.count()
    total_jobs = Job.objects.count()

    return render(request, 'admin/admin-dashboard.html', {
        'users': total_users,
        'jobs': total_jobs
    })