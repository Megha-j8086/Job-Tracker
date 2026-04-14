from django.shortcuts import render,redirect
from jobsapp.models import Job
from userapp.models import User
# Create your views here.


def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')

    jobs = Job.objects.filter(user_id=request.session['user_id'])

    total = jobs.count()
    interviews = jobs.filter(status='Interview').count()
    rejected = jobs.filter(status='Rejected').count()
    offers = jobs.filter(status='Offer').count()

    return render(request, 'dashboard.html', {
        'jobs': jobs,
        'total': total,
        'interviews': interviews,
        'rejected': rejected,
        'offers': offers
    })
def my_applications(request):
    if 'user_id' not in request.session:
        return redirect('login')

    jobs = Job.objects.filter(user_id=request.session['user_id'])
    return render(request, 'my_applications.html', {'jobs': jobs})
def analytics(request):
    if 'user_id' not in request.session:
        return redirect('login')

    jobs = Job.objects.filter(user_id=request.session['user_id'])

    data = {
        'total': jobs.count(),
        'pending': jobs.filter(status='Pending').count(),
        'interview': jobs.filter(status='Interview').count(),
        'rejected': jobs.filter(status='Rejected').count(),
        'offer': jobs.filter(status='Offer').count(),
    }

    return render(request, 'analytics.html', data)

def profile(request):
    if 'user_id' not in request.session:
        return redirect('login')

    user = User.objects.get(id=request.session['user_id'])

    if request.method == "POST":
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')

        password = request.POST.get('password')
        if password:
            user.password = password

        user.save()

        request.session['username'] = user.username

        return redirect('dashboard')

    return render(request, 'profile.html', {'user': user})