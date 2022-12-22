from django.urls import path

from . import views

urlpatterns = [
    path('', views.getallservicesview.as_view(),name='services'),
    path('<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('create/', views.ServiceCreateView.as_view(), name='services_create'),

    path('showServicePerApi', views.getallservicesviewstep2.as_view(),name='showServicePerApi'),
    
    path('cardetails/', views.cardetails,name='cardetails'),

    # path('sendapi/', views.sendapi),

    # path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('create/', views.PostCreateView.as_view(), name='post_create'),
    # path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    # path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]