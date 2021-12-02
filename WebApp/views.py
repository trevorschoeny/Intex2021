from django.shortcuts import render
from WebApp.models import PdDrugs

# Create your views here.

def indexPageView(request) :
    return render(request, 'webapp/index.html')

def prescribersPageView(request) :
    return render(request, 'webapp/prescribers.html')

def drugsPageView(request) :
    data = PdDrugs.objects.all()

    context = {
        "drugs" : data
    }

    return render(request, 'webapp/drugs.html', context)

def drugDetailPageView(request, drug_id) :
    data = PdDrugs.objects.get(drugid = drug_id)

    context = {
        "drug" : data
    }

    return render(request, 'webapp/drugdetail.html', context)

def drugSearchPageView(request) :

    data = PdDrugs.objects.all()
    name_contains = request.GET.get('name_contains')
    is_opioid = request.GET.get('isopioid')

    if name_contains != '' :
        data = data.filter(drugname__icontains=name_contains)

    if is_opioid :
        data = data.filter(isopioid=True)

    context = {
        "drugs" : data
    }

    return render(request, 'webapp/drugs.html', context)

def prescriberDetailPageView(request) :
    return render(request, 'webapp/prescriberdetail.html')

def aboutPageView(request) :
    return render(request, 'webapp/about.html')

def contactPageView(request) :
    return render(request, 'webapp/contact.html')