from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
#import mysql.connector #alternative to 'connection' from django.db



'''
#few examples of using my sql connection that is currently being used
mycursor = connection.cursor()
mycursor.execute("SELECT count(*) FROM people_person")
>>1L
row = cursor.fetchone()
print row
>>(12L,)
Person.objects.all().count()
>>12
'''

'''
#my sql connection using mysqlconnect an alternative
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="juxt",
  port=3306,
)
 #mycursor = mydb.cursor()
'''
diagnostic=''
proce ='x1 x2'


def patient(request):
    if request.method == 'POST':
        diagnostic = request.POST['diagnostic']
        proce = request.POST['proce']
        proce1,proce2 = proce.split(',', 1)
        proce1=str(proce1)
        proce2=str(proce2)
        
        #mycursor is a saviour for sql query in dzango
        mycursor = connection.cursor()
       
        mycursor.execute("Use juxt")
        
      
        #mycursor.execute("SELECT DISTINCT disorder FROM t1 WHERE diagnostic = 'p1' AND disorder IN (SELECT disorder FROM t1 tb1 JOIN t1 tb2 USING( disorder ) WHERE tb1.proce = 'x1' AND tb2.proce = 'x2')")
        mycursor.execute("SELECT DISTINCT disorder FROM t1 WHERE diagnostic = %s AND disorder IN (SELECT disorder FROM t1 tb1 JOIN t1 tb2 USING( disorder ) WHERE tb1.proce = %s AND tb2.proce = %s)",(diagnostic, proce1, proce2))
        y=[''.join(y) for y in mycursor]
          
        #mycursor.execute("SELECT DISTINCT patientID FROM t1 WHERE diagnostic = 'p1' AND PatientID IN (SELECT PatientID FROM t1 tb1 JOIN t1 tb2 USING( PatientID ) WHERE tb1.proce = 'x1' AND tb2.proce = 'x2')")
        mycursor.execute("SELECT DISTINCT patientID FROM t1 WHERE diagnostic = %s AND PatientID IN (SELECT PatientID FROM t1 tb1 JOIN t1 tb2 USING( PatientID ) WHERE tb1.proce = %s AND tb2.proce = %s)",(diagnostic, proce1, proce2))
        z=[''.join(str(x)) for x in mycursor]

        context= {
        'y': str(y),
        'z': str(z),
          }
        return render(request, 'app/patient.html', context)

        #return HttpResponse("<h2>disorders are<h2>"+str(y)+"<h2>PatientIds are<h2>"+str(z))



        #query part ends

def index(request):
    #return HttpResponse("Hello Doctors, let us do all the digostics for you!!!")
    return render(request, 'app/index.html')


def about(request):
    #return HttpResponse("Hello Doctors, let us do all the digostics for you!!!")
    return render(request, 'app/about.html')

#here are some data in disctionary are irrelavent, for testing purpose
def test(request):
  person= {'firstname': 'Craig', 'lastname': 'Daniels'}
  weather= "jk"
  context= {
        'weather': weather,
        'leather':"jk" 
          }
  return render(request, 'app/test.html', context)

    
    