from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import F, Value
from django.db.models import ProtectedError
from .models import Vozidlo,Zakaznik,Pneumatiky,ServisZaznam,ServisPracovnik,TypZakaznik,TypVozidla, ZakaznikVozidloRelation, TypServis
from django.db.models.functions import Concat
from .forms import AddCustomerForm
import datetime

def index(request):
    num_vehicles = Vozidlo.objects.all().count()
    num_customers = Zakaznik.objects.all().count()
    num_tires = Pneumatiky.objects.all().count()
    num_records = ServisZaznam.objects.count()
    num_workers = ServisPracovnik.objects.all().count()

    context = {
        'num_vehicles': num_vehicles,
        'num_customers': num_customers,
        'num_tires': num_tires,
        'num_records': num_records,
        'num_workers': num_workers,
    }

    return render(request,'project/index.html', context=context)

def errorPage(request):
    return render(request, 'project/ErrorPage.html')

def customers(request):
    customers = Zakaznik.objects.all().annotate(text=Concat(F("jmeno"),Value(" "), F("prijmeni")))

    return render(request,'project/customers.html', {'customers':customers}) 

def add_customer_succesfull(request):

    if request.method == 'POST':

        typ_zakaznik = TypZakaznik.objects.get(typzakaznikid=1)
        cust_name = request.POST['cust_name']
        cust_lname = request.POST["cust_lname"]
        cust_log = request.POST["cust_log"]
        cust_tel = request.POST["cust_tel"]
        cust_address = request.POST["cust_address"]

        add_cust = Zakaznik(jmeno=cust_name, prijmeni=cust_lname, login=cust_log, telefon=cust_tel, adresa=cust_address, typzakaznikid=typ_zakaznik)
        add_cust.save()
        customers = Zakaznik.objects.all().annotate(text=Concat(F("jmeno"),Value(" "), F("prijmeni")))
        return render(request,'project/customers.html',{'customers':customers}) 

def edit_customer(request, cust_id):
    customer = Zakaznik.objects.get(pk=cust_id)

    if request.method == 'POST':
        customer.jmeno = request.POST['cust_name']
        customer.prijmeni = request.POST["cust_lname"]
        customer.login = request.POST["cust_log"]
        customer.telefon = request.POST["cust_tel"]
        tmp_adresa = request.POST["cust_address"]

        if tmp_adresa != "None":
            customer.adresa = tmp_adresa

        customer.save()
        return render(request,'project/customer.html', {'customer':customer})     

def customer(request, cust_id):
    cust =  get_object_or_404(Zakaznik,pk=cust_id)
    vehicles = Vozidlo.objects.raw('SELECT * ,v.ID as pk, v.znacka as znacka, v.spz as spz, tv.nazev as nazev FROM Vozidlo v JOIN Zakaznik_Vozidlo_Relation zv ON v.ID = zv.vozidloID JOIN Typ_vozidla tv ON v.typVozidlaID = tv.typVozidlaID WHERE zv.zakaznikID = %s', [cust_id])


    return render(request,'project/customer.html', {'customer':cust, 'vehicles':vehicles})


def customerDelete(request, cust_id):
    cust = get_object_or_404(Zakaznik, pk=cust_id) 

    customers = Zakaznik.objects.all().annotate(text=Concat(F("jmeno"),Value(" "), F("prijmeni")))

    if request.method == 'POST':   

        try:
            cust.delete()                     
            return redirect('/')  

        except ProtectedError as e:
             return render(request, 'project/ErrorPage.html')

        except Exception as e:
             return render(request, 'project/ErrorPage.html')

    return render(request,'project/customers.html', {'customers':customers})



def vehicles(request):
    cars = Vozidlo.objects.filter(typvozidlaid=1).order_by('znacka')
    bikes = Vozidlo.objects.filter(typvozidlaid=2).order_by('znacka')
    buses = Vozidlo.objects.filter(typvozidlaid=3).order_by('znacka')
    tractors = Vozidlo.objects.filter(typvozidlaid=4).order_by('znacka')
    trucks = Vozidlo.objects.filter(typvozidlaid=5).order_by('znacka')

    context = {
        'cars': cars,
        'bikes': bikes,
        'buses': buses,
        'tractors': tractors,
        'trucks': trucks,
    }

    return render(request,'project/vehicles.html', context=context) 

def addVehicle(request, cust_id):
    customer = Zakaznik.objects.get(pk=cust_id)

    if request.method == 'POST':   
        veh_brand = request.POST['veh_brand'] 
        veh_model = request.POST['veh_model'] 
        veh_spz = request.POST['veh_spz'] 
        tmp_type = request.POST['veh_type']       
        
        tmp_veh = Vozidlo.objects.filter(spz=veh_spz).count()

        if tmp_veh != 0:
            exist_veh = Vozidlo.objects.get(spz=veh_spz)
            create_relation=ZakaznikVozidloRelation(zakaznikid=customer, vozidloid=exist_veh)
            create_relation.save()

            vehicles = Vozidlo.objects.raw('SELECT * ,v.ID as pk, v.znacka as znacka, v.spz as spz, tv.nazev as nazev FROM Vozidlo v JOIN Zakaznik_Vozidlo_Relation zv ON v.ID = zv.vozidloID JOIN Typ_vozidla tv ON v.typVozidlaID = tv.typVozidlaID WHERE zv.zakaznikID = %s', [cust_id])

            return render(request,'project/customer.html', {'customer':customer, 'vehicles':vehicles}) 
        else:
            veh_type=TypVozidla.objects.get(typvozidlaid=tmp_type)

            veh_znacka = veh_brand + " " + veh_model
            add_vehicle = Vozidlo(znacka=veh_znacka, spz=veh_spz, typvozidlaid=veh_type)
            add_vehicle.save()

            create_relation=ZakaznikVozidloRelation(zakaznikid=customer, vozidloid=add_vehicle)
            create_relation.save()

            vehicles = Vozidlo.objects.raw('SELECT * ,v.ID as pk, v.znacka as znacka, v.spz as spz, tv.nazev as nazev FROM Vozidlo v JOIN Zakaznik_Vozidlo_Relation zv ON v.ID = zv.vozidloID JOIN Typ_vozidla tv ON v.typVozidlaID = tv.typVozidlaID WHERE zv.zakaznikID = %s', [cust_id])

            return render(request,'project/customer.html', {'customer':customer, 'vehicles':vehicles}) 



def vehicleDelete(request, cust_id): 

    cust = get_object_or_404(Zakaznik, pk=cust_id) 
   

    veh_id = request.POST["veh_id"]

    for word in veh_id.split():
        if word.isdigit():
            veh_id = word

    veh = get_object_or_404(Vozidlo, pk=veh_id)

    vehToCust=ZakaznikVozidloRelation.objects.filter(zakaznikid=cust.id, vozidloid=veh.id)

    try:
        vehToCust.delete()
        vehCount = ZakaznikVozidloRelation.objects.filter(vozidloid=veh_id).count()
        if vehCount == 0:
            veh.delete()              
        return redirect('/customer/'+str(cust_id))  

    except ProtectedError as e:
        return render(request, 'project/ErrorPage.html')

    except Exception as e:
        return render(request, 'project/ErrorPage.html')   
   
    return render(request,'project/customers.html', {'customers':customers})

def vehicle(request, veh_id):
    veh =  get_object_or_404(Vozidlo,pk=veh_id)

    customers = Zakaznik.objects.raw('SELECT * FROM Zakaznik JOIN Zakaznik_Vozidlo_Relation zv on Zakaznik.ID = zv.zakaznikID WHERE zv.vozidloID = %s', [veh_id])

    return render(request,'project/vehicle.html', {'vehicle':veh, 'customers':customers})

def edit_vehicle(request, veh_id):
    veh = Vozidlo.objects.get(pk=veh_id)

    if request.method == 'POST':
        veh.znacka = request.POST['veh_brand']
        veh.spz = request.POST["veh_spz"]

        veh.save()

        customers = Zakaznik.objects.raw('SELECT * FROM Zakaznik JOIN Zakaznik_Vozidlo_Relation zv on Zakaznik.ID = zv.zakaznikID WHERE zv.vozidloID = %s', [veh_id])
        return render(request,'project/vehicle.html', {'vehicle':veh, 'customers':customers}) 

def workers(request):
    workers = ServisPracovnik.objects.all()
    return render(request, 'project/workers.html', {'workers':workers})


def tires(request):
    tires = Pneumatiky.objects.all().order_by('znacka')
    return render(request, 'project/tires.html', {'tires':tires})

def tire(request, pneu_id):
    tire = get_object_or_404(Pneumatiky,pk=pneu_id)
    return render(request, 'project/tire.html', {'tire':tire})

def edit_tire(request, pneu_id):
    tire = Pneumatiky.objects.get(pk=pneu_id)

    if request.method == 'POST':
        tire.znacka = request.POST['tire_brand']
        tire.rozmery = request.POST["tire_size"]
        tire.hloubka_dezenu = request.POST["tire_depth"]

        if int(tire.hloubka_dezenu) < int(8):
            tire.sjete = '1'
        else: 
            tire.sjete = '0'

        tire.save()
        return render(request,'project/tire.html', {'tire':tire}) 


def tireDelete(request, pneu_id):
    tire = get_object_or_404(Pneumatiky,pk=pneu_id)

    tires = Pneumatiky.objects.all().order_by('znacka')

    if request.method == 'POST':   

        try:
            tire.delete()                     
            return render(request,'project/tires.html', {'tires':tires}) 

        except ProtectedError as e:
             return render(request, 'project/ErrorPage.html')

        except Exception as e:
             return render(request, 'project/ErrorPage.html')

    return render(request,'project/tires.html', {'tires':tires})

def add_tire(request):

    if request.method == 'POST':   
        tire_brand = request.POST['tire_brand']
        tire_model = request.POST["tire_model"]
        tire_size = request.POST["tire_size"]
        tire_depth = request.POST["tire_depth"]
        tire_type = request.POST["tire_type"]

        if 'tire_used' in request.POST:
            tire_used = request.POST['tire_used']
        else:
            tire_used = 0

        
        
        tire_name = tire_brand + " " + tire_model

        add_tire = Pneumatiky(znacka=tire_name, rozmery=tire_size, hloubka_dezenu=tire_depth, typ=tire_type, sjete=tire_used)
        add_tire.save()

        tires = Pneumatiky.objects.all().order_by('znacka')
        return render(request,'project/tires.html',{'tires':tires}) 

def records(request):
    records = ServisZaznam.objects.all().order_by('-datum')

    return render(request, 'project/serviceRecords.html', {'records':records})

def deleteRecord(request, rec_id):
    record = get_object_or_404(ServisZaznam,pk=rec_id)

    records = ServisZaznam.objects.all().order_by('-datum')

    if request.method == 'POST':   

        try:
            record.delete()                     
            return render(request, 'project/serviceRecords.html', {'records':records}) 

        except ProtectedError as e:
             return render(request, 'project/ErrorPage.html')

        except Exception as e:
             return render(request, 'project/ErrorPage.html')

    return render(request, 'project/serviceRecords.html', {'records':records})


def getCustomer(request):
    customer = request.GET.get("cust_name", None)

    vehicles = Vozidlo.objects.raw('SELECT * FROM Vozidlo JOIN Zakaznik_Vozidlo_Relation zv on vozidlo.ID = zv.vozidloID WHERE zv.zakaznikID = %s', [customer])

    vehToCus = []
    
    for vehicle in vehicles:
        vozidloID = vehicle.id
        znacka = vehicle.znacka
        vehicle = {
            'id':str(vozidloID),
            'znacka':str(znacka)
        }
        
        vehToCus.append(vehicle)

    data = { 
        'vehicles':vehToCus
    }
    
    return JsonResponse(data)

def add_record(request):

    customers = Zakaznik.objects.all()
    ftires = Pneumatiky.objects.all().order_by('znacka')
    rtires = Pneumatiky.objects.all().order_by('znacka')
    workers = ServisPracovnik.objects.all()
    types = TypServis.objects.all()

    context = {
        'customers': customers,
        'vehicles': vehicles,
        'ftires': ftires,
        'rtires': rtires,
        'workers': workers,
        'types': types,
    }


    return render(request, 'project/addRecord.html', context=context)

def add_record_success(request):

    if request.method == 'POST':   
        customer_t = request.POST['cust_name']
        vehicle_t = request.POST["veh_name"]
        ftire_t = request.POST["ftire_name"]
        rtire_t = request.POST["rtire_name"]
        worker_t = request.POST["worker_name"]
        type_s_t = request.POST["type_name"]

        worker = ServisPracovnik.objects.get(pk=worker_t)
        customer = Zakaznik.objects.get(pk=customer_t)
        ftire = Pneumatiky.objects.get(pk=ftire_t)
        rtire = Pneumatiky.objects.get(pk=rtire_t)
        type_s = TypServis.objects.get(pk=type_s_t)
        vehicle = Vozidlo.objects.get(pk=vehicle_t)

        datum = datetime.datetime.today()


        add_record = ServisZaznam(datum=datum, pracovnikid=worker, typid=type_s, zakaznikid=customer, vozidloid=vehicle, pneuid_predni=ftire, pneuid_zadni=rtire)
        add_record.save()


        vehicle.pneuid_predni = ftire
        vehicle.pneuid_zadni = rtire
        vehicle.save()

        records = ServisZaznam.objects.all().order_by('-datum')

        return render(request, 'project/serviceRecords.html', {'records':records})

def contact(request):

    return render(request, 'project/contacts.html')

def deleteTireFromVeh(request, veh_id):
    
    if request.method == 'POST':  
        vehicle = Vozidlo.objects.get(pk=veh_id)

        vehicle.pneuid_predni = None
        vehicle.pneuid_zadni = None
        vehicle.save()

        

    customers = Zakaznik.objects.raw('SELECT * FROM Zakaznik JOIN Zakaznik_Vozidlo_Relation zv on Zakaznik.ID = zv.zakaznikID WHERE zv.vozidloID = %s', [veh_id])

    return render(request,'project/vehicle.html', {'vehicle':veh, 'customers':customers})

       