from django.urls import path
from .views import login, ClientAccess, AdminAccess, register

urlpatterns = [
    path('login/', login, name='login'),
    path('client-access/', ClientAccess.as_view(), name='client-access'),
    path('admin-access/', AdminAccess.as_view(), name='admin-access'),
    path('register/', register, name='register'),

]
