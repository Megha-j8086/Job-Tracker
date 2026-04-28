from django.shortcuts import render,redirect
from userapp.models import User
from jobsapp.models import Job
from .models import Add_Job
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
        return redirect('admin_login')

    total_users = User.objects.count()
    total_jobs = Job.objects.count()

    return render(request, 'admin/admin-dashboard.html', {
        'users': total_users,
        'jobs': total_jobs
    })

def manage_users(request):
    if not request.session.get('admin'):
        return redirect('admin_login')

    users = User.objects.all()
    return render(request, 'admin/users.html', {'users': users})
def delete_user(request, id):
    if not request.session.get('admin'):
        return redirect('admin_login')

    user = User.objects.get(id=id)
    user.delete()
    return redirect('manage_users')

def manage_jobs(request):
    if not request.session.get('admin'):
        return redirect('admin_login')

    jobs = Job.objects.all()
    return render(request, 'admin/jobs.html', {'jobs': jobs})

def delete_job(request, id):
    if not request.session.get('admin'):
        return redirect('admin_login')

    job = Job.objects.get(id=id)
    job.delete()
    return redirect('manage_jobs')
def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')




def upload_job(request):
    if request.method == "POST":

        title = request.POST.get('title')
        company = request.POST.get('company')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')
        job_type = request.POST.get('job_type')
        skills = request.POST.get('skills')
        description = request.POST.get('description')

        if not title or not company:
            return render(request, 'admin/admin-job.html', {
                'error': 'Title and Company are required'
            })

        Add_Job.objects.create(
            title=title,
            company=company,
            salary=salary,
            experience=experience,
            job_type=job_type,
            skills=skills,
            description=description
        )

        return render(request, 'admin/admin-job.html', {
            'success': 'Job posted successfully!'
        })

    return render(request, 'admin/admin-job.html')