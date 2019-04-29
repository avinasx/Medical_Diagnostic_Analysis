from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="juxt"
)

mycursor = mydb.cursor()

mycursor = mydb.cursor()
    #mycursor1 = mydb.cursor()
mycursor.execute("USE juxt")
    
mycursor.execute("SELECT DISTINCT disorder FROM t1 WHERE diagnostic = 'p1' AND disorder IN (SELECT disorder FROM t1 tb1 JOIN t1 tb2 USING( disorder ) WHERE tb1.proce = 'x1' AND tb2.proce = 'x2')")

y=[''.join(y) for y in mycursor]
          
    
mycursor.execute("SELECT DISTINCT patientID FROM t1 WHERE diagnostic = 'p1' AND PatientID IN (SELECT PatientID FROM t1 tb1 JOIN t1 tb2 USING( PatientID ) WHERE tb1.proce = 'x1' AND tb2.proce = 'x2')")

y=y+[''.join(str(x)) for x in mycursor]

def index(request):
    #return HttpResponse("Hello Doctors, let us do all the digostics for you!!!")
    return render(request, 'app/index.html')


def test(request):
    template = loader.get_template("app/test.html")
    return HttpResponse(template.render)


    
    