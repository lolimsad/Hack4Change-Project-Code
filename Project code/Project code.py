import mysql.connector
db = mysql.connector.connect(host = "localhost", user = "root", passwd = "ayoo", database = "hospital")
cur=db.cursor()

def insertdept():
    while True:
        depno = int(input("Enter department no.:"))
        depname = input("Enter department name:")
        no_do = int(input("Enter number of doctors in department:"))
        no_pn = int(input("Enter number of patients in department:"))
        no_bd = int(input("Enter number of empty beds in department:"))
        cur.execute(f"insert into deptinfo values({depno},'{depname}',{no_do},{no_pn},{no_bd})")
        db.commit()
        rep = input("Do you want to add more department records?\nEnter YES/NO\n")
        if rep in "NOno":
            break

def deldep():
    cur.execute("select * from deptinfo")
    records = cur.fetchall()
    s_ip = input("Enter 'no' for the department no. or 'name' for the department name.\n")
    if s_ip in "NOno":
        dno = int(input("Enter department no.:"))
        for i in records:
            if i[0]==dno:
                cur.execute(f"delete from deptinfo where deptno={dno}")
                db.commit()
                break
            else:
                print("Invalid department number.")
    elif s_ip in "nameNAME":
        dnam = input("Enter department name:")
        for i in records:
            if i[1]==dnam:
               cur.execute(f"delete from deptinfo where deptname={dnam}")
               db.commit()
               break
            else:
                print("Invalid department name.")
    else:
        print("Invalid output")
    
def depdocup():
    cur.execute(f"select * from deptinfo")
    records = cur.fetchall()
    dname = input("Enter the department name: ")
    for i in records:
        if i[1]==dname:
            nod = int(input("Enter updated no. of doctors: "))
            cur.execute(f"update deptinfo set no_doc={nod} where deptname='{dname}'")
            db.commit()
            break
        
def deppntup():
    cur.execute(f"select * from deptinfo")
    records = cur.fetchall()
    dname = input("Enter the department name: ")
    for i in records:
        if i[1]==dname:
            nop = int(input("Enter updated no. of patients: "))
            cur.execute(f"update deptinfo set no_pnt={nop} where deptname='{dname}'")
            db.commit()
            break
      
def depebdup():
    cur.execute(f"select * from deptinfo")
    records = cur.fetchall()
    dname = input("Enter the department name: ")
    for i in records:
        if i[1]==dname:
            nbd = int(input("Enter updated no. of empty beds: "))
            cur.execute(f"update deptinfo set nob={nbd} where deptname='{dname}'")
            db.commit()
            break
    
def updtdep():
    s_ip = int(input("Choose record to be updated:\n1.No. of Doctors\n2.No. of Patients\n3.No. of Empty beds\n"))
    if s_ip==1:
        depdocup()
    elif s_ip==2:
        deppntup()
    elif s_ip==3:
        depebdup()
    else:
        print("Invalid choice")

def searchdep():
    cur.execute("select * from deptinfo")
    records = cur.fetchall()
    dnm = input("Enter the department name: ")
    for i in records:
        if i[1]==dnm:
            print("Department no.",i[0],"\nDepartment Name:",i[1],"\nNo. of Doctors:",i[2],"\nNo. of patients:",i[3],"\nNo. of beds:",i[4])
    
def readdep():
    cur.execute("select * from deptinfo")
    records=cur.fetchall()
    for i in records:
        print(i[0],i[1],i[2],i[3],i[4])

def insertdoc():
    while True:
        docn = int(input("Enter doctor ID no.:"))
        docname = input("Enter the doctor's name:")
        depname = input("Enter department name:")
        doj = input("Enter the date of joining:")
        dol = input("Enter thr date of leaving:\nIf not applicable enter NA")
        dmob = int(input("Enter the doctor's no.:"))
        dmail = input("Enter the doctor's email ID:")
        cur.execute(f"insert into docinfo values({docn},'{docname}','{depname}','{doj}','{dol}',{dmob},'{dmail}')")
        db.commit()
        rep = input("Do you want to add more records?\nEnter YES/NO\n")
        if rep in "NOno":
            break

def deldoc():
    cur.execute("select * from docinfo")
    records = cur.fetchall()
    s_ip = input("Enter 'no' for the doctor ID no. or 'name' for the doctor's name.\n")
    if s_ip in "NOno":
        dno = int(input("Enter doctor ID no.:"))
        for i in records:
            if i[0]==dno:
                cur.execute(f"delete from docinfo where docno={dno}")
                db.commit()
                break
            else:
                print("Invalid doctor ID number.")
    elif s_ip in "nameNAME":
        dnam = input("Enter doctor's name:")
        for i in records:
            if i[1]==dnam:
               cur.execute(f"delete from docinfo where docname={dnam}")
               db.commit()
               break
            else:
                print("Invalid name.")
    else:
        print("Invalid output")

def updtdoc():
    cur.execute(f"select * from docinfo")
    records = cur.fetchall()
    dnum = input("Enter the doctor's ID no.: ")
    for i in records:
        if i[0]==dnum:
            dol = int(input("Enter updated date of leaving: "))
            cur.execute(f"update docinfo set dateleave={dol} where docno='{dnum}'")
            db.commit()
            break

def searchdoc():
    cur.execute("select * from docinfo")
    records = cur.fetchall()
    dnm = input("Enter the doctor's ID no.: ")
    for i in records:
        if i[0]==dnm:
            print("Doctor ID no.",i[0],"\nName:",i[1],"\nDepartment Name:",i[2],"\nDate of Joining:",i[3],"\nDate of leaving:",i[4],"\nMobile No.:",i[5],"\nEmail ID:",i[6])

def readdoc():
    cur.execute("select * from docinfo")
    records=cur.fetchall()
    for i in records:
        print(i[0],i[1],i[2],i[3],i[4],i[5],i[6])

def insertpnt():
    while True:
        print("Kindly enter 'NA' if the data is not applicable")
        pno = int(input("Enter patient ID no.:"))
        pname = input("Enter patient name:")
        pmob = int(input("Enter patient mobil no.:"))
        pgdn =input("Enter guardian name:")
        pgdr = input("Enter relation with patient:")
        amdt = input("Enter admit date:")
        dcdt = input("Enter discharge date:")
        amcas = input("Enter the cause for admitting:")
        depname = input("Enter the department name where the patient is admitted:")
        cur.execute(f"insert into pntinfo values({pno},'{pname},{pmob},'{pgdn}','{pgdr}','{amdt}','{dcdt}','{amcas}','{depname}')")
        db.commit()
        rep = input("Do you want to add more records?\nEnter YES/NO\n")
        if rep in "NOno":
            break

def delpnt():
    cur.execute("select * from pntinfo")
    records = cur.fetchall()
    s_ip = input("Enter 'no' for the patient ID no. or 'name' for the patient name.\n")
    if s_ip in "NOno":
        pno = int(input("Enter patient ID no.:"))
        for i in records:
            if i[0]==pno:
                cur.execute(f"delete from pntinfo where pntno={pno}")
                db.commit()
                break
            else:
                print("Invalid patient ID number.")
    elif s_ip in "nameNAME":
        pnam = input("Enter patient name:")
        for i in records:
            if i[1]==pnam:
               cur.execute(f"delete from pntinfo where pntname='{pnam}'")
               db.commit()
               break
            else:
                print("Invalid name.")
    else:
        print("Invalid input")

def gdup():
    cur.execute(f"select * from pntinfo")
    records = cur.fetchall()
    pnum = int(input("Enter the patient ID no.: "))
    for i in records:
        if i[0]==pnum:
            gdnm = input("Enter guardian's name: ")
            gdrl = input("Enter relation to patient: ")
            cur.execute(f"update pntinfo set pngdn='{gdnm}' where pntno={pnum}")
            cur.execute(f"update pntinfo set pngdr='{gdrl}' where pntno={pnum}")
            db.commit()
            break

def dcdtup():
    cur.execute(f"select * from pntinfo")
    records = cur.fetchall()
    pnum = int(input("Enter patient ID no.: "))
    for i in records:
        if i[0]==pnum:
            disd = input("Enter updated discharging date: ")
            cur.execute(f"update pntinfo set disdate='{disd}' where pntno={pnum}")
            db.commit()
            break

def updtpnt():
    up_c=int(input("Choose column to be updated:\n1.Guardian Details\n2.Discharging Date\n"))
    if up_c==1:
        gdup()
    elif up_c==2:
        dcdtup()
    else:
        print("Invalid choice.")

def searchpnt():
    cur.execute("select * from pntinfo")
    records = cur.fetchall()
    pnm = input("Enter the patient ID no.: ")
    for i in records:
        if i[0]==pnm:
            print("Patient ID no.",i[0],"\nPatient Name:",i[1],"\nMobile No.:",i[2],"\Guardian name:",i[3],"\nRelation:",i[4],"\nAdmit Date:",i[5],"\nDicharge Date:",i[6],"\nCause of Admitting:",i[7],"\nAdmitting Department",i[8])
def readpnt():
    cur.execute("select * from pntinfo")
    records=cur.fetchall()
    for i in records:
        print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])

def pntfunc():
    print("*********************PATIENT RECORDS************************")
    while True:
        c_no=int(input("Enter choice no.:\n1.Display all recordss\n2.Insert new record/s\n3.Search for a record\n4.Update a record\n5.Delete a record\n6.Exit from Patient Records"))
        if c_no==1:
            readpnt()
        elif c_no==2:
            insertpnt()
        elif c_no==3:
            searchpnt()
        elif c_no==4:
            updtpnt()
        elif c_no==5:
            delpnt()
        else:
            break

def docfunc():
    print("*********************DOCTOR RECORDS************************")
    while True:
        c_no=int(input("Enter choice no.:\n1.Display all recordss\n2.Insert new record/s\n3.Search for a record\n4.Update a record\n5.Delete a record\n6.Exit from Doctor Records"))
        if c_no==1:
            readdoc()
        elif c_no==2:
            insertdoc()
        elif c_no==3:
            searchdoc()
        elif c_no==4:
            updtdoc()
        elif c_no==5:
            deldoc()
        else:
            break

def depfunc():
    print("*********************DEPARTMENT RECORDS************************")
    while True:
        c_no=int(input("Enter choice no.:\n1.Display all recordss\n2.Insert new record/s\n3.Search for a record\n4.Update a record\n5.Delete a record\n6.Exit from Department Records"))
        if c_no==1:
            readdep()
        elif c_no==2:
            insertdept()
        elif c_no==3:
            searchdep()
        elif c_no==4:
            updtdep()
        elif c_no==5:
            deldep()
        else:
            break

print("*********************LAUGH OUT LOUD HOSPITAL************************") 
usnm=input("Enter Username:\n")
paswd=input("Enter Password:") 
if usnm=="admin" and paswd=='l5o3l4lolhospp':
    while True: 
        print("WELCOME")
        re=int(input("Enter Choice number to access:\n1.Department Records\n2.Doctor Records\n3.Patient Records\n4.Exit"))
        if re==1:
            depfunc()
        elif re==2:
            docfunc()
        elif re==3:
            pntfunc()
        else:
            print("Thankyou for visiting.")
            break
else:
    print("Invalid Username or Password\nPlease Try Again")
    exit
db.close()
