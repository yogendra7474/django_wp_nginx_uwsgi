def Client_top(request):
    if request.method == 'POST':
        
        fn = request.POST.get('fn')
        company = request.POST['company']
        title = request.POST['title']
        secdept = request.POST.getlist('checks[]')
        CompanySize = request.POST.getlist('CS[]')
        Level = request.POST.getlist('CL[]')
        industry = request.POST['industry']
        Company_Revenue = request.POST['Company_Revenue']
        geography = request.POST['geography']

        Level_qs = Q()
        for cl in Level:
            Level_qs = Level_qs | Q(Level=cl)

        CompanySize_qs = Q()
        for cs in CompanySize:
            CompanySize_qs = CompanySize_qs | Q(Company_Headcount=cs)

        my_filter_qs = Q()
        for sec in secdept:
            my_filter_qs = my_filter_qs | Q(Q(Secondary_Department=sec) | Q(Primary_Department=sec))
            
        filter = Client.objects.filter(Level_qs & CompanySize_qs & my_filter_qs & Q(First_Name__icontains=fn) & Q(Industry__icontains=industry) & Q(Company_Revenue__icontains=Company_Revenue) & Q(Country__icontains=
        geography))

        print(filter)
        tak=Client.objects.all()
        print(tak)

        paginator = Paginator(filter, 10)
        page_num = request.GET.get('page')
        # print(page_num)
        page_obj = paginator.get_page(page_num)
        print(page_obj)



        return render(request, 'html/dashboard.html',{'filters':page_obj})



















        def Client_top(request):
        
    fn = request.POST.get('fn')
    company = request.POST.get('company')
    title = request.POST.get('title')
    secdept = request.POST.getlist('checks[]')
    CompanySize = request.POST.getlist('CS[]')
    Level = request.POST.getlist('CL[]')
    industry = request.POST.get('industry')
    Company_Revenue = request.POST.get('Company_Revenue')
    geography = request.POST.get('geography')

    pass

    Level_qs = Q()
    for cl in Level:
        Level_qs = Level_qs | Q(Level=cl)

    CompanySize_qs = Q()
    for cs in CompanySize:
        CompanySize_qs = CompanySize_qs | Q(Company_Headcount=cs)

    my_filter_qs = Q()
    for sec in secdept:
        my_filter_qs = my_filter_qs | Q(Q(Secondary_Department=sec) | Q(Primary_Department=sec))
        
    filter = Client.objects.filter(Level_qs & CompanySize_qs & my_filter_qs & Q(First_Name__icontains=fn) & Q(Industry__icontains=industry) & Q(Company_Revenue__icontains=Company_Revenue) & Q(Country__icontains=geography))


    paginator = Paginator(filter, 10)
    page_num = request.GET.get('page')
    # print(page_num)
    page_obj = paginator.get_page(page_num)
    print(page_obj)



    return render(request, 'html/dashboard.html',{'filters':page_obj})















    def Client_top(request):
    fn=request.GET['fn']
    Level = request.POST.getlist('CL[]')

    Level_qs = Q()
    for cl in Level:
        Level_qs = Level_qs | Q(Level=cl)

    filter = Client.objects.all()
    queryset_list = filter.filter(Level_qs & Q(First_Name__icontains=fn))

    page_request_var = "page"
    page = request.GET.get(page_request_var)
    paginator = Paginator(queryset_list, 10)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
        
    return render(request, 'html/dashboard.html',{'filters':queryset})
















    <!-- <div class="">
                  <table id="myTable">
                    <thead>
                      <th>All</th>
                        <th>Name</th>
                        <th>Company</th>
                        <th>Email | Phone Number</th>
                        <th>Company ddress</th>
                        <th>Delverabilty</th>
                    </thead>
                    {% for user in filters %}
                    <tbody>
                      <tr>
                        <td><input type="checkbox" name="checks[]"  id="clinet[]" value="{{user.id}}"></td>
                        <td>{{ user.First_Name}} {{ user.Last_Name}}</td>
                        <td>{{ user.Company}}, {{ user.City}},
                          {{ user.State}}</td>
                        <td>{{ user.Email}},
                            {{ user.Company_Number}}</td>
                        <td>{{ user.Address}}</td>
                        <td>{{ user.Email_Confidence}}</td>
                      </tr>
                    </tbody>
                    {% endfor %}
                  </table>
                
                  
                  <div class="search-result-title">
                    <div class="srcheck">All</div>
                    <div class="srname">Name</div>
                    <div class="srcompany">Company</div>
                    <div class="srep">Email | Phone Number</div>
                    <div class="srcd">Company ddress</div>
                    <div class="srdel">Delverabilty</div>
                  </div>
                  {% for user in filters %}
                  <div class="SearchResult">
                    <div class="srcheck1"><input type="checkbox" name="checks[]"  id="clinet[]" value="{{user.id}}"></div>
                    <div class="srname1">{{ user.First_Name}} {{ user.Last_Name}}</div>
                    <div class="srcompany1">{{ user.Company}}, {{ user.City}},
                      {{ user.State}}
                    </div>
                    <div class="srep1">{{ user.Email}},
                      {{ user.Company_Number}}
                    </div>
                    <div class="srcd1">{{ user.Address}}</div>
                    <div class="srdel1">{{ user.Email_Confidence}}</div>
                  </div>
                  {% endfor %}
                </div> -->