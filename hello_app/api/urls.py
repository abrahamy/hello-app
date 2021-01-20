from django.urls import path

from hello_app.api import views

urlpatterns = [
    path("address/", views.AddressEndpoint.as_view(), name="address"),
]