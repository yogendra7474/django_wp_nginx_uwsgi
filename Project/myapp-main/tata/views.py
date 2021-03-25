from django.db.models import Q
from data.models import Client
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db.models.functions import Concat
from django.db.models import Value
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required

from django.http import JsonResponse
#from djqscsv import render_to_csv_response



def tata(request):
    request.session.flush()

    return render(request,'html/tata.html')


def jj(request):
    request.session['ab']='name'
    if request.method == 'POST':
        # query1 = request.POST.getlist('checks[]')
        # print(query1)
        query2 = request.POST['fn']
        request.session['search'] = query2
        if len(query2)==0:
            return render(request, 'html/tata.html')

        else:
            filter=Client.objects.filter(First_Name__icontains=query2)
            paginator = Paginator(filter, 5) # Show 25 contacts per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            pa=request.session['ab']
            context={'filters':page_obj,'pa':pa }
            return render(request, 'html/tata.html',context)

    if request.method == 'GET':
        if 'search' in request.session:
            query_set = Client.objects.filter(myattribute__icontains=query2)
            paginator = Paginator(query_set, 1)
            page = request.GET.get('page')
            search = paginator.get_page(page)
            return render(request, 'html/tata.html',{'filters':search})
        else:
            return render(request, 'myapp/mytemplate.html')


def pix(request):
    if request .method=='POST':
        request.session.flush()
        query2 = request.POST.get('fn')
        request.session['query2'] = query2
        request.session['page_show']=10
        request.session['page']=1
        filter=Client.objects.filter(First_Name__icontains=query2)
        page_show=10
        paginator = Paginator(filter, page_show) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # emailfor=Client.objects.all()
        # id=[]
        # my_list=[]
        # for i in emailfor:
        #     my_list.append("xxx@" + str(i.Email).split('@')[1])
        #     id.append(str(i.id))
        
        # for k in id:
        #     emai=Client.objects.get(id=k)
        #     for j in my_list:
        #       emai.Email_Encrypt=j
        #       emai.Mobile_Number_Encrypt="xxxxxxxxx"
        #       emai.save()


        context={'filters':page_obj,'paginator':paginator}
        return render(request, 'html/tata.html',context)

    if request.method == 'GET':
        if request.GET.get('page_show'):
            request.session['page_show'] = request.GET.get('page_show')
        else:
            pass
        if request.GET.get('page'):
            request.session['page']=request.GET.get('page')
        else:
            pass

        page_number=request.session['page']
        page_show=request.session['page_show']
        query2 =request.session['query2']
        filter=Client.objects.filter(First_Name__icontains=query2)
        paginator = Paginator(filter, page_show) # Show 25 contacts per page.
        page_obj = paginator.get_page(page_number)

        context={'filters':page_obj}
        return render(request, 'html/tata.html',context)


def reply(request):
    if request.method=='POST':
        id = request.POST['id']
        print(type(id))
        print(id)
        value = Client.objects.get(id=id)
        email=value.Email
        phone=value.Company_Number
        print(email)
        print(phone)
        context={'email':email, 'phone':phone,'reply':'ok'}
        return JsonResponse(context)


