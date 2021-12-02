from django.urls import path
from .views import indexPageView, prescribersPageView, drugsPageView, prescriberDetailPageView, aboutPageView, contactPageView, drugDetailPageView, drugSearchPageView

urlpatterns = [
    path("prescribers/", prescribersPageView, name="prescribers"),
    path("drugs/", drugsPageView, name="drugs"),
    path("drug/<drug_id>", drugDetailPageView, name="drugdetail"),
    path("drugsearch/", drugSearchPageView, name="drugsearch"),
    path("prescriber/", prescriberDetailPageView, name="prescriberdetail"),
    path("about/", aboutPageView, name="about"),
    path("contact/", contactPageView, name="contact"),
    path("", indexPageView, name="index")
]