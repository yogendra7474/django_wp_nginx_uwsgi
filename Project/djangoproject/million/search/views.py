import csv
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from .filters import ClientFilter
from data.models import Client
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db.models.functions import Concat
from django.db.models import Value
#from djqscsv import render_to_csv_response



def search(request):
    myFilter = ClientFilter()
    return render(request,'html/base.html',{'myFilter': myFilter})


def Client_top(request):
    myFilter = ClientFilter()
    # if request.method == 'POST':
    Clients = Client.objects.all()
    myFilters = ClientFilter(request.POST, queryset=Clients)
    count_id = Client.objects.all().count()
    print(count_id)
    paginator = Paginator(myFilters.qs, 10)
    page_num = request.GET.get('page')
    print(page_num)
    page = paginator.get_page(page_num)
    #has_filter = any(field in request.GET for field in set(page.get_fields()))
    print(page)

    context = {'Clients': page, 'myFilter': myFilter, 'count_id': count_id}
    return render(request, 'html/search.html', context)
    # else:
    #     return HttpResponse("Page you are looking does not exist")



    
def Clinet_save(request):
    myFilter = ClientFilter()
    if request.method == 'POST':
        data = request.POST.getlist('checks[]')
        print(data)
        product = Client.objects.filter(Email__in=data)
        print(product)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file_1.csv"'
        writer = csv.writer(response)
        writer.writerow(['First_Name', 'Last_Name', 'Email'])
        for obj in product:
            writer.writerow([obj.First_Name, obj.Last_Name, obj.Email])
        return response
    else:
        HttpResponse("404 error")
