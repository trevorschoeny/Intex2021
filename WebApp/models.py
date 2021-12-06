# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PdStatedata(models.Model):
    state = models.CharField(max_length=14)
    stateabbrev = models.CharField(primary_key=True, max_length=2)
    population = models.IntegerField()
    deaths = models.IntegerField()

    def __str__(self):
        return (self.state)

    class Meta:
        db_table = 'pd_statedata'


class PdCredential(models.Model):
    title = models.CharField(primary_key=True, max_length=20)

    class Meta:
        db_table = 'pd_credential'


class PdDrugs(models.Model):
    drugid = models.IntegerField(primary_key=True)
    drugname = models.CharField(max_length=30)
    isopioid = models.CharField(max_length=5)

    def __str__(self):
        return (self.drugname)

    class Meta:
        db_table = 'pd_drugs'


class PdPrescriber(models.Model):
    npi = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.ForeignKey(PdStatedata, models.DO_NOTHING, db_column='state')
    credentials = models.CharField(max_length=30, blank=True, null=True)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField(blank=True, null=True)

    specialties = models.ManyToManyField('PdSpecialty', through='PdPrescriberSpecialties')
    drugs = models.ManyToManyField('PdDrugs', through='PdPrescriberDrugs')

    def __str__(self):
        return (self.fname + ' ' + self.lname)

    class Meta:
        db_table = 'pd_prescriber'


class PdPrescriberDrugs(models.Model):
    id = models.BigAutoField(primary_key=True)
    pdprescriber = models.ForeignKey(PdPrescriber, models.DO_NOTHING)
    pddrugs = models.ForeignKey(PdDrugs, models.DO_NOTHING)
    qty = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return (str(self.pdprescriber) + ' - ' + str(self.pddrugs) + ' - ' + str(self.qty))

    class Meta:
        db_table = 'pd_prescriber_drugs'
        unique_together = (('pdprescriber', 'pddrugs'),)


class PdPrescriberSpecialties(models.Model):
    id = models.BigAutoField(primary_key=True)
    pdprescriber = models.ForeignKey(PdPrescriber, models.DO_NOTHING)
    pdspecialty = models.ForeignKey('PdSpecialty', models.DO_NOTHING)

    class Meta:
        db_table = 'pd_prescriber_specialties'
        unique_together = (('pdprescriber', 'pdspecialty'),)


class PdSpecialty(models.Model):
    title = models.CharField(primary_key=True, max_length=62)

    def __str__(self):
        return (self.title)

    class Meta:
        db_table = 'pd_specialty'


class PdTriplenew(models.Model):
    prescriberid = models.OneToOneField(PdPrescriber, models.DO_NOTHING, db_column='prescriberid', primary_key=True, default=1003008475)
    qty = models.IntegerField()
    drugid = models.ForeignKey(PdDrugs, models.DO_NOTHING, db_column='drugid', default=2)

    class Meta:
        managed = False
        db_table = 'pd_triplenew'
        unique_together = (('prescriberid', 'qty', 'drugid'),)


class PrescriberCredential(models.Model):
    id = models.IntegerField(primary_key=True)
    prescriber_id = models.IntegerField()
    credential_title = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'prescriber_credential'


class PrescriberSpecialty(models.Model):
    id = models.IntegerField(primary_key=True)
    prescriber = models.ForeignKey(PdPrescriber, models.DO_NOTHING, default=1003008475)
    specialty_title = models.ForeignKey(PdSpecialty, models.DO_NOTHING, db_column='specialty_title', default='Clinic')

    class Meta:
        managed = False
        db_table = 'prescriber_specialty'
