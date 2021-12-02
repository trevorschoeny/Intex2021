from django.shortcuts import render
from WebApp.models import PdDrugs, PdPrescriber

# Create your views here.

def indexPageView(request) :
    return render(request, 'webapp/index.html')

def drugsPageView(request) :
    data = PdDrugs.objects.all()

    context = {
        "drugs" : data
    }

    return render(request, 'webapp/drugs.html', context)

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

def drugDetailPageView(request, drug_id) :
    drug_data = PdDrugs.objects.get(drugid = drug_id)
    p_query = "select * from pd_triple t inner join pd_prescriber p on t.prescriberid = p.npi inner join pd_drugs d on t.drugname = d.drugname where drugid = "
    p_query += drug_id
    p_query += "order by qty desc limit 10;"
    prescriber_data = PdPrescriber.objects.raw(p_query)



    context = {
        "drug" : drug_data,
        "prescribers" : prescriber_data
    }

    return render(request, 'webapp/drugdetail.html', context)

def prescribersPageView(request) :

    data = PdPrescriber.objects.raw("select * from pd_prescriber limit 201")

    context = {
        "prescribers" : data
    }

    return render(request, 'webapp/prescribers.html', context)

def prescriberSearchPageView(request) :
    return render(request, 'webapp/prescribers.html')

def prescriberDetailPageView(request) :
    return render(request, 'webapp/prescriberdetail.html')

def aboutPageView(request) :
    return render(request, 'webapp/about.html')

def contactPageView(request) :
    return render(request, 'webapp/contact.html')