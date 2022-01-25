from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("our_collection", views.our_collection, name="our_collection"),
    path("partner_with_us", views.partner_with_us, name="partner_with_us"),
    path("privacy_policy", views.privacy_policy, name="privacy_policy"),
]
