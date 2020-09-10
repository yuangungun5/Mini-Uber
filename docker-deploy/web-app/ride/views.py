from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Ride, ShareOrder
from .forms import DriverSearchForm, SharerSearchForm, ShareCreateForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from project1.settings import EMAIL_HOST_USER
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone


def home(request):
    context = {
        'rides': Ride.objects.all(order_status='OP')
    }
    return render(request, 'ride/home.html', context)

def index(request):
    return render(request, 'ride/index.html')

class RideListView(ListView):
    model = Ride
    template_name = 'ride/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rides'
    ordering = ['-date_arrival']
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return Ride.objects.filter(Q(order_status='OP')|Q(order_status='PD')).order_by('-date_arrival')

class UserRideListView(ListView):
    model = Ride
    template_name = 'ride/user_rides.html'
    context_object_name = 'rides'
    ordering = ['-date_arrival']
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return Ride.objects.filter(Q(owner=user)|(Q(sharer=user)&Q(share_flag=True))).order_by('-date_arrival')

class DriverRideListView(ListView):
    model = Ride
    template_name = 'ride/user_drives.html'
    context_object_name = 'rides'
    ordering = ['-date_arrival']
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return Ride.objects.filter(Q(driver=user)).order_by('-date_arrival')

class DSListView(ListView):
    model = Ride
    template_name = 'ride/driver_search_results.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rides'
    ordering = ['-date_arrival']
    paginate_by = 5


class SSListView(ListView):
    model = Ride
    template_name = 'ride/sharer_search_results.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rides'
    ordering = ['-date_arrival']
    paginate_by = 5

def driver_search(request):
    if request.method == 'POST':
        form = DriverSearchForm(request.POST)
        if form.is_valid():
            after = form.cleaned_data['arrival_after']
            before = form.cleaned_data['arrival_before']
            driver = request.user

            context = {
                'rides': Ride.objects.all().filter(Q(order_status='OP')|Q(order_status='PD')
                ).filter(passenger_num__lte=driver.profile.max_passenger
                ).filter(date_arrival__gte=after
                ).filter(date_arrival__lte=before)
   
            }
            return render(request, 'ride/driver_search_results.html',context)
    else:
        form = DriverSearchForm()
        return render(request, 'ride/search.html', {'form':form})
    
def share(request):
    if request.method == 'POST':
        form = SharerSearchForm(request.POST)
        if form.is_valid():
            dest = form.cleaned_data['destination']
            num = form.cleaned_data['passenger_num']
            after = form.cleaned_data['arrival_after']
            before = form.cleaned_data['arrival_before']
            context = {
                'rides': Ride.objects.all().filter(order_status='OP'
                ).filter(is_shared=True
                ).filter(destination=dest
                ).filter(date_arrival__gte=after
                ).filter(date_arrival__lte=before)
            }
            return render(request, 'ride/sharer_search_results.html',context)
    else:
        form = SharerSearchForm()
        return render(request, 'ride/share.html', {'form':form})


def join_ride(request, pk):
    if request.method == 'POST':
        form = ShareCreateForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['passenger_num']
            ride = get_object_or_404(Ride, pk=pk)
            #print(ride.owner.id)
            #print(request.user.id)
 
            if ride.order_status == 'OP':
                if ride.owner.id != request.user.id:
                    #print('confirm')
                    ride.order_status = 'PD'
                    ride.share_passenger_num = num
                    ride.sharer = request.user
                    ride.share_flag = True
                    ride.save()

                    order = ShareOrder(ride=ride, sharer=request.user, passenger_num=num)
                    order.save()

                    subject = 'Someone joins your ride!'
                    body = 'Your ride is now pending!'
                    send_mail(subject, body, EMAIL_HOST_USER, [ride.owner.email])

                    messages.success(request,f'You have joined the ride!')
                    
                    return HttpResponseRedirect(reverse('ride-sharer-detail', kwargs={'pk': ride.pk}))
                else:
                    messages.warning(request,f'You cannot join your own ride!')
                    return redirect('sharer-search')
    else:
        form = ShareCreateForm()
        return render(request,'ride/join_confirm.html', {'form':form})


def quit_ride(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    print(ride.id)
    order = get_object_or_404(ShareOrder, ride=ride)
    print(order.id)
    if ride.order_status == 'PD':
        ride.order_status = 'OP'
        ride.share_passenger_num = 0
        ride.share_flag = False
        ride.save()

        return HttpResponse('You are now quit the ride-sharing!')


    
class RideDetailView(DetailView):
    model = Ride


class DRDetailView(DetailView):
    model = Ride
    template_name = 'ride/rd_detail.html'


class SRDetailView(DetailView):
    model = Ride
    template_name = 'ride/rs_detail.html'


class RideCreateView(LoginRequiredMixin, CreateView):
    model = Ride
    fields = ['start', 'destination', 'date_arrival', 'passenger_num',
              'capacity_level', 'is_shared', 'note']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class RideUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ride
    fields = ['start', 'destination', 'date_arrival', 'passenger_num',
              'capacity_level', 'is_shared', 'note']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ride = self.get_object()
        if self.request.user == ride.owner:
            return True
        return False


class RideDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ride
    success_url = '/'

    def test_func(self):
        ride = self.get_object()
        if self.request.user == ride.owner:
            return True
        return False


def complete(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    if ride.order_status == 'ON':
        ride.order_status = 'CP'
        ride.date_arrival = timezone.now()
        ride.save()
    return HttpResponse('The ride completes!')

def close(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    if ride.order_status == 'ON':
        ride.order_status = 'CL'
        ride.save()
    return HttpResponse('The order is closed!')

def confirm(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    if ride.order_status == 'OP' or ride.order_status == 'PD':
        if ride.owner.id != request.user.id:
            if (ride.share_flag) and (ride.sharer.id != request.user.id):
                prev_status = ride.order_status
                ride.order_status = 'ON'
                ride.driver = request.user
                ride.save()

                subject = 'Your ride is now ongoing!'
                body = 'Your ride with RideShare has been confirmed.'
                if prev_status == 'OP':  # no sharer
                    send_mail(subject, body, EMAIL_HOST_USER, [ride.owner.email], fail_silently=False)
                else:
                    send_mail(subject, body, EMAIL_HOST_USER, [ride.owner.email, ride.sharer.email], fail_silently=False)
                return HttpResponse('Confirmed message has been sent to passengers :)')
            else:
                 messages.warning(request,f'You cannot drive your own ride!')
                 return redirect('driver-search')

        else:
            messages.warning(request,f'You cannot drive your own ride!')
            return redirect('driver-search')
