from django.db.models import Q
from django.db.models.aggregates import Sum 
from django.shortcuts import render
from WebApp.models import PdDrugs, PdPrescriber, PdPrescriberDrugs, PdSpecialty, PdStatedata
import re

import pip._vendor.requests
import json

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
    data_raw = PdPrescriber.objects.raw('''select *, (select sum(pd.qty)
                                                from pd_prescriber p
                                                    inner join pd_prescriber_drugs pd on p.npi = pd.pdprescriber_id
                                                    inner join pd_drugs d on d.drugid = pd.pddrugs_id
                                                where d.isopioid = 'TRUE'
                                                    and pd.pdprescriber_id = p1.npi) / (select sum(pd.qty)
                                                from pd_prescriber p
                                                    inner join pd_prescriber_drugs pd on p.npi = pd.pdprescriber_id
                                                    inner join pd_drugs d on d.drugid = pd.pddrugs_id
                                                    and pd.pdprescriber_id = p1.npi) as opioidpercent, (select sum(pd.qty)
                                                from pd_prescriber p
                                                    inner join pd_prescriber_drugs pd on p.npi = pd.pdprescriber_id
                                                    inner join pd_drugs d on d.drugid = pd.pddrugs_id
                                                    and pd.pdprescriber_id = p1.npi) as dynamictotalprescriptions
                                            from pd_prescriber p1''')
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
        # data_raw = data_raw.raw("select * from data_raw")
    
    if gender != 'Select' :
        data = data.filter(gender=gender)

    if state != '' :
        data = data.filter(state__state__icontains=state)

    if credentials != '' :
        data = data.filter(credentials__icontains=credentials)

    if specialty != '' :
        data = data.filter(specialties__title__icontains=specialty)

    if opioid_level != 'Select' :
        pass

    if is_licensed :
        data = data.filter(isopioidprescriber=is_licensed)

    result_count = data.count()
    
    if (name_contains == '') and (gender == 'Select') and (state == '') and (credentials == '') and (specialty == '') and (opioid_level == 'Select') and (is_licensed == False) :
        data = data[0:100]
        result_count = data.count()
        result_count = str(result_count) + '+'

    genderF = 0
    genderM = 1
    isopioidprescriber = 0
    AK = 0
    AL =0
    AR=0
    AZ=0
    CA=0
    CO=0
    CT=0
    DC=0
    FL=0
    GA=0
    HI=0
    IA=0
    ID=0
    IL=0
    IN=0
    KS=0
    KY=0
    LA=0
    MA=0
    MD=0
    ME=0
    MI=0
    MN=0
    MO=0
    MS=0
    MT=0
    NC=0
    ND=0
    NE=0
    NH=0
    NM=0
    NV=0
    NY=0
    OK=0
    OR=0
    PA=0
    PR=0
    RI=0
    SC=0
    TN=0
    TX=0
    UT=0
    VA=0
    VT=0
    WA=0
    WI=0
    WV=0
    WY=0

    special_dict = {"Internal Medicine": 0,"Family Practice": 0,
          "Cardiology": 0,
          "Nurse Practitioner": 0,
            "Neurology": 0,
          "Nephrology": 0,
            "Gastroenterology": 0,
            "Student in an Organized Health Care Education": 0,
            "Pulmonary Disease": 0,
            "Physician Assistant": 0,
            "Endocrinology": 0,
           "General Practice": 0,
            "Obstetrics": 0,
            "Emergency Medicine": 0,
            "Dentist": 0,
            "Dermatology": 0,
            "Gynecology": 0,
            "Radiation Oncology": 0,
            "Psychologist (billing independently)": 0,
            "Legal Medicine": 0,
            "Osteopathic Manipulative Medicine": 0,
            "Center": 0,
            "Rheumatology": 0,
            "Rehabilitation": 0,
            "Hematology": 0,
            "Ophthalmology": 0,
            "General Surgery": 0,
           "Orthopedic Surgery": 0,
            "Urology": 0,
            "Oncology": 0,
           "Geriatric Medicine": 0,
            "Training Program": 0,
            "Infectious Disease": 0,
            "Anesthesiology": 0,
            "Medical Oncology": 0}
    
    if gender == 'Female' :
        genderF = 1
        genderM = 0

    if state == "Alaska" :
        AK = 1
    elif state == 'Alabama' :
        AL = 1
    elif state == 'Arkansas' :
        AR = 1
    elif state == 'Arizona' :
        AZ = 1
    elif state == 'California' :
        CA = 1
    elif state == 'Colorado' :
        CO = 1
    elif state == 'Connecticut' :
        CT = 1
    elif state == 'Washington, D.C.' :
        DC = 1
    elif state == 'Florida' :
        FL = 1
    elif state == 'Georgia' :
        GA = 1
    elif state == 'Hawaii' :
        HI = 1
    elif state == 'Iowa' :
        IA = 1
    elif state == 'Idaho' :
        ID = 1
    elif state == 'Illinois' :
        IL = 1
    elif state == 'Indiana' :
        IN = 1
    elif state == 'Kansas' :
        KS = 1
    elif state == 'Kentucky' :
        KY = 1
    elif state == 'Louisiana' :
        LA = 1
    elif state == 'Massachussets' :
        MA = 1
    elif state == 'Maryland' :
        MD = 1
    elif state == 'Maine' :
        ME = 1
    elif state == 'Michigan' :
        MI = 1
    elif state == 'Montana' :
        MN = 1
    elif state == 'Missouri' :
        MO = 1
    elif state == 'Mississippi' :
        MS = 1
    elif state == 'Montana' :
        MT = 1
    elif state == 'North Carolina' :
        NC = 1
    elif state == 'North Dakota' :
        ND = 1
    elif state == 'Nebraska' :
        NE = 1
    elif state == 'New Hamphire' :
        NH = 1
    elif state == 'New Mexico' :
        NM = 1
    elif state == 'Nevada' :
        NV = 1
    elif state == 'New York' :
        NY = 1
    elif state == 'Oklahoma' :
        OK = 1
    elif state == 'Oregon' :
        OR = 1
    elif state == 'Pennsylvania' :
        PA = 1
    elif state == 'Puerto Rico' :
        PR = 1
    elif state == 'Rhode Island' :
        RI = 1
    elif state == 'South Carolina' :
        SC = 1
    elif state == 'Tennessee' :
        TN = 1
    elif state == 'Texas' :
        TX = 1
    elif state == 'Utah' :
        UT = 1
    elif state == 'Virginia' :
        VA = 1
    elif state == 'Vermont' :
        VT = 1
    elif state == 'Washington' :
        WA = 1
    elif state == 'Wisconsin' :
        WI = 1
    elif state == 'West Virginia' :
        WV = 1
    elif state == 'Wyoming' :
        WY = 1

    url = "http://865a706f-ddaa-4d50-bd71-4cd909771a7f.westus.azurecontainer.io/score"

    payload = json.dumps({
    "Inputs": {
        "WebServiceInput0": [
        {
            "isopioidprescriber": isopioidprescriber,
            "Ope": 0, #Keep this feature 0 always in the application
            "Cuberoot(totalprescriptions)": 12.918623821828756,
            "gender-F": genderF,
            "gender-M": genderM,
            "state-AK": AK,
            "state-AL": AL,
            "state-AR":AR,
            "state-AZ": AZ,
            "state-CA": CA,
            "state-CO": CO,
            "state-CT": CT,
            "state-DC": DC,
            "state-FL": FL,
            "state-GA": GA,
            "state-HI": HI,
            "state-IA": IA,
            "state-ID": ID,
            "state-IL": IL,
            "state-IN": IN,
            "state-KS": KS,
            "state-KY": KY,
            "state-LA": LA,
            "state-MA": MA,
            "state-MD": MD,
            "state-ME": ME,
            "state-MI": MI,
            "state-MN": MN,
            "state-MO": MO,
            "state-MS": MS,
            "state-MT": MT,
            "state-NC": NC,
            "state-ND": ND,
            "state-NE": NE,
            "state-NH": NH,
            "state-NM": NM,
            "state-NV": NV,
            "state-NY": NY,
            "state-OK": OK,
            "state-OR": OR,
            "state-PA": PA,
            "state-PR": PR,
            "state-RI": RI,
            "state-SC": SC,
            "state-TN": TN,
            "state-TX": TX,
            "state-UT": UT,
            "state-VA": VA,
            "state-VT": VT,
            "state-WA": WA,
            "state-WI": WI,
            "state-WV": WV,
            "state-WY": WY,
            "pdspecialty_id-Internal Medicine": special_dict["Internal Medicine"],
            "pdspecialty_id-Family Practice": special_dict["Family Practice"],
            "pdspecialty_id-Cardiology": special_dict["Cardiology"],
            "pdspecialty_id-Nurse Practitioner": special_dict["Nurse Practitioner"],
            "pdspecialty_id-Neurology": special_dict["Neurology"],
            "pdspecialty_id-Nephrology": special_dict["Nephrology"],
            "pdspecialty_id-Gastroenterology": special_dict["Gastroenterology"],
            "pdspecialty_id-Student in an Organized Health Care Education": special_dict["Student in an Organized Health Care Education"],
            "pdspecialty_id-Pulmonary Disease": special_dict["Pulmonary Disease"],
            "pdspecialty_id-Physician Assistant": special_dict["Physician Assistant"],
            "pdspecialty_id-Endocrinology": special_dict["Endocrinology"],
            "pdspecialty_id-General Practice": special_dict["General Practice"],
            "pdspecialty_id-Obstetrics": special_dict["Obstetrics"],
            "pdspecialty_id-Emergency Medicine": special_dict["Emergency Medicine"],
            "pdspecialty_id-Dentist": special_dict["Dentist"],
            "pdspecialty_id-Dermatology": special_dict["Dermatology"],
            "pdspecialty_id-Gynecology": special_dict["Gynecology"],
            "pdspecialty_id-Radiation Oncology": special_dict["Radiation Oncology"],
            "pdspecialty_id-Psychologist (billing independently)": special_dict["Psychologist (billing independently)"],
            "pdspecialty_id-Legal Medicine": special_dict["Legal Medicine"],
            "pdspecialty_id-Osteopathic Manipulative Medicine": special_dict["Osteopathic Manipulative Medicine"],
            "pdspecialty_id-Center": special_dict["Center"],
            "pdspecialty_id-Rheumatology":special_dict["Rheumatology"],
            "pdspecialty_id-Rehabilitation": special_dict["Rehabilitation"],
            "pdspecialty_id-Hematology": special_dict["Hematology"],
            "pdspecialty_id-Ophthalmology": special_dict["Ophthalmology"],
            "pdspecialty_id-General Surgery": special_dict["General Surgery"],
            "pdspecialty_id-Orthopedic Surgery": special_dict["Orthopedic Surgery"],
            "pdspecialty_id-Urology": special_dict["Urology"],
            "pdspecialty_id-Oncology": special_dict["Oncology"],
            "pdspecialty_id-Geriatric Medicine": special_dict["Geriatric Medicine"],
            "pdspecialty_id-Training Program": special_dict["Training Program"],
            "pdspecialty_id-Infectious Disease": special_dict["Infectious Disease"],
            "pdspecialty_id-Anesthesiology": special_dict["Anesthesiology"],
            "pdspecialty_id-Medical Oncology": special_dict["Medical Oncology"]
        }
        ]
    },
    "GlobalParameters": {}
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ctSJxwqI6zUw2wB2rfhwRkoMy8YHf91w'
    }

    response = pip._vendor.requests.request("POST", url, headers=headers, data=payload)

    json_data = json.loads(response.text)

    dic = json_data['Results']['WebServiceOutput0'][0]

    prediction = "Does not prescribe opioids."

    if dic["Scored Labels"] == 1:
        prediction = 1
    else:
        prediction = 0

    context = {
        "prescribers" : data,
        "states" : state_data,
        "result_count" : result_count,
        "specialties" : specialty_data,
        "predict" : prediction
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
    state_data = PdStatedata.objects.all()
    specialty_data = PdSpecialty.objects.all()

    context = {
        "prescribers": prescribers,
        "states" : state_data,
        "specialties" : specialty_data
    }

    return render(request, 'webapp/addprescriber.html', context)

def storePrescriberPageView(request):
    state_data = PdStatedata.objects.all()
    specialty_data = PdSpecialty.objects.all()

    #Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new prescriber object from the model (like a new record)
        new_prescriber = PdPrescriber()
        
        #Store the data from the form to the new object's attributes (like columns)
        new_prescriber.npi = request.POST.get('npi')
        new_prescriber.fname = request.POST.get('fname')                   
        new_prescriber.lname = request.POST.get('lname')
        new_prescriber.gender = request.POST.get('gender_select')
        new_prescriber.credentials = request.POST.get('credentials')
        
        state_input = request.POST.get('state_select') 
        for state in state_data :
            if state.state == state_input :
                new_prescriber.state = state

        licensed_check = request.POST.get('licensed_check')
        if licensed_check :
            new_prescriber.isopioidprescriber = 'TRUE'
        else :
            new_prescriber.isopioidprescriber = 'FALSE'
        
        new_prescriber.save()
        (specialty_input, created) = PdSpecialty.objects.get_or_create(title=request.POST.get('specialty_select'))
        print(created)
        new_prescriber.specialties.add(specialty_input)
        # for specialty in specialty_data :
        #     if specialty.title == specialty_input :
        #         new_prescriber.specialties.add(specialty)
        #         specialty.save()

        new_prescriber.save()

        # print(specialty_input)
        print(new_prescriber.specialties)

    data = PdPrescriber.objects.all()[0:100]
    state_data = PdStatedata.objects.all()
    specialty_data = PdSpecialty.objects.all()

    result_count = data.count()
    result_count = str(result_count) + '+'

    context = {
        "prescribers" : data,
        "states" : state_data,
        "result_count" : result_count,
        "specialties" : specialty_data
    }

    return render(request, 'webapp/prescribers.html', context)  

def aboutPageView(request) :
    return render(request, 'webapp/about.html')

def contactPageView(request) :
    return render(request, 'webapp/contact.html')