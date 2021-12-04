from django.urls import path
from .views import indexPageView, prescribersPageView, drugsPageView, prescriberDetailPageView, aboutPageView
from .views import contactPageView, drugDetailPageView, drugSearchPageView, prescriberSearchPageView

urlpatterns = [
    path("drugs/", drugsPageView, name="drugs"),
    path("drug/<drug_id>", drugDetailPageView, name="drugdetail"),
    path("drugsearch/", drugSearchPageView, name="drugsearch"),
    path("prescribers/", prescribersPageView, name="prescribers"),
    path("prescribersearch/", prescriberSearchPageView, name="prescribersearch"),
    path("prescriber/<prescriber_id>", prescriberDetailPageView, name="prescriberdetail"),
    path("about/", aboutPageView, name="about"),
    path("contact/", contactPageView, name="contact"),
    path("", indexPageView, name="index")
]