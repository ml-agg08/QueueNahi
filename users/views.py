from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import UserProfile
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

class RoleBasedLoginView(LoginView):
    def get_success_url(self):
        profile = self.request.user.userprofile
        if profile.role == 'student':
            return '/student/dashboard/'
        else:
            return '/chef/chefdashboard/'

def register(request):
    if request.method == 'POST':
        print("helloo")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']

            # ✅ Prevent UNIQUE constraint error
            UserProfile.objects.get_or_create(user=user, defaults={'role': role})

            login(request, user)
            if role == 'student':
                return redirect('student_dashboard')
            else:
                return redirect('chef_dashboard_2')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
def chef_dashboard(request):
    return render(request, 'test.html')

def logoutpage(request):
    logout(request)  # Django built-in logout
    return redirect('login')  # Redirect to login page after logout