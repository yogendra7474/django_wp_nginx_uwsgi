from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Articles


def pagination_pro(request):

    return render(request, 'html/base.html')  


def pagination_p(request):
     if request.method == 'POST':
         print("raga")
         my_model = Articles.objects.all()
         number_of_item = 5
         paginatorr = Paginator(my_model, number_of_item)
         first_page = paginatorr.page(1).object_list
         page_range = paginatorr.page_range
         context = {'paginatorr':paginatorr,'first_page':first_page,'page_range':page_range}
         page_n = request.POST.get('page_n', None) #getting page number
         print("saga")
         results = list(paginatorr.page(page_n).object_list.values('id', 'title'))
         return JsonResponse({"results":results})
         return render(request, 'html/index.html',context)  