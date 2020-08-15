from django.urls import path
from . import views
urlpatterns=[

    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.home,name='home'),
    path('authenticateuser',views.authenticate_user,name='authenticate_user'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('getstart',views.getstart,name='getstart'),
    path('index',views.index,name='index'),
    path('complete-profile',views.completeprofile,name='complete-profile'),
    path('selfhelp',views.selfhelp,name='self-help'),
    path('relativehelp',views.relativehelp,name='relative-help'),
    path('sendmessageforself',views.selfhelpmessage,name='self-help-message'),
    path('sendmessageforrelative',views.relativehelpmessage,name='relative-help-message'),
    path('viewhospitals',views.viewhospitals,name='viewhospitals'),
    path('backtodashboard',views.backtodashboard,name='index'),
    path('viewhistory',views.viewhistory,name='viewhistory')
]
