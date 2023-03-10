"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('compreg/',regis),

    path('sendmail/', send_mail_regis),
    path('success/', success),
    path('verify/<auth_token>', verify),
    path('error/',error),

    path('login/',login),

    path('disp/',prodisp),
    path('indexjob/',indexjob),

    path('postjob/',postjobdef),
    path('jobsu/',jobsuces),
    path('table/',table),

    path('sendmaildef<int:id>',sendmaildef),
    path('sendit/<int:id>',sendit),

    path('employeeregis/',empregis),
    path('employeelogin/',emplogin),

    path('viewjob/<int:id>',viewjob),
    path('viewmore/<int:id>/<int:pk>',viewmore),
    path('applynow/<int:id>/<int:pk>',applynow),


    path('editprofile<int:id>',editprof),
    path('updateprof<int:id>',updateprof)

]