from django.http import HttpResponse
from django.shortcuts import render, redirect
from CSV_LOADER.models import csvfiles,csv_table
from django.db.models import Q
import csv
import datetime
import os
def index(request):
    if request.method == 'POST':
        csv_file = request.POST.get("csv_file", "")
        upload_date = datetime.datetime.now()
        csvfiles(name=csv_file, date_created=upload_date).save()
        criterion = Q(date_created=upload_date)
        csv_filename = csvfiles.objects.filter(criterion).values('name')
        pwd = os.path.dirname(__file__)
        data = {}
        with open(pwd + '/media/uploads/'+csv_filename[0]['name']) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for csvRow in csvReader:
                id = csvRow["size"]
                data[id] = csvRow

        print(data)
        return HttpResponse(pwd + '/media/uploads/'+csv_filename[0]['name'])
    else:
	    return render(request, 'index.html')