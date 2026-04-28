from django.shortcuts import render, redirect
from .models import Job


def add_job(request):
    if not request.session.get('user_id'):
        return redirect('login')

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
    if request.session.get('user_id'):
        Job.objects.filter(id=id).delete()
    return redirect('dashboard')


# ✅ JOB LIST WITH SEARCH (IMPORTANT)
def jobs_list(request):
    query = request.GET.get('q', '').strip()

    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(
            role__icontains=query
        ) | jobs.filter(
            company__icontains=query
        ) | jobs.filter(
            status__icontains=query
        )

    jobs = jobs.distinct()

    return render(request, 'jobs.html', {
        'jobs': jobs,
        'query': query
    })


def applications(request):
    if not request.session.get('user_id'):
        return redirect('login')

    jobs = Job.objects.filter(user_id=request.session.get('user_id'))

    return render(request, 'application.html', {'jobs': jobs})


def apply_job(request, id):
    if not request.session.get('user_id'):
        return redirect('login')

    job = Job.objects.filter(id=id).first()

    if job:
        job.status = "Applied"
        job.user_id = request.session.get('user_id')
        job.save()

    return redirect('applications')


def delete_application(request, id):
    if not request.session.get('user_id'):
        return redirect('login')

    job = Job.objects.filter(
        id=id,
        user_id=request.session.get('user_id')
    ).first()

    if job:
        job.delete()

    return redirect('applications')