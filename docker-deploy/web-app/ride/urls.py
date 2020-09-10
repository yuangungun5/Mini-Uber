from django.urls import path
from .views import (
    RideListView,
    RideDetailView,
    RideCreateView,
    RideUpdateView,
    RideDeleteView,
    UserRideListView,
    DriverRideListView,
    DSListView,
    SSListView,
    DRDetailView,
    SRDetailView,
)
from . import views

urlpatterns = [
    path('ride/home/', RideListView.as_view(), name='ride-home'),
    path('ride/myride/', UserRideListView.as_view(), name='myride'),
    path('ride/mydrive/', DriverRideListView.as_view(), name='mydrive'),
    path('ride/driver_search_results/', DSListView.as_view(), name='driver-search'),
    path('ride/sharer_search_results/', SSListView.as_view(), name='sharer-search'),
    path('ride/<int:pk>/', RideDetailView.as_view(), name='ride-detail'),
    path('ride/driver/<int:pk>/', DRDetailView.as_view(), name='ride-driver-detail'),
    path('ride/sharer/<int:pk>/', SRDetailView.as_view(), name='ride-sharer-detail'),
    path('ride/new/', RideCreateView.as_view(), name='ride-create'),
    path('ride/<int:pk>/update/', RideUpdateView.as_view(), name='ride-update'),
    path('ride/<int:pk>/delete/', RideDeleteView.as_view(), name='ride-delete'),
    path('ride/<int:pk>/complete/', views.complete, name='ride-complete'),
    path('ride/<int:pk>/close/', views.close, name='ride-close'),
    path('ride/<int:pk>/quit/', views.quit_ride, name='ride-quit'),
    path('ride/share/', views.share, name='ride-share'),
    path('ride/search/', views.driver_search, name='search'),
    path('ride/<int:pk>/confirm', views.confirm, name='confirm'),
    path('ride/<int:pk>/join', views.join_ride, name='join'),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
]
