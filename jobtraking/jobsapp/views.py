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

def jobs_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})


def applications(request):
    if not request.session.get('user_id'):
        return redirect('login')

    jobs = Job.objects.filter(user_id=request.session.get('user_id'))
    return render(request, 'application.html', {'jobs': jobs})
def apply_job(request, id):
    if not request.session.get('user_id'):
        return redirect('login')

    job = Job.objects.filter(id=id).first()

    if not job:
        return redirect('jobs')

    job.status = "Applied"
    job.user_id = request.session.get('user_id')
    job.save()

    return redirect('applications')

def delete_application(request, id):
    if not request.session.get('user_id'):
        return redirect('login')

    job = Job.objects.filter(id=id, user_id=request.session.get('user_id')).first()

    if job:
        job.delete()   # removes application

    return redirect('applications')