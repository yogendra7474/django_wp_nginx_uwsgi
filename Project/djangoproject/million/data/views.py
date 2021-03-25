from django.shortcuts import render

# Create your views here.
import csv, io
from django.shortcuts import render, redirect
from data.models import Client
from django.contrib.auth.decorators import permission_required
from django.contrib import messages


@permission_required('admin.can_add_log_entry')

def data(request):
	template = "html/data.html"
	prompt = {
		'order': 'order of the CSV should be '
	}

	if request.method == "GET":
		return render(request, template, prompt)

	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'This is not a csv file')

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		_, created = Client.objects.update_or_create(
			First_Name=column[0],
			Last_Name=column[1],
			Company=column[2],
			Website=column[3],
			Title=column[4],
			Email=column[5],
			Email_Confidence=column[6],
			Address=column[7],
			Primary_Department=column[8],
			Secondary_Department=column[9],
			Level=column[10],
			Street=column[11],
			City=column[12],
			State=column[13],
			Zip=column[14],
			Country=column[15],
			LinkedIn=column[16],
			Twitter=column[17],
			Facebook=column[18],
			Industry=column[19],
			Company_Headcount=column[20],
			Company_Revenue=column[21],
			Direct_Dial=column[22],
			Mobile_Number=column[23],
			Company_Number=column[24],
			Other_Number=column[25],
			Email_Encrypt=column[25],
			Mobile_Number_Encrypt=column[25],
		)
	context = {}
	return render(request, 'html/data.html',context)


