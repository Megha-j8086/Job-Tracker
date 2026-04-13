from django.shortcuts import render,redirect
from .models import Job
# Create your views here.


def add_job(request):
    if request.method == "POST":
        Job.objects.create(
            user_id=request.session.get('user_id'),
            company=request.POST.get('company'),
            role=request.POST.get('role'),
            experience=request.POST.get('experience')
        )
        return redirect('dashboard')

    return render(request, 'addjob.html')


def delete_job(request, id):
    Job.objects.filter(id=id).delete()
    return redirect('dashboard')