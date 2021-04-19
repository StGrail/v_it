"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path, include

from api.routers import router
from users import views as user_views
from users.views import JoinForm, EditProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_pages.urls')),
    path('join/', JoinForm.as_view(template_name='web_pages/join.html'), name='join'),
    path('edit_profile/',
         login_required(EditProfile.as_view(template_name='web_pages/edit_profile.html')),
         name='edit_profile'),
    path('login/',
         auth_views.LoginView.as_view(template_name='web_pages/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='web_pages/logout.html'),
         name='logout'),
    path('password-reset',
         auth_views.PasswordResetView.as_view(template_name='web_pages/password_reset.html'),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='web_pages/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='web_pages/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='web_pages/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', user_views.profile, name='profile'),
    path('rate_vacancy/', user_views.rate_vacancy, name='rate_vacancy'),
]

urlpatterns += router.urls
