'''Write a python program create csv file student.csv(sid,sname,city,contact) using 10 records 
(in which 5 records input directly and 5 records take input from user) write records into this file.
Read this file using csv module and print it. 
NOTE: Reading and writting must be perform using python script.'''

import csv
#create and write the records in csv file
with open("c://sqlite3//student_csv.csv","w",newline="")as stud:
    write=csv.writer(stud)
    #create header of a csv file
    header=['S_Id','S_Name','City','Contact']
    write.writerow(header)
    #5 record's insert directly in csv file
    rows=[
        [1,'Om','Sarbhon',1234567890],
        [2,'Sai','Bardoli',9876543210],
        [3,'Ram','Bardoli',564898321],
        [4,'Jai','Surat',1748523690],
        [5,'Shree','Vyara',9632587410]
        ]
    write.writerows(rows)
    print('Record Inserted successful')
    
    #5 records insert using user input
    #create empty list
    l=[]
    #iterate the loop for entering multiple records
    for record in range(5):
        n=int(input('Enter Student ID:'))
        name=input('Enter Student Name: ')
        city=input('Enter City Name: ')
        contact=int(input('Enter Contact Number:'))
        #append records in a variable 'store'
        store=[n,name,city,contact]
        #append the records in list
        l.append(store)
        #write the rows in a csv file
    write.writerows(l)
    print('Record Inserted successful')

with open("c://sqlite3//student_csv.csv","r")as stud:
    r=csv.DictReader(stud)
    for i in r:
        print(i)
print()
with open("c://sqlite3//student_csv.csv","r",newline="")as stud:
    #using read csv file using reader()
    read=csv.reader(stud)
    for i in read:
        print(i)
    
