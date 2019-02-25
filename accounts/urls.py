from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^register/', views.RegistrationView.as_view(), name='register'),
    url(r'^login/', views.user_login, name='user_login')
]
