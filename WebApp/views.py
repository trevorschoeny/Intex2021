from django.db.models import Q 
from django.shortcuts import render
from WebApp.models import PdDrugs, PdPrescriber, PdStatedata

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
    state_data = PdStatedata.objects.all()

    context = {
        "prescribers" : data,
        "states" : state_data
    }

    return render(request, 'webapp/prescribers.html', context)

def prescriberSearchPageView(request) :

    data = PdPrescriber.objects.all()
    state_data = PdStatedata.objects.all()

    name_contains = request.GET.get('name_contains')
    gender = request.GET.get('gender_select')
    state = request.GET.get('state_select')
    credential = request.GET.get('credential_select')
    specialty = request.GET.get('specialty_select')
    opioid_level = request.GET.get('opioid_level_select')
    is_licensed = request.GET.get('licensed_check')

    if name_contains != '' :
        data = data.filter( Q(fname__icontains=name_contains) | Q(lname__icontains=name_contains))
    
    if gender != 'Select' :
        data = data.filter(gender=gender)

    if state != '' :
        data = data.filter(state=state)

    if credential != '' :
        data = data.filter(credential=credential)

    if specialty != '' :
        data = data.filter(specialty=specialty)

    if opioid_level != 'Select' :
        data = data.filter(opioidlevel=opioid_level)

    if is_licensed != '' :
        data = data.filter(isopioidprescriber=is_licensed)
    

    context = {
        "prescribers" : data,
        "states" : state_data,
    }

    return render(request, 'webapp/prescribers.html', context)

def prescriberDetailPageView(request) :
    return render(request, 'webapp/prescriberdetail.html')

def aboutPageView(request) :
    return render(request, 'webapp/about.html')

def contactPageView(request) :
    return render(request, 'webapp/contact.html')