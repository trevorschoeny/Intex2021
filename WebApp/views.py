from django.db.models import Q 
from django.shortcuts import render
from WebApp.models import PdDrugs, PdPrescriber, PdSpecialty, PdStatedata

# Create your views here.

def indexPageView(request) :
    return render(request, 'webapp/index.html')

def drugsPageView(request) :
    data = PdDrugs.objects.all()

    result_count = data.count()

    context = {
        "drugs" : data,
        "result_count" : result_count
    }

    return render(request, 'webapp/drugs.html', context)

def drugSearchPageView(request) :

    data = PdDrugs.objects.all()
    name_contains = request.GET.get('name_contains')
    is_opioid = request.GET.get('isopioid')

    if name_contains != '' :
        data = data.filter(drugname__icontains=name_contains)

    if is_opioid :
        data = data.filter(isopioid="TRUE")

    result_count = data.count()

    context = {
        "drugs" : data,
        "result_count" : result_count
    }

    return render(request, 'webapp/drugs.html', context)

def drugDetailPageView(request, drug_id) :
    drug_data = PdDrugs.objects.get(drugid = drug_id)
    p_query = "select * from pd_triplenew t inner join pd_prescriber p on t.prescriberid = p.npi inner join pd_drugs d on t.drugname = d.drugname where drugid = "
    p_query += drug_id
    p_query += "order by qty desc limit 10;"
    prescriber_data = PdPrescriber.objects.raw(p_query)

    context = {
        "drug" : drug_data,
        "prescribers" : prescriber_data
    }

    return render(request, 'webapp/drugdetail.html', context)

def prescribersPageView(request) :

    data = PdPrescriber.objects.all()[0:100]
    specialty_data = PdSpecialty.objects.all()
    state_data = PdStatedata.objects.all()

    result_count = data.count()
    result_count = str(result_count) + '+'

    context = {
        "prescribers" : data,
        "states" : state_data,
        "result_count" : result_count,
        "specialties" : specialty_data
    }

    return render(request, 'webapp/prescribers.html', context)

def prescriberSearchPageView(request) :

    data = PdPrescriber.objects.all()
    specialty_data = PdSpecialty.objects.all()
    state_data = PdStatedata.objects.all()

    name_contains = request.GET.get('name_contains')
    gender = request.GET.get('gender_select')
    state = request.GET.get('state_select')
    credentials = request.GET.get('credentials_contains')
    specialty = request.GET.get('specialty_select')
    opioid_level = request.GET.get('opioid_level_select')
    is_licensed = request.GET.get('licensed_check')

    for state_i in state_data :
        if state_i.state == state :
            state = state_i.stateabbrev

    if name_contains != '' :
        data = data.filter( Q(fname__icontains=name_contains) | Q(lname__icontains=name_contains))
    
    if gender != 'Select' :
        data = data.filter(gender=gender)

    if state != '' :
        data = data.filter(state__icontains=state)

    if credentials != '' :
        data = data.filter(credentials__icontains=credentials)

    if specialty != '' :
        data_s = data
        data_s = data_s.raw("select * from pd_specialty")

    if opioid_level != 'Select' :
        data = data.filter(opioidlevel=opioid_level)

    if is_licensed :
        data = data.filter(isopioidprescriber=is_licensed)

    result_count = data.count()
    
    if (name_contains == '') and (gender == 'Select') and (state == '') and (credentials == '') and (specialty == '') and (opioid_level == 'Select') and (is_licensed == False) :
        data = data[0:100]
        result_count = data.count()
        result_count = str(result_count) + '+'

    context = {
        "prescribers" : data,
        "states" : state_data,
        "result_count" : result_count,
        "specialties" : specialty_data
    }

    return render(request, 'webapp/prescribers.html', context)

def prescriberDetailPageView(request, prescriber_id) :

    prescriber_data = PdPrescriber.objects.get(npi = prescriber_id)
    drug_data = PdDrugs.objects.all()

    context = {
        "drugs" : drug_data,
        "prescriber" : prescriber_data
    }

    print(prescriber_data.fname)

    return render(request, 'webapp/prescriberdetail.html', context)

def aboutPageView(request) :
    return render(request, 'webapp/about.html')

def contactPageView(request) :
    return render(request, 'webapp/contact.html')