# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class PdDrugs(models.Model):
    drugid = models.IntegerField(primary_key=True)
    drugname = models.CharField(max_length=30)
    isopioid = models.CharField(max_length=5)

    def __str__(self):
        return (self.drugname)

    class Meta:
        managed = False
        db_table = 'pd_drugs'


class PdPrescriber(models.Model):
    npi = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.CharField(max_length=2)
    credentials = models.CharField(max_length=20, blank=True, null=True)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField()
    abilify = models.IntegerField()
    acetaminophencodeine = models.IntegerField()
    acyclovir = models.IntegerField()
    advairdiskus = models.IntegerField()
    aggrenox = models.IntegerField()
    alendronatesodium = models.IntegerField()
    allopurinol = models.IntegerField()
    alprazolam = models.IntegerField()
    amiodaronehcl = models.IntegerField()
    amitriptylinehcl = models.IntegerField()
    amlodipinebesylate = models.IntegerField()
    amlodipinebesylatebenazepril = models.IntegerField()
    amoxicillin = models.IntegerField()
    amoxtrpotassiumclavulanate = models.IntegerField()
    amphetaminesaltcombo = models.IntegerField()
    atenolol = models.IntegerField()
    atorvastatincalcium = models.IntegerField()
    avodart = models.IntegerField()
    azithromycin = models.IntegerField()
    baclofen = models.IntegerField()
    bdultrafinepenneedle = models.IntegerField()
    benazeprilhcl = models.IntegerField()
    benicar = models.IntegerField()
    benicarhct = models.IntegerField()
    benztropinemesylate = models.IntegerField()
    bisoprololhydrochlorothiazide = models.IntegerField()
    brimonidinetartrate = models.IntegerField()
    bumetanide = models.IntegerField()
    bupropionhclsr = models.IntegerField()
    bupropionxl = models.IntegerField()
    buspironehcl = models.IntegerField()
    bystolic = models.IntegerField()
    carbamazepine = models.IntegerField()
    carbidopalevodopa = models.IntegerField()
    carisoprodol = models.IntegerField()
    cartiaxt = models.IntegerField()
    carvedilol = models.IntegerField()
    cefuroxime = models.IntegerField()
    celebrex = models.IntegerField()
    cephalexin = models.IntegerField()
    chlorhexidinegluconate = models.IntegerField()
    chlorthalidone = models.IntegerField()
    cilostazol = models.IntegerField()
    ciprofloxacinhcl = models.IntegerField()
    citalopramhbr = models.IntegerField()
    clindamycinhcl = models.IntegerField()
    clobetasolpropionate = models.IntegerField()
    clonazepam = models.IntegerField()
    clonidinehcl = models.IntegerField()
    clopidogrel = models.IntegerField()
    clotrimazolebetamethasone = models.IntegerField()
    colcrys = models.IntegerField()
    combiventrespimat = models.IntegerField()
    crestor = models.IntegerField()
    cyclobenzaprinehcl = models.IntegerField()
    dexilant = models.IntegerField()
    diazepam = models.IntegerField()
    diclofenacsodium = models.IntegerField()
    dicyclominehcl = models.IntegerField()
    digox = models.IntegerField()
    digoxin = models.IntegerField()
    diltiazem24hrcd = models.IntegerField()
    diltiazem24hrer = models.IntegerField()
    diltiazemer = models.IntegerField()
    diltiazemhcl = models.IntegerField()
    diovan = models.IntegerField()
    diphenoxylateatropine = models.IntegerField()
    divalproexsodium = models.IntegerField()
    divalproexsodiumer = models.IntegerField()
    donepezilhcl = models.IntegerField()
    dorzolamidetimolol = models.IntegerField()
    doxazosinmesylate = models.IntegerField()
    doxepinhcl = models.IntegerField()
    doxycyclinehyclate = models.IntegerField()
    duloxetinehcl = models.IntegerField()
    enalaprilmaleate = models.IntegerField()
    escitalopramoxalate = models.IntegerField()
    estradiol = models.IntegerField()
    exelon = models.IntegerField()
    famotidine = models.IntegerField()
    felodipineer = models.IntegerField()
    fenofibrate = models.IntegerField()
    fentanyl = models.IntegerField()
    finasteride = models.IntegerField()
    floventhfa = models.IntegerField()
    fluconazole = models.IntegerField()
    fluoxetinehcl = models.IntegerField()
    fluticasonepropionate = models.IntegerField()
    furosemide = models.IntegerField()
    gabapentin = models.IntegerField()
    gemfibrozil = models.IntegerField()
    glimepiride = models.IntegerField()
    glipizide = models.IntegerField()
    glipizideer = models.IntegerField()
    glipizidexl = models.IntegerField()
    glyburide = models.IntegerField()
    haloperidol = models.IntegerField()
    humalog = models.IntegerField()
    hydralazinehcl = models.IntegerField()
    hydrochlorothiazide = models.IntegerField()
    hydrocodoneacetaminophen = models.IntegerField()
    hydrocortisone = models.IntegerField()
    hydromorphonehcl = models.IntegerField()
    hydroxyzinehcl = models.IntegerField()
    ibandronatesodium = models.IntegerField()
    ibuprofen = models.IntegerField()
    insulinsyringe = models.IntegerField()
    ipratropiumbromide = models.IntegerField()
    irbesartan = models.IntegerField()
    isosorbidemononitrateer = models.IntegerField()
    jantoven = models.IntegerField()
    janumet = models.IntegerField()
    januvia = models.IntegerField()
    ketoconazole = models.IntegerField()
    klorcon10 = models.IntegerField()
    klorconm10 = models.IntegerField()
    klorconm20 = models.IntegerField()
    labetalolhcl = models.IntegerField()
    lactulose = models.IntegerField()
    lamotrigine = models.IntegerField()
    lansoprazole = models.IntegerField()
    lantus = models.IntegerField()
    lantussolostar = models.IntegerField()
    latanoprost = models.IntegerField()
    levemir = models.IntegerField()
    levemirflexpen = models.IntegerField()
    levetiracetam = models.IntegerField()
    levofloxacin = models.IntegerField()
    levothyroxinesodium = models.IntegerField()
    lidocaine = models.IntegerField()
    lisinopril = models.IntegerField()
    lisinoprilhydrochlorothiazide = models.IntegerField()
    lithiumcarbonate = models.IntegerField()
    lorazepam = models.IntegerField()
    losartanhydrochlorothiazide = models.IntegerField()
    losartanpotassium = models.IntegerField()
    lovastatin = models.IntegerField()
    lovaza = models.IntegerField()
    lumigan = models.IntegerField()
    lyrica = models.IntegerField()
    meclizinehcl = models.IntegerField()
    meloxicam = models.IntegerField()
    metforminhcl = models.IntegerField()
    metforminhcler = models.IntegerField()
    methadonehcl = models.IntegerField()
    methocarbamol = models.IntegerField()
    methotrexate = models.IntegerField()
    methylprednisolone = models.IntegerField()
    metoclopramidehcl = models.IntegerField()
    metolazone = models.IntegerField()
    metoprololsuccinate = models.IntegerField()
    metoprololtartrate = models.IntegerField()
    metronidazole = models.IntegerField()
    mirtazapine = models.IntegerField()
    montelukastsodium = models.IntegerField()
    morphinesulfate = models.IntegerField()
    morphinesulfateer = models.IntegerField()
    mupirocin = models.IntegerField()
    nabumetone = models.IntegerField()
    namenda = models.IntegerField()
    namendaxr = models.IntegerField()
    naproxen = models.IntegerField()
    nasonex = models.IntegerField()
    nexium = models.IntegerField()
    niaciner = models.IntegerField()
    nifedicalxl = models.IntegerField()
    nifedipineer = models.IntegerField()
    nitrofurantoinmonomacro = models.IntegerField()
    nitrostat = models.IntegerField()
    nortriptylinehcl = models.IntegerField()
    novolog = models.IntegerField()
    novologflexpen = models.IntegerField()
    nystatin = models.IntegerField()
    olanzapine = models.IntegerField()
    omeprazole = models.IntegerField()
    ondansetronhcl = models.IntegerField()
    ondansetronodt = models.IntegerField()
    onglyza = models.IntegerField()
    oxcarbazepine = models.IntegerField()
    oxybutyninchloride = models.IntegerField()
    oxybutyninchlorideer = models.IntegerField()
    oxycodoneacetaminophen = models.IntegerField()
    oxycodonehcl = models.IntegerField()
    oxycontin = models.IntegerField()
    pantoprazolesodium = models.IntegerField()
    paroxetinehcl = models.IntegerField()
    phenobarbital = models.IntegerField()
    phenytoinsodiumextended = models.IntegerField()
    pioglitazonehcl = models.IntegerField()
    polyethyleneglycol3350 = models.IntegerField()
    potassiumchloride = models.IntegerField()
    pradaxa = models.IntegerField()
    pramipexoledihydrochloride = models.IntegerField()
    pravastatinsodium = models.IntegerField()
    prednisone = models.IntegerField()
    premarin = models.IntegerField()
    primidone = models.IntegerField()
    proairhfa = models.IntegerField()
    promethazinehcl = models.IntegerField()
    propranololhcl = models.IntegerField()
    propranololhcler = models.IntegerField()
    quetiapinefumarate = models.IntegerField()
    quinaprilhcl = models.IntegerField()
    raloxifenehcl = models.IntegerField()
    ramipril = models.IntegerField()
    ranexa = models.IntegerField()
    ranitidinehcl = models.IntegerField()
    restasis = models.IntegerField()
    risperidone = models.IntegerField()
    ropinirolehcl = models.IntegerField()
    seroquelxr = models.IntegerField()
    sertralinehcl = models.IntegerField()
    simvastatin = models.IntegerField()
    sotalol = models.IntegerField()
    spiriva = models.IntegerField()
    spironolactone = models.IntegerField()
    sucralfate = models.IntegerField()
    sulfamethoxazoletrimethoprim = models.IntegerField()
    sumatriptansuccinate = models.IntegerField()
    symbicort = models.IntegerField()
    synthroid = models.IntegerField()
    tamsulosinhcl = models.IntegerField()
    temazepam = models.IntegerField()
    terazosinhcl = models.IntegerField()
    timololmaleate = models.IntegerField()
    tizanidinehcl = models.IntegerField()
    tolterodinetartrateer = models.IntegerField()
    topiramate = models.IntegerField()
    toprolxl = models.IntegerField()
    torsemide = models.IntegerField()
    tramadolhcl = models.IntegerField()
    travatanz = models.IntegerField()
    trazodonehcl = models.IntegerField()
    triamcinoloneacetonide = models.IntegerField()
    triamterenehydrochlorothiazid = models.IntegerField()
    valacyclovir = models.IntegerField()
    valsartan = models.IntegerField()
    valsartanhydrochlorothiazide = models.IntegerField()
    venlafaxinehcl = models.IntegerField()
    venlafaxinehcler = models.IntegerField()
    ventolinhfa = models.IntegerField()
    verapamiler = models.IntegerField()
    vesicare = models.IntegerField()
    voltaren = models.IntegerField()
    vytorin = models.IntegerField()
    warfarinsodium = models.IntegerField()
    xarelto = models.IntegerField()
    zetia = models.IntegerField()
    ziprasidonehcl = models.IntegerField()
    zolpidemtartrate = models.IntegerField()
    opioidprescribe = models.BooleanField()

    def __str__(self):
        return (self.lname)

    class Meta:
        managed = False
        db_table = 'pd_prescriber'


class PdStatedata(models.Model):
    state = models.CharField(primary_key=True, max_length=14)
    stateabbrev = models.CharField(max_length=2)
    population = models.IntegerField()
    deaths = models.IntegerField()

    def __str__(self):
        return (self.state)

    class Meta:
        managed = False
        db_table = 'pd_statedata'


class PdTriple(models.Model):
    id = models.IntegerField(primary_key=True)
    prescriberid = models.IntegerField()
    drugname = models.CharField(max_length=30)
    qty = models.IntegerField()

    def __str__(self):
        return (self.id)

    class Meta:
        managed = False
        db_table = 'pd_triple'
