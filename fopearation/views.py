from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import FileOperation
# Create your views here.
def fileupload(request):
   return  render(request,"fileupload.html")

def view_details(request):
    filedata = FileOperation.objects.all()
    #data=pd.read_csv(filedata.csv_file)
    return  render(request,"view.html",{'filedata':filedata})
    #return render(request,'view.html',data)

def upload(request):
   file=request.FILES['file1']
   #file1=request.POST['file1']
   FileOperation.objects.create(name=file,csv_file=file)
   #FileOperation.csv_file=file
   return  render(request,"fileupload.html")

def display(request,fid):
   data = FileOperation.objects.get(id=fid)
   f=data.csv_file
   fdata=pd.read_csv(f)
  # fdata.head()
   fdata.head().to_html("fopearation/templates/output.html")
   #return HttpResponse(fdata)
   return  render(request,"output.html",{'data':data})

def displayhist(request,fid):
   data = FileOperation.objects.get(id=fid)
   f=data.csv_file
   fdata=pd.read_csv(f)
   fdata.head().to_html("fopearation/templates/output.html")
   #return HttpResponse(fdata)
   return  render(request,"display.html",{'kdata':data})
   


