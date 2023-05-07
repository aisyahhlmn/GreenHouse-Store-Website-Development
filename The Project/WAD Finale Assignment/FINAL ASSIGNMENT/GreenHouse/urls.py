from django.urls import path
from .import views

urlpatterns = [
    path('registration', views.registration, name="registration"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    path('userprofile', views.userprofile, name="userprofile"),
    path('userprofile/deletedata/<str:Email_Id>',views.deletedata,name="deletedata"),
    path('userprofile/updatedata/<str:Email_Id>',views.updatedata,name="updatedata"),
    path('userprofile/updatedata/updates/<str:Email_Id>',views.updates,name="updates"),
]