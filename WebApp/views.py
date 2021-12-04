from django.db.models import Q
from django.db.models.aggregates import Sum 
from django.shortcuts import render
from WebApp.models import PdDrugs, PdPrescriber, PdPrescriberDrugs, PdSpecialty, PdStatedata
import re

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
    p_query = "select * from pd_prescriber_drugs pd inner join pd_prescriber p on pd.pdprescriber_id = p.npi inner join pd_drugs d on pd.pddrugs_id = d.drugid where d.drugid = "
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

    if name_contains != '' :
        data = data.filter( Q(fname__icontains=name_contains) | Q(lname__icontains=name_contains))
    
    if gender != 'Select' :
        data = data.filter(gender=gender)

    if state != '' :
        data = data.filter(state__state__icontains=state)

    if credentials != '' :
        data = data.filter(credentials__icontains=credentials)

    if specialty != '' :
        data = data.filter(specialties__title__icontains=specialty)

    if opioid_level != 'Select' :

        ## FIX ME

        list_to_include = []

        for prescriber in data :
            query = "select pd.id, drugname, qty, isopioid from pd_prescriber p inner join pd_prescriber_drugs pd on p.npi = pd.pdprescriber_id inner join pd_drugs d on d.drugid = pd.pddrugs_id where npi = "
            query += str(prescriber.npi)
            prescriptions_raw = PdPrescriberDrugs.objects.raw(query)
            
            total_prescriptions = 0
            total_opioids = 0

            for obj in prescriptions_raw:
                total_prescriptions += obj.qty

            for obj in prescriptions_raw:
                if obj.isopioid == 'TRUE' :
                    total_opioids += obj.qty

            opioid_percent = round((total_opioids / total_prescriptions) * 100)

            if opioid_level == 'None' and opioid_percent == 0:
                list_to_include.append(prescriber.npi)

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

    # DYNAMIC DATA (Total Prescriptions, Total Opioid Prescriptions, Percent Opioid Prescriptions)

    prescriptions_raw = PdPrescriberDrugs.objects.raw("select pd.id, drugname, qty, isopioid from pd_prescriber p inner join pd_prescriber_drugs pd on p.npi = pd.pdprescriber_id inner join pd_drugs d on d.drugid = pd.pddrugs_id where npi = " + prescriber_id)
    total_prescriptions = 0
    total_opioids = 0

    for obj in prescriptions_raw:
        total_prescriptions += obj.qty

    for obj in prescriptions_raw:
        if obj.isopioid == 'TRUE' :
            total_opioids += obj.qty

    opioid_percent = round((total_opioids / total_prescriptions) * 100)

    context = {
        "drugs" : drug_data,
        "prescriber" : prescriber_data,
        "total_prescriptions" : total_prescriptions,
        "total_opioids" : total_opioids,
        "opioid_percent" : opioid_percent,
        "prescriptions" : prescriptions_raw
    }

    return render(request, 'webapp/prescriberdetail.html', context)

def addPrescriberPageView(request):
    prescribers = PdPrescriber.objects.all()
    context = {
        "prescribers": prescribers,
    }

    return render(request, 'webapp/addprescriber.html', context)

def storePrescriberPageView(request):
    states = PdStatedata.objects.all()
    specialties = PdSpecialty.objects.all()

    #Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new employee object from the model (like a new record)
        new_prescriber = PdPrescriber()
        
        #Store the data from the form to the new object's attributes (like columns)
        new_prescriber.fname = request.POST.get('fname')                   
        new_prescriber.lname = request.POST.get('lname')  
        gender = request.POST.get('gender_select')            
        if gender == 'Female' :
            new_prescriber.gender = 'F'
        elif gender == 'Male' :
            new_prescriber.gender = 'M'
        else :
            new_prescriber.gender = 'O'                 
        state_input = request.POST.get('state') 
        for state in states :
            if state.state == state_input :
                new_prescriber.state = state.stateabbrev
        new_prescriber.credentials = request.POST.get('credentials')
            
        new_prescriber.save()
        specialty_input = request.POST.get('specialty_select')
        for specialty in specialties :
            if specialty.title == specialty_input :
                new_prescriber.specialties.add(specialty)
        
        #Get all of the State objects (record or records) for the current employee state
        new_state = State.objects.get(state_abbrev = request.POST.get('emp_state'))
        
        #Create a new Contact Information object (record)
        new_contact = Contact_Information()
        
        #Store the data from the form to the contact phone attribute (column) 
        new_contact.contact_phone = request.POST.get('contact_info')
        
        #Save the contact information record which will generate the autoincremented id
        new_contact.save()
        
        #Store the newly created contact information id (object or record reference) to the employee record
        new_prescriber.contact_information = new_contact
        
        #Store the State reference found to the employee state
        new_prescriber.emp_state = new_state
        
        #Save the employee record
        new_prescriber.save()
        
    #Make a list of all of the employee records and store it to the variable
    data = Employee.objects.all()
    
    #Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "our_emps" : data
    }
    return render(request, 'homepages/displayEmps.html', context)  

def aboutPageView(request) :
    return render(request, 'webapp/about.html')

def contactPageView(request) :
    return render(request, 'webapp/contact.html')