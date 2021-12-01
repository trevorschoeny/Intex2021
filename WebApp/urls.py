from django.urls import path
from .views import indexPageView, prescribersPageView, drugsPageView, prescriberDetailPageView, aboutPageView, contactPageView

urlpatterns = [
    path("prescribers/", prescribersPageView, name="prescribers"),
    path("drugs/", drugsPageView, name="drugs"),
    path("prescriber/", prescriberDetailPageView, name="prescriberdetail"),
    path("about/", aboutPageView, name="about"),
    path("contact/", contactPageView, name="contact"),
    path("", indexPageView, name="index")
]