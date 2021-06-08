# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Calender(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reservationdate = models.CharField(db_column='reservationDate', max_length=50)  # Field name made lowercase.
    guestid = models.ForeignKey('Guest', models.DO_NOTHING, db_column='guestID')  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vehicleID')  # Field name made lowercase.
    reservationtime = models.TimeField(db_column='reservationTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calender'


class Guest(models.Model):
    guestid = models.AutoField(db_column='guestID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    telephone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Guest'


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


class ServisPracovnik(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    login = models.CharField(max_length=10)
    datum_narozeni = models.DateField(blank=True, null=True)
    telefon = models.IntegerField()
    pracovnikid = models.IntegerField(db_column='pracovnikID')  # Field name made lowercase.
    jmeno_0 = models.CharField(db_column='jmeno', max_length=30)  # Field renamed because of name conflict.
    prijmeni_0 = models.CharField(db_column='prijmeni', max_length=30)  # Field renamed because of name conflict.
    login_0 = models.CharField(db_column='login', max_length=10)  # Field renamed because of name conflict.
    heslo = models.CharField(max_length=50)
    datum_narozeni_0 = models.DateField(db_column='datum_narozeni', blank=True, null=True)  # Field renamed because of name conflict.
    telefon_0 = models.IntegerField(db_column='telefon')  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'Servis_pracovnik'


class ServisZaznam(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    datum = models.DateTimeField()
    pracovnikid = models.ForeignKey(ServisPracovnik, models.DO_NOTHING, db_column='pracovnikID')  # Field name made lowercase.
    typid = models.ForeignKey('TypServis', models.DO_NOTHING, db_column='typID')  # Field name made lowercase.
    zakaznikid = models.ForeignKey('Zakaznik', models.DO_NOTHING, db_column='zakaznikID', blank=True, null=True)  # Field name made lowercase.
    vozidloid = models.ForeignKey('Vozidlo', models.DO_NOTHING, db_column='vozidloID', blank=True, null=True)  # Field name made lowercase.
    pneuid_predni = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID_predni')  # Field name made lowercase.
    pneuid_zadni = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID_zadni')  # Field name made lowercase.
    zaznamid = models.IntegerField(db_column='zaznamID')  # Field name made lowercase.
    datum_0 = models.DateTimeField(db_column='datum')  # Field renamed because of name conflict.
    zakaznikid_0 = models.ForeignKey('Zakaznik', models.DO_NOTHING, db_column='zakaznikID', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    vozidloid_0 = models.ForeignKey('Vozidlo', models.DO_NOTHING, db_column='vozidloID', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    pracovnikid_0 = models.ForeignKey(ServisPracovnik, models.DO_NOTHING, db_column='pracovnikID')  # Field name made lowercase. Field renamed because of name conflict.
    typid_0 = models.ForeignKey('TypServis', models.DO_NOTHING, db_column='typID')  # Field name made lowercase. Field renamed because of name conflict.
    pneuid = models.IntegerField(db_column='pneuID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Servis_zaznam'


class Sklad(models.Model):
    skladid = models.IntegerField(db_column='skladID', primary_key=True)  # Field name made lowercase.
    pocet = models.IntegerField()
    misto_uskladneni = models.IntegerField(blank=True, null=True)
    pneuid = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sklad'


class Test(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TEST'


class TypServis(models.Model):
    typid = models.AutoField(db_column='typID', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(max_length=50)
    typid_0 = models.AutoField(db_column='typID', primary_key=True)  # Field name made lowercase. Field renamed because of name conflict.
    nazev_0 = models.CharField(db_column='nazev', max_length=50)  # Field renamed because of name conflict.
    cena = models.IntegerField()
    poznamka = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Typ_servis'


class TypVozidla(models.Model):
    typvozidlaid = models.IntegerField(db_column='typVozidlaID', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Typ_vozidla'


class TypZakaznik(models.Model):
    typzakaznikid = models.IntegerField(db_column='typZakaznikID', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(max_length=40)
    registrovany = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'Typ_zakaznik'


class Vehicle(models.Model):
    vehicleid = models.AutoField(db_column='vehicleID', primary_key=True)  # Field name made lowercase.
    brand = models.CharField(max_length=50)
    spz = models.CharField(max_length=20)
    servicetype = models.CharField(db_column='serviceType', max_length=50)  # Field name made lowercase.
    vehicletype = models.CharField(db_column='vehicleType', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vehicle'


class Vozidlo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    znacka = models.CharField(max_length=50, blank=True, null=True)
    spz = models.CharField(max_length=7)
    typvozidlaid = models.ForeignKey(TypVozidla, models.DO_NOTHING, db_column='typVozidlaID')  # Field name made lowercase.
    pneuid_predni = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID_predni', blank=True, null=True)  # Field name made lowercase.
    pneuid_zadni = models.ForeignKey(Pneumatiky, models.DO_NOTHING, db_column='pneuID_zadni', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vozidlo'


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


class ZakaznikVozidloRelation(models.Model):
    zakaznikid = models.ForeignKey(Zakaznik, models.DO_NOTHING, db_column='zakaznikID')  # Field name made lowercase.
    vozidloid = models.ForeignKey(Vozidlo, models.DO_NOTHING, db_column='vozidloID')  # Field name made lowercase.
    zakaznikid_0 = models.ForeignKey(Zakaznik, models.DO_NOTHING, db_column='zakaznikID')  # Field name made lowercase. Field renamed because of name conflict.
    vozidloid_0 = models.ForeignKey(Vozidlo, models.DO_NOTHING, db_column='vozidloID')  # Field name made lowercase. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'Zakaznik_Vozidlo_Relation'
        unique_together = (('zakaznikid_0', 'vozidloid_0'),)


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actor'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City', models.DO_NOTHING)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'address'


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


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store', models.DO_NOTHING)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    active = models.CharField(max_length=1)
    create_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer'


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


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    release_year = models.CharField(max_length=4, blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    original_language = models.ForeignKey('Language', models.DO_NOTHING, blank=True, null=True)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=10, blank=True, null=True)
    special_features = models.CharField(max_length=255, blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film'


class FilmActor(models.Model):
    actor = models.OneToOneField(Actor, models.DO_NOTHING, primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = (('actor', 'film'),)


class FilmCategory(models.Model):
    film = models.OneToOneField(Film, models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_category'
        unique_together = (('film', 'category'),)


class FilmText(models.Model):
    film_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film_text'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    store = models.ForeignKey('Store', models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'language'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    rental = models.ForeignKey('Rental', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    picture = models.BinaryField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING)
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'staff'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(Staff, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'store'
