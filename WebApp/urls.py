from django.urls import path
from .views import indexPageView, prescribersPageView, drugsPageView, prescriberDetailPageView

urlpatterns = [
    path("prescribers/", prescribersPageView, name="prescribers"),
    path("drugs/", drugsPageView, name="drugs"),
    path("prescriber/", prescriberDetailPageView, name="prescriberdetail"),
    path("", indexPageView, name="index")
]