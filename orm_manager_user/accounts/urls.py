from django.urls import path
from . import views

urlpatterns = [
      path('register/user/',views.UserSignUpView.as_view(), name='user_signup'),
      path('register/staff/',views.StaffSignUpView.as_view(), name='staff_signup'),
      path('request/<str:pk>/',views.requestPermission, name='request'),
      path('request/accept/<str:pk>/',views.acceptPermission, name='accept'),
      path('request/deny/<str:pk>/',views.deniedPermission, name='deny'),
      path('login/',views.loginPage,name='login'),
      path('logout/',views.logoutUser,name='logout'),

      path('',views.home,name='home'),
      path('dashboard/',views.dashboard,name='dashboard'),  
      path('customer/<str:pk>/',views.customer,name='customer'),  
      path('create_order/',views.createOrder,name='create_order'),
      path('update_order/<str:pk>/',views.updateOrder,name='update_order'),
      path('delete_order/<str:pk>/',views.deleteOrder,name='delete_order'),
]


