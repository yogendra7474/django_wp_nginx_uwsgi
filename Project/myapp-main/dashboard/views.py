import csv
import json
from accounts.models import User
from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from .filters import ClientFilter
from data.models import Client
from home.models import ProfileData
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db.models.functions import Concat
from django.db.models import Value
from dashboard import signals
from .signals import notification
from django.dispatch import receiver
from django.http import JsonResponse
from accounts.models import User
from django.contrib.auth.decorators import login_required
from home.forms import ProfileDataForm
from home.models import UserCredit
from home.models import ProfileData, Profile
from django.core import serializers
from django.contrib import messages
import re


# some shortcut to call function

'''
GetSavedData = ExtratingSavedFile(request)------get saved search queries

'''

def ExtratingSavedFile(request):
    if request.user.is_authenticated:
        UserId=request.user.id
        UserSavedFile = ProfileData.objects.filter(user_id=UserId)

        return UserSavedFile


#  ------------------------to get what search quesries has been saved by user
def savedSearchQueries(request):
    UserId=request.user.id
    SearchValue=ProfileData.objects.filter(user_id=UserId)
    # data = serializers.serialize("json", SearchValue)
    telt=[]
    id=[]
    for k in SearchValue:
        telt.append(k.SaveTitle)
        id.append(k.id)
    dictionary = dict(zip(id, telt))
    return dictionary

# @login_required(redirect_field_name=None, login_url='dashboard')
def dashboard(request):
    if request.user.is_authenticated:
        UserId=request.user.id
        UserName=request.user
        filter2 = ProfileData.objects.filter(user_id=UserId)
        return render(request,'html/dashboard.html', {'filter2':filter2,'UserName1':UserName})

def company(request):
    if request.user.is_authenticated:
        UserId=request.user.id
        filter2 = ProfileData.objects.filter(user_id=UserId)
        return render(request,'html/companies.html',{'filter2':filter2})

def contact(request):
    if request.user.is_authenticated:
        UserId=request.user.id
        filter2 = ProfileData.objects.filter(user_id=UserId)
        return render(request,'html/contact.html',{'filter2':filter2})


def SuggestProject(request):
    if 'fn' in request.GET:
        fn = request.GET.get('fn')
        filter = Client.objects.filter(Q(Q(First_Name__icontains=fn) | Q(Company__icontains=fn)))
        titles = list()
        for product in filter:
            titles.append(product.title)
            return JsonResponse(titles, safe=False)
        return render(request,'html/dashboard.html')
        


def searchany(request):
    GetSavedData = ExtratingSavedFile(request)
    if request.method == 'POST':
        fn = request.POST.get('fn')
        request.session['fn'] = fn
        request.session['page_show']=10
        request.session['page']=1
        page_show=10
        
        if len(fn)==0:
            return render(request, 'html/dashboard.html',{'filter2':GetSavedData})
        else:
            filter = Client.objects.filter(Q(Q(First_Name__icontains=fn) | Q(Company__icontains=fn)))
            filter_count= filter.count()
            paginator = Paginator(filter, page_show)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'html/contact.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})

    if request.method == "GET":
        if request.GET.get('page_show'):
            request.session['page_show'] = request.GET.get('page_show')
        else:
            pass
        if request.GET.get('page'):
            request.session['page']=request.GET.get('page')
        else:
            pass
        if request.GET.get('selected'):
            request.session['page_show'] = request.GET.get('selected')
        else:
            pass
    
        page_number=request.session['page']
        page_show=request.session['page_show']
        fn=request.session['fn'] 
        filter = Client.objects.filter(Q(Q(First_Name__icontains=fn) | Q(Company__icontains=fn)))
        filter_count= filter.count()
        paginator = Paginator(filter, page_show)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'html/contact.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})


def SearchComp(request):
    GetSavedData = ExtratingSavedFile(request)
    if request.method == 'POST':
        fn = request.POST.get('fn')
        request.session['fn'] = fn
        request.session['page_show']=10
        request.session['page']=1
        page_show=10
        if len(fn)==0:
            return render(request, 'html/companies.html')
        else:
            filter = Client.objects.filter(Q(Q(First_Name__icontains=fn) | Q(Company__icontains=fn)))
            filter_count= filter.count()
            paginator = Paginator(filter, page_show)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'html/companies.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})

    if request.method == "GET":
        if request.GET.get('page_show'):
            request.session['page_show'] = request.GET.get('page_show')
        else:
            pass
        if request.GET.get('page'):
            request.session['page']=request.GET.get('page')
        else:
            pass
        if request.GET.get('selected'):
            request.session['page_show'] = request.GET.get('selected')
        else:
            pass
        page_number=request.session['page']
        page_show=request.session['page_show']
        fn=request.session['fn'] 
        filter = Client.objects.filter(Q(Q(First_Name__icontains=fn) | Q(Company__icontains=fn)))
        filter_count= filter.count()
        paginator = Paginator(filter, page_show)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'html/companies.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})


@receiver(notification)
def show_notification(sender, request, **kwargs):
    return render(request,'html/dashboard_lead.html')


def Client_top(request):
    GetSavedData = ExtratingSavedFile(request)
    if request.method == 'POST':
        fn = request.POST.get('fn')
        Company = request.POST.get('company')
        Title = request.POST.getlist('title[]')
        Function = request.POST.getlist('function[]')
        CompanySize = request.POST.getlist('CS[]')
        Level = request.POST.getlist('CL[]')
        Industry = request.POST.get('industry')
        Geography = request.POST.get('geography')

        request.session['fn'] = fn
        request.session['Company'] = Company
        request.session['Title'] = Title
        request.session['Function'] = Function
        request.session['CompanySize'] = CompanySize
        request.session['Level'] = Level
        request.session['Industry'] = Industry
        request.session['Geography'] = Geography

        request.session['page_show']=10
        request.session['page']=1
        page_show=10
        
        if len(fn)==len(Company)==len(Company)==len(Title)==len(Function)==len(CompanySize)==len(Level)==len(Geography)==0:
            return render(request, 'html/contact.html',{'filter2':GetSavedData})
        else:

            Title_qs = Q()
            for Ttl in Title:
                Title_qs = Title_qs | Q(Level=Ttl)
            Function_qs = Q()
            for sec in Function:
                Function_qs = Function_qs | Q(Q(Secondary_Department=sec) | Q(Primary_Department=sec))
            CompanySize_qs = Q()
            for CS in CompanySize:
                CompanySize_qs = CompanySize_qs | Q(Company_Headcount=CS)
            Level_qs = Q()
            for Lvl in Level:
                Level_qs = Level_qs | Q(Level=Lvl)
            
            filter = Client.objects.filter(Title_qs & Function_qs & CompanySize_qs & Level_qs & Q(First_Name__icontains=fn) & Q(Company__icontains=Company) & Q(Industry__icontains=Industry) & Q(Country__icontains=Geography))
            filter_dis=filter.distinct()
            filter_count= filter.count()
            paginator = Paginator(filter, page_show)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'html/contact.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})

    if request.method == "GET":
        if request.GET.get('page_show'):
            request.session['page_show'] = request.GET.get('page_show')
        else:
            pass
        if request.GET.get('page'):
            request.session['page']=request.GET.get('page')
        else:
            pass
        if request.GET.get('selected'):
            request.session['page_show'] = request.GET.get('selected')
        else:
            pass
    
        page_number=request.session['page']
        page_show=request.session['page_show']
        fn=request.session['fn'] 
        Company=request.session['Company']
        Title=request.session['Title'] 
        Function=request.session['Function'] 
        CompanySize=request.session['CompanySize']
        Level=request.session['Level'] 
        Industry=request.session['Industry']
        Geography=request.session['Geography']

        Title_qs = Q()
        for Ttl in Title:
            Title_qs = Title_qs | Q(Level=Ttl)
        Function_qs = Q()
        for sec in Function:
            Function_qs = Function_qs | Q(Q(Secondary_Department=sec) | Q(Primary_Department=sec))
        CompanySize_qs = Q()
        for CS in CompanySize:
            CompanySize_qs = CompanySize_qs | Q(Company_Headcount=CS)
        Level_qs = Q()
        for Lvl in Level:
            Level_qs = Level_qs | Q(Level=Lvl)

        filter = Client.objects.filter(Title_qs & Function_qs & CompanySize_qs & Level_qs & Q(First_Name__icontains=fn) & Q(Company__icontains=Company) & Q(Industry__icontains=Industry) & Q(Country__icontains=Geography)) 
        paginator = Paginator(filter, page_show) # Show 25 contacts per page.
        page_obj = paginator.get_page(page_number)
        filter_count= filter.count()
        return render(request, 'html/contact.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})



def Client_acc(request):
    GetSavedData = ExtratingSavedFile(request)
    if request.method == 'POST':
        Company = request.POST.get('company')
        Function = request.POST.getlist('function[]')
        CompanySize = request.POST.getlist('CS[]')
        Industry = request.POST.get('industry')
        Geography = request.POST.get('geography')
#-------------------------starting search sesion------------------------
        request.session['Company'] = Company
        request.session['Function'] = Function
        request.session['CompanySize'] = CompanySize
        request.session['Industry'] = Industry
        request.session['Geography'] = Geography
        request.session['page_show']=10
        request.session['page']=1
        page_show=10
        

        if len(Company)==len(Industry)==len(Function)==len(CompanySize)==len(Geography)==0:
            return render(request, 'html/companies.html')
        else: 
            Function_qs = Q()
            for sec in Function:
                Function_qs = Function_qs | Q(Q(Secondary_Department=sec) | Q(Primary_Department=sec))
            CompanySize_qs = Q()
            for CS in CompanySize:
                CompanySize_qs = CompanySize_qs | Q(Company_Headcount=CS)

            

            filter = Client.objects.filter(Function_qs & CompanySize_qs & Q(Company__icontains=Company) & Q(Industry__icontains=Industry) & Q(Country__icontains=Geography))
            filter_dis=filter.distinct()
            filter_count= filter.count()
            paginator = Paginator(filter, page_show)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'html/companies.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})

    if request.method == "GET":
        if request.GET.get('page_show'):
            request.session['page_show'] = request.GET.get('page_show')
        else:
            pass
        if request.GET.get('page'):
            request.session['page']=request.GET.get('page')
        else:
            pass
        if request.GET.get('selected'):
            request.session['page_show'] = request.GET.get('selected')
        else:
            pass
        
        page_number=request.session['page']
        page_show=request.session['page_show']
        Company=request.session['Company']
        Function=request.session['Function'] 
        CompanySize=request.session['CompanySize']
        Industry=request.session['Industry']
        Geography=request.session['Geography']    
        Function_qs = Q()
        for sec in Function:
            Function_qs = Function_qs | Q(Q(Secondary_Department=sec) | Q(Primary_Department=sec))
        CompanySize_qs = Q()
        for CS in CompanySize:
            CompanySize_qs = CompanySize_qs | Q(Company_Headcount=CS)
        
        filter = Client.objects.filter(Function_qs & CompanySize_qs & Q(Company__icontains=Company) & Q(Industry__icontains=Industry) & Q(Country__icontains=Geography)) 
        paginator = Paginator(filter, page_show) # Show 25 contacts per page.
        page_obj = paginator.get_page(page_number)
        filter_count= filter.count()
        return render(request, 'html/companies.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})
        
def reply(request):
    if request.method=='POST':
        data = request.POST['id']
        page_number=request.session['page']
        DataCount=len(data)
        UserId=request.user.id
        IdData = UserCredit.objects.get(user_id=UserId)
        credit=IdData.DefaultCredit
        if DataCount <= credit:
            LaodUserData=IdData.DownloadedContacts
            contactdata=LaodUserData+','+data
            dataLeft=int(credit)-int(DataCount)
            IdData.DefaultCredit=dataLeft
            IdData.DownloadedContacts=contactdata
            IdData.save()
            value = Client.objects.get(id=data)
            email=value.Email
            phone=value.Company_Number
            filter2=savedSearchQueries(request)
            context={'email':email, 'phone':phone,'reply':'ok','filter2':filter2}
            return JsonResponse(context)
        else:
            context={'not':'not'}
            return JsonResponse(context)
            
def Clinet_save(request):
    GetSavedData = ExtratingSavedFile(request)
    if request.method == 'POST':
        page_number=request.session['page']
        data = request.POST.getlist('checks[]')
        if len(data)!=0:
            DataInString = ','.join(data)
            DataCount=len(data)
            print(DataCount)
            page_number=request.session['page']
            UserId=request.user.id
            IdData = UserCredit.objects.get(user_id=UserId)
            credit=IdData.DefaultCredit
            if DataCount <= credit:
                LaodUserData=IdData.DownloadedContacts
                contactdata=LaodUserData+','+DataInString
                dataLeft=int(credit)-int(DataCount)
                IdData.DefaultCredit=dataLeft
                IdData.DownloadedContacts=contactdata
                IdData.save()
                product = Client.objects.filter(id__in=data)
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="file_1.csv"'
                writer = csv.writer(response)
                writer.writerow(['First_Name', 'Last_Name', 'Email'])
                for obj in product:
                    writer.writerow([obj.First_Name, obj.Last_Name, obj.Email])
                return response
            else:
                page_number=request.session['page']
                page_show=request.session['page_show']
                Company=request.session['Company']
                Function=request.session['Function'] 
                CompanySize=request.session['CompanySize']
                Industry=request.session['Industry']
                Geography=request.session['Geography']    
                Function_qs = Q()
                for sec in Function:
                    Function_qs = Function_qs | Q(Q(Secondary_Department=sec) | Q(Primary_Department=sec))
                CompanySize_qs = Q()
                for CS in CompanySize:
                    CompanySize_qs = CompanySize_qs | Q(Company_Headcount=CS)
                
                filter = Client.objects.filter(Function_qs & CompanySize_qs & Q(Company__icontains=Company) & Q(Industry__icontains=Industry) & Q(Country__icontains=Geography)) 
                paginator = Paginator(filter, page_show) # Show 25 contacts per page.
                page_obj = paginator.get_page(page_number)
                filter_count= filter.count()
                messages.error(request, 'You do not have enough credit')
                return render(request, 'html/companies.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})
        else:
                page_number=request.session['page']
                page_show=request.session['page_show']
                Company=request.session['Company']
                Function=request.session['Function'] 
                CompanySize=request.session['CompanySize']
                Industry=request.session['Industry']
                Geography=request.session['Geography']    
                Function_qs = Q()
                for sec in Function:
                    Function_qs = Function_qs | Q(Q(Secondary_Department=sec) | Q(Primary_Department=sec))
                CompanySize_qs = Q()
                for CS in CompanySize:
                    CompanySize_qs = CompanySize_qs | Q(Company_Headcount=CS)
                
                filter = Client.objects.filter(Function_qs & CompanySize_qs & Q(Company__icontains=Company) & Q(Industry__icontains=Industry) & Q(Country__icontains=Geography)) 
                paginator = Paginator(filter, page_show) # Show 25 contacts per page.
                page_obj = paginator.get_page(page_number)
                filter_count= filter.count()
                return render(request, 'html/companies.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})



    if request.method == "GET":
        if request.GET.get('page_show'):
            request.session['page_show'] = request.GET.get('page_show')
        else:
            pass
        if request.GET.get('page'):
            request.session['page']=request.GET.get('page')
        else:
            pass
        if request.GET.get('selected'):
            request.session['page_show'] = request.GET.get('selected')
        else:
            pass
        
        page_number=request.session['page']
        page_show=request.session['page_show']
        Company=request.session['Company']
        Function=request.session['Function'] 
        CompanySize=request.session['CompanySize']
        Industry=request.session['Industry']
        Geography=request.session['Geography']    
        Function_qs = Q()
        for sec in Function:
            Function_qs = Function_qs | Q(Q(Secondary_Department=sec) | Q(Primary_Department=sec))
        CompanySize_qs = Q()
        for CS in CompanySize:
            CompanySize_qs = CompanySize_qs | Q(Company_Headcount=CS)
        
        filter = Client.objects.filter(Function_qs & CompanySize_qs & Q(Company__icontains=Company) & Q(Industry__icontains=Industry) & Q(Country__icontains=Geography)) 
        paginator = Paginator(filter, page_show) # Show 25 contacts per page.
        page_obj = paginator.get_page(page_number)
        filter_count= filter.count()
        return render(request, 'html/companies.html',{'filters':page_obj,'filter_count':filter_count,'filter2':GetSavedData})


def SaveSearch(request):
    if request.method == 'POST':
        obj=ProfileData()
        obj.SaveTitle = request.POST['savename']
        saveField = request.POST.getlist('checks[]')
        obj.save()
        return HttpResponse("you dont have password")
    else:
        return HttpResponse("nothing")






def SaveSearchResult(request):
    if request.method == 'POST':
        CheckBox = request.POST.getlist('ChecBox[]')
        Name= request.POST.get('name')
        form = ProfileDataForm()
        data={'SaveTitle':Name,
            'SaveField':CheckBox,}

        form = ProfileDataForm(data)
        if form.is_valid():
            obj = ProfileData()
            obj.SaveTitle = Name
            obj.SaveField = CheckBox
            obj.user = request.user
            obj.save()

        if request.user.is_authenticated:
            UserId=request.user.id
            SearchValue=ProfileData.objects.filter(user_id=UserId)
            # data = serializers.serialize("json", SearchValue)
            telt=[]
            id=[]
            for k in SearchValue:
                telt.append(k.SaveTitle)
                id.append(k.id)
            dictionary = dict(zip(id, telt))
            context={'reply':'ok','filter2':dictionary}
            return JsonResponse(context, content_type="application/json")

def CompanySave(request):
    UserId=request.user.id
    filter2 = ProfileData.objects.filter(user_id=UserId)
    if request.method == 'POST':
        SaveValues = request.POST.getlist('SaveValues[]')
        request.session['page_show']=10
        request.session['page']=1
        page_show=10
        filter2 = ProfileData.objects.filter(id=SaveValues[0])
        for i in filter2:
            lebra=i.SaveField
        listvalue=[int(s) for s in re.findall(r'\b\d+\b', lebra)]
        request.session['listvalue'] = listvalue
        filter = Client.objects.filter(pk__in=listvalue)
        filter_dis=filter.distinct()
        filter_count= filter.count()
        paginator = Paginator(filter, page_show)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'html/companies.html',{'searchdance':page_obj,'filter_count':filter_count,'filter2':filter2})
    if request.method == "GET":
        if request.GET.get('page_show'):
            request.session['page_show'] = request.GET.get('page_show')
        else:
            pass
        if request.GET.get('page'):
            request.session['page']=request.GET.get('page')
        else:
            pass
        if request.GET.get('selected'):
            request.session['page_show'] = request.GET.get('selected')
        else:
            pass
        page_number=request.session['page']
        page_show=request.session['page_show']
        listvalue=request.session['listvalue']
        filter = Client.objects.filter(pk__in=listvalue)
        paginator = Paginator(filter, page_show) # Show 25 contacts per page.
        page_obj = paginator.get_page(page_number)
        filter_count= filter.count()

        dataDictionary = { 
            'hello': 'World', 
            'geeks': 'forgeeks', 
            'ABC': 123,
            456: 'abc', 
            14000605: 1, 
            'list': ['geeks', 4, 'geeks'], 
            'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
            }
        dataJSON = dumps(dataDictionary) 
        return render(request, 'html/companies.html',{'searchdance':page_obj,'filter_count':filter_count,'filter2':filter2,'data3': dataJSON})


def ContactSave(request):
    UserId=request.user.id
    filter2 = ProfileData.objects.filter(user_id=UserId)
    if request.method == 'POST':
        SaveValues = request.POST.getlist('SaveValues[]')
        request.session['page_show']=10
        request.session['page']=1
        page_show=10
        filter2 = ProfileData.objects.filter(id=SaveValues[0])
        for i in filter2:
            lebra=i.SaveField
        listvalue=[int(s) for s in re.findall(r'\b\d+\b', lebra)]
        request.session['listvalue'] = listvalue
        filter = Client.objects.filter(pk__in=listvalue)
        filter_dis=filter.distinct()
        filter_count= filter.count()
        paginator = Paginator(filter, page_show)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'html/contact.html',{'searchdance':page_obj,'filter_count':filter_count,'filter2':filter2})
    if request.method == "GET":
        if request.GET.get('page_show'):
            request.session['page_show'] = request.GET.get('page_show')
        else:
            pass
        if request.GET.get('page'):
            request.session['page']=request.GET.get('page')
        else:
            pass
        if request.GET.get('selected'):
            request.session['page_show'] = request.GET.get('selected')
        else:
            pass
        page_number=request.session['page']
        page_show=request.session['page_show']
        listvalue=request.session['listvalue']
        filter = Client.objects.filter(pk__in=listvalue)
        paginator = Paginator(filter, page_show) # Show 25 contacts per page.
        page_obj = paginator.get_page(page_number)
        filter_count= filter.count()
        return render(request, 'html/contact.html',{'searchdance':page_obj,'filter_count':filter_count,'filter2':filter2})

def SavedSearchUpdate(request):
     if request.method == 'POST':
        SaveChecBox = request.POST.getlist('SaveChecBox[]')

        if 'on' in SaveChecBox:
            SaveChecBox.remove('on')
        saveId = request.POST.getlist('saveId')
        val=saveId[0]
        DatabaseData=ProfileData.objects.get(id=val)
        piks=str(DatabaseData)
        stringFormat=piks.replace("'", '')
        databaseList = stringFormat.strip('][').split(', ')
        data=SaveChecBox+databaseList
        dataFilter=list(set(data)) 
        DatabaseData.SaveField = dataFilter
        DatabaseData.save()
        context={'SaveChecBox':SaveChecBox,'saveId':saveId}
        return JsonResponse(context)



def WindowsLoadData(request):
    if request.method=='POST':
        UserId=request.user.id
        IdData = UserCredit.objects.get(user_id=UserId)
        # credit=IdData.DefaultCredit
        LaodUserData=IdData.DownloadedContacts

        IncomingId = request.POST.getlist('id[]')
        id=[]
        for k in IncomingId:
            if k in LaodUserData:
                id.append(k)
        UserEmail=[]
        UserPhoneNumber=[]
        value = Client.objects.filter(pk__in=id)
        for i in range(len(id)):
            UserEmail.append(value[i].Email)
            UserPhoneNumber.append(value[i].Company_Number)
        test_dict = dict(zip(UserEmail, UserPhoneNumber))
        res = {}
        for key, ele in zip(id, test_dict.items()): 
            res[key] = dict([ele]) 
        context={'res':res,'reply':'ok'}
        return JsonResponse(context)


