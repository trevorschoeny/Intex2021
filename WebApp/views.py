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

def prescriberDetailPageView(request) :
    return render(request, 'webapp/prescriberdetail.html')

def aboutPageView(request) :
    return render(request, 'webapp/about.html')

def contactPageView(request) :
    return render(request, 'webapp/contact.html')