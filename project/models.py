# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Pneumatiky(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    typ = models.IntegerField()
    znacka = models.CharField(max_length=50, blank=True, null=True)
    rozmery = models.CharField(max_length=30)
    hloubka_dezenu = models.IntegerField()
    sjete = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'Pneumatiky'

    def __str__(self):
        return   str(self.id) + " " + self.znacka + " "+ self.rozmery


class ServisPracovnik(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    login = models.CharField(max_length=10)
    datum_narozeni = models.DateField(blank=True, null=True)
    telefon = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'Servis_pracovnik'

    def __str__(self):
        return str(self.id) + " " + self.jmeno + " "+ self.prijmeni + " " + self.login


class ServisZaznam(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    datum = models.DateTimeField()
    pracovnikid = models.ForeignKey(ServisPracovnik, models.DO_NOTHING, db_column='pracovnikID')  # Field name made lowercase.
    typid = models.ForeignKey('TypServis', models.DO_NOTHING, db_column='typID')  # Field name made lowercase.
    zakaznikid = models.ForeignKey('Zakaznik', models.DO_NOTHING, db_column='zakaznikID', blank=True, null=True)  # Field name made lowercase.
    vozidloid = models.ForeignKey('Vozidlo', models.DO_NOTHING, db_column='vozidloID', blank=True, null=True)  # Field name made lowercase.
    pneuid_predni = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID_predni', related_name='SZ_predni_pneu')  # Field name made lowercase.
    pneuid_zadni = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID_zadni', related_name='SZ_zadni_pneu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Servis_zaznam'

    def __str__(self):
        return   str(self.id) + " " + self.datum


class Sklad(models.Model):
    skladid = models.IntegerField(db_column='skladID', primary_key=True)  # Field name made lowercase.
    pocet = models.IntegerField()
    misto_uskladneni = models.IntegerField(blank=True, null=True)
    pneuid = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sklad'

    def __str__(self):
        return   str(self.skladid)

class TypServis(models.Model):
    typid = models.AutoField(db_column='typID', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Typ_servis'
    
    def __str__(self):
        return   str(self.typid) + " " + self.nazev


class TypVozidla(models.Model):
    typvozidlaid = models.IntegerField(db_column='typVozidlaID', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Typ_vozidla'
    
    def __str__(self):
        return str(self.typvozidlaid) + " " + self.nazev


class TypZakaznik(models.Model):
    typzakaznikid = models.IntegerField(db_column='typZakaznikID', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(max_length=40)
    registrovany = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'Typ_zakaznik'

    def __str__(self):
        return  str(self.typzakaznikid) + " " + self.nazev



class Vozidlo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    znacka = models.CharField(max_length=50, blank=True, null=True)
    spz = models.CharField(max_length=7)
    typvozidlaid = models.ForeignKey(TypVozidla, models.DO_NOTHING, db_column='typVozidlaID')  # Field name made lowercase.
    pneuid_predni = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID_predni', blank=True, null=True, related_name='V_predni_pneu')  # Field name made lowercase.
    pneuid_zadni = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID_zadni', blank=True, null=True, related_name='V_zadni_pneu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vozidlo'

    def __str__(self):
        return  str(self.id) + " " + self.znacka


class Zakaznik(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    adresa = models.CharField(max_length=40, blank=True, null=True)
    telefon = models.IntegerField()
    typzakaznikid = models.ForeignKey(TypZakaznik, models.DO_NOTHING, db_column='typZakaznikID')  # Field name made lowercase.
    pneuid = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID', blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Zakaznik'

    def __str__(self):
        return  str(self.id) + " " + self.jmeno + " " + self.prijmeni


class ZakaznikVozidloRelation(models.Model):
    zakaznikid = models.ForeignKey(Zakaznik, models.DO_NOTHING, db_column='zakaznikID')  # Field name made lowercase.
    vozidloid = models.ForeignKey(Vozidlo, models.DO_NOTHING, db_column='vozidloID')  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'Zakaznik_Vozidlo_Relation'

    def __str__(self):
        return  str(self.zakaznikid) + " " + str(self.vozidloid)




class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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

