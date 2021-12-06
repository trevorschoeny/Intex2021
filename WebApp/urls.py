from django.urls import path
from .views import addPrescriberDrugPageView, addPrescriberSpecialtyPageView, deletePrescriberPageView, indexPageView, prescribersPageView, drugsPageView, prescriberDetailPageView, aboutPageView, removePrescriberDrugPageView, removePrescriberSpecialty, updateAndStorePrescriberPageView, updatePrescriberPageView
from .views import contactPageView, drugDetailPageView, drugSearchPageView, prescriberSearchPageView
from .views import addPrescriberPageView, storePrescriberPageView, indexSearchPageView, loadRecDrugsView, loadRecDocView

urlpatterns = [
    path("drugs/", drugsPageView, name="drugs"),
    path("drug/<drug_id>", drugDetailPageView, name="drugdetail"),
    path("drugsearch/", drugSearchPageView, name="drugsearch"),
    path("prescribers/", prescribersPageView, name="prescribers"),
    path("prescribersearch/", prescriberSearchPageView, name="prescribersearch"),
    path("prescriber/<prescriber_id>/", prescriberDetailPageView, name="prescriberdetail"),
    path("about/", aboutPageView, name="about"),
    path("contact/", contactPageView, name="contact"),
    path("addprescriber/", addPrescriberPageView, name="addprescriber"),   
    path("storeprescriber/", storePrescriberPageView, name="storeprescriber"),
    path("statesearch/", indexSearchPageView, name="statesearch"),
    path("updateprescriber/<prescriber_id>", updatePrescriberPageView, name="updateprescriber"),
    path("updateandstoreprescriber/<prescriber_id>", updateAndStorePrescriberPageView, name="updateandstoreprescriber"),
    path("addprescriberspecialty/<prescriber_id>/<is_new>", addPrescriberSpecialtyPageView, name="addprescriberspecialty"),
    path("addprescriberdrug/<prescriber_id>/<is_new>", addPrescriberDrugPageView, name="addprescriberdrug"),
    path("deleteprescriber/<prescriber_id>", deletePrescriberPageView, name="deleteprescriber"),
    path("removeprescriberdrug/<prescriber_id>/<drug_id>/<is_new>", removePrescriberDrugPageView, name="removeprescriberdrug"),
    path("removeprescriberspecialty/<prescriber_id>/<specialty>/<is_new>", removePrescriberSpecialty, name="removeprescriberspecialty"),
    path("loadRecDrugs/<prescriber_id>/<value>/", loadRecDrugsView, name="loadRecDrugs"),
    path("loadRecDoc/<drug_id>/<value>/", loadRecDocView, name="loadRecDoc"),
    path("", indexPageView, name="index")
]