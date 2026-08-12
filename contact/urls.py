from django.urls import path
from . import views

urlpatterns = [
    path("submit-commission/", views.submit_commission, name="submit_commission"),
]