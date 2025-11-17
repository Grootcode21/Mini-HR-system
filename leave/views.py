from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import LeaveRequest
from .forms import LeaveForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def dashboard(request):
    leaves = LeaveRequest.objects.filter(user=request.user)
    return render(request, 'leave/dashboard.html', {'leaves': leaves})

@login_required
def apply_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            return redirect('dashboard')
    else:
        form = LeaveForm()
    return render(request, 'leave/leave_form.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def leave_list(request):
    leaves = LeaveRequest.objects.all().order_by('-created_at')
    return render(request, 'leave/leave_list.html', {'leaves': leaves})

@user_passes_test(lambda u: u.is_staff)
def approve_leave(request, pk):
    leave = get_object_or_404(LeaveRequest, pk=pk)
    leave.status = 'Approved'
    leave.save()
    return redirect('leave_list')

@user_passes_test(lambda u: u.is_staff)
def reject_leave(request, pk):
    leave = get_object_or_404(LeaveRequest, pk=pk)
    leave.status = 'Rejected'
    leave.save()
    return redirect('leave_list')
