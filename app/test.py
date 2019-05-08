import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()
#mycursor1 = mydb.cursor()
mycursor.execute("USE juxt")

mycursor.execute("SELECT DISTINCT disorder FROM t1 WHERE diagnostic = 'p1' AND disorder IN (SELECT disorder FROM t1 tb1 JOIN t1 tb2 USING( disorder ) WHERE tb1.proce = 'x1' AND tb2.proce = 'x2')")
for x in mycursor:
  print(x)

mycursor.execute("SELECT DISTINCT patientID FROM t1 WHERE diagnostic = 'p1' AND PatientID IN (SELECT PatientID FROM t1 tb1 JOIN t1 tb2 USING( PatientID ) WHERE tb1.proce = 'x1' AND tb2.proce = 'x2')")

for x in mycursor:
  print(x)