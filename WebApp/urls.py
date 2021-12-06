from django.urls import path
from .views import indexPageView, indexSearchPageView, prescribersPageView, drugsPageView, prescriberDetailPageView, aboutPageView
from .views import contactPageView, drugDetailPageView, drugSearchPageView, prescriberSearchPageView
from .views import addPrescriberPageView, storePrescriberPageView

urlpatterns = [
    path("drugs/", drugsPageView, name="drugs"),
    path("drug/<drug_id>", drugDetailPageView, name="drugdetail"),
    path("drugsearch/", drugSearchPageView, name="drugsearch"),
    path("prescribers/", prescribersPageView, name="prescribers"),
    path("prescribersearch/", prescriberSearchPageView, name="prescribersearch"),
    path("prescriber/<prescriber_id>", prescriberDetailPageView, name="prescriberdetail"),
    path("about/", aboutPageView, name="about"),
    path("contact/", contactPageView, name="contact"),
    path("addprescriber/", addPrescriberPageView, name="addprescriber"),   
    path("storeprescriber/", storePrescriberPageView, name="storeprescriber"),
    path("statesearch/", indexSearchPageView, name="statesearch"),
    path("", indexPageView, name="index")
]