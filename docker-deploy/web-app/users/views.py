from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, DriverRegisterForm, DriverUpdateForm

@login_required
def account(request):
    if request.user.profile.is_driver:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
            d_form = DriverUpdateForm(request.POST, instance=request.user.profile)
       
            if u_form.is_valid() and p_form.is_valid() and d_form.is_valid():
                u_form.save()
                p_form.save()
                d_form.save()
            
                messages.success(request, f'Your account has been updated!')
                return redirect('account')

        else:
                u_form = UserUpdateForm(instance=request.user)
                p_form = ProfileUpdateForm(instance=request.user.profile)
                d_form = DriverUpdateForm(instance=request.user.profile)
       
                context = {
                    'u_form': u_form,
                    'p_form': p_form,
                    'd_form': d_form,
                }
                return render(request, 'users/account.html', context)
    else:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
            
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                
                messages.success(request, f'Your account has been updated!')
                return redirect('account')

        else:
                u_form = UserUpdateForm(instance=request.user)
                p_form = ProfileUpdateForm(instance=request.user.profile)
                
                context = {
                    'u_form': u_form,
                    'p_form': p_form,
                 }
                return render(request, 'users/account.html', context)
            
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            
            messages.success(request, f'You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})


@login_required
def driver_register(request):
    if request.method == 'POST':
        driverform = DriverRegisterForm(request.POST, instance=request.user.profile)
        if driverform.is_valid:
            driverform.save()
           
            messages.success(request, f'You are registered as a driver!')
            return redirect('account')

    else:
        form = DriverRegisterForm(instance=request.user.profile)
        return render(request, 'users/driver_reg.html',{'form':form})
