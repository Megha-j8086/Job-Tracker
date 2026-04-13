from django.shortcuts import render,redirect
from jobsapp.models import Job
# Create your views here.



def dashboard(request):
    if not request.session.get('user_id'):
        return redirect('login')

    user_id = request.session.get('user_id')
    jobs = Job.objects.filter(user_id=user_id)

    return render(request, 'dashboard.html', {
        'jobs': jobs
    })