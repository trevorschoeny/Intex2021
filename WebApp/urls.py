from django.urls import path
from .views import addPrescriberDrugPageView, addPrescriberSpecialtyPageView, indexPageView, prescribersPageView, drugsPageView, prescriberDetailPageView, aboutPageView, updateAndStorePrescriberPageView, updatePrescriberPageView
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
    path("updateprescriber/<prescriber_id>", updatePrescriberPageView, name="updateprescriber"),
    path("updateandstoreprescriber/<prescriber_id>", updateAndStorePrescriberPageView, name="updateandstoreprescriber"),
    path("addprescriberspecialty/<prescriber_id>", addPrescriberSpecialtyPageView, name="addprescriberspecialty"),
    path("addprescriberdrug/<prescriber_id>", addPrescriberDrugPageView, name="addprescriberdrug"),
    path("", indexPageView, name="index")
]