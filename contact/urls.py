from django.urls import path
from .views import portfolio_home, contact_form

urlpatterns = [
    path('', portfolio_home, name='portfolio_home'),
    path('contact/', contact_form, name='contact_form'),
]
