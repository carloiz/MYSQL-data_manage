import mysql.connector 
server = "localhost"
user = "root"
pasx = "your_password"
db = "records"
conn = mysql.connector.connect(host=server,username=user,password=pasx,database=db)

def b1():
    res_1 = input("\nDo you want to go Main?y/n: ")
    if res_1 == "y":
        main()
    elif res_1 == "n":
        print("\n====Program Exit====\n")
        exit()
    else:
        b1()

def Goto_(): # EDIT UPDATE LAST CALL
    u_idx = input("\nGo to Choose fields?y/n: ")
    if u_idx == "y":
        fields_1()
    elif u_idx == "n":
        un_r()
    else:
        Goto_()

def un_r(): # EDIT UPDATE LAST CALL 1
    u_idx1 = input("\nUpdate New Record?y/n: ")
    if u_idx1 == "y":
        UPDATERECORD()
    elif u_idx1 == "n":
        b1()
    else:
        un_r()

def s_2(): # DELETE LAST CALL
    u_idv1 = input("\nDelete Another Record Again?y/n: ")
    if u_idv1 == "y":
        DELETERECORD()
    elif u_idv1 == "n":
        b1()
    else:
        s_2()

def id_x(): # SEARCH LAST CALL
    res_1 = input("\nSearch Another?y/n: ")
    if res_1 == "y":
        SEARCHRECORD()
    elif res_1 == "n":
        b1()
    else:
        id_x()


def VIEWALLRECORD(): # VIEW ALL RECORD
    cursor=conn.cursor()
    selectquery = "select * from players order by ID desc"
    cursor.execute(selectquery)
    records=cursor.fetchall()
    print("\n\tNumber of Players:",cursor.rowcount)
    print("\t  ID  FirstName  LastName")
    for row in records:
        print("\t", row)
    b1()

def ADDNEWRECORD(): # ADD NEW RECORD
    f_n = input("\nEnter your First Name:")
    l_n = input("Enter your Last Name:")

    if f_n == "" or l_n == "":
        print("\n\tPlease Fill-up All Fields")
        ADDNEWRECORD()

    cursor=conn.cursor()
    s1 = "insert into players (firstname, lastname) values ('"+ f_n +"','"+ l_n +"')"   # ADD QUERY
    cursor.execute(s1)
    conn.commit()
    print("\nSuccessfully Added: "+ f_n +" "+ l_n +"")

    cursor=conn.cursor()
    selectquery = "select * from players order by ID desc limit 5"
    cursor.execute(selectquery)
    records=cursor.fetchall()
    print("\nNumber of Players:",cursor.rowcount)
    print("ID  Firstname  Lastname")
    for row in records:
        print(row)
    def bx():
        res_2 = input("\nDo you want Add New Record Again?y/n: ")
        if res_2 == "y":
            ADDNEWRECORD()
        elif res_2 == "n":
            b1()
        else:
            bx()
    bx()

def UPDATERECORD():   # EDIT/UPDATE RECORD
    u_n = input("\nEnter First Name: ")
    cursor=conn.cursor()
    selectquery = "select * from players where firstname like '%"+ u_n +"%'"
    cursor.execute(selectquery)
    records=cursor.fetchall()
    a2 = ["ID Numbers Available"]   # Declared First the Variable
    print("\nID\tFirstname\tLastname")
    for row in records:
        print(row)
        a2 = a2
        a2.append(row[0]) # Adding ID numbers in Database

    a1 = str(records)
    if a1 == "[]":
        print("No Record Found!")
        UPDATERECORD()
 
    def edit_2():
        print("\nID Numbers Available: ", a2[1:])
        global u_id3
        u_id3 = input("\nEnter ID Number: ")
        if not int(u_id3) in a2[1:]:        # Comparing Input ID number to ID numbers Filtered
            edit_2()
    edit_2()

    def fn1_(): # Edit Only First Name
        fn1 = input("\nInput New First Name: ")
        if fn1 == "":
            fn1_()
        cursor=conn.cursor()
        selectquery = "select * from players where ID = '"+ u_id3 +"'"
        cursor.execute(selectquery)
        records1=cursor.fetchall()                                        
        for row1 in records1:
            print("\n\tOld Record:",row1)

        cursor=conn.cursor()
        s1 = "update players set firstname = '"+ fn1 +"' where ID = '"+ u_id3 +"'"
        cursor.execute(s1)
        conn.commit()

        cursor=conn.cursor()
        selectquery = "select * from players where ID = '"+ u_id3 +"'"
        cursor.execute(selectquery)
        records2=cursor.fetchall()                                        
        for row2 in records2:
            print("\tUpdated Record:",row2)
        Goto_()

    def ln1_(): # Edit Only Last Name
        ln1 = input("\nInput New Last Name: ")
        if ln1 == "":
            ln1_()
        cursor=conn.cursor()
        selectquery = "select * from players where ID = '"+ u_id3 +"'"
        cursor.execute(selectquery)
        records1=cursor.fetchall()                                        
        for row1 in records1:
            print("\n\tOld Record:",row1)

        cursor=conn.cursor()
        s1 = "update players set lastname = '"+ ln1 +"' where ID = '"+ u_id3 +"'"
        cursor.execute(s1)
        conn.commit()

        cursor=conn.cursor()
        selectquery = "select * from players where ID = '"+ u_id3 +"'"
        cursor.execute(selectquery)
        records2=cursor.fetchall()                                        
        for row2 in records2:
            print("\tUpdated Record:",row2)    
        Goto_()

    def fln1_(): # Edit Firstname and Lastname
        fn3 = input("\nInput New First Name: ")
        ln3 = input("Input New Last Name: ")
        if fn3 == "" or ln3 == "":
            fln1_()

        cursor=conn.cursor()
        selectquery = "select * from players where ID = '"+ u_id3 +"'"
        cursor.execute(selectquery)
        records1=cursor.fetchall()                                        
        for row1 in records1:
            print("\n\tOld Record:",row1)

        cursor=conn.cursor()
        s1 = "update players set firstname = '"+ fn3 +"', lastname = '"+ ln3 +"' where ID = '"+ u_id3 +"'"  # EDIT QUERY
        cursor.execute(s1)
        conn.commit()

        cursor=conn.cursor()
        selectquery = "select * from players where ID = '"+ u_id3 +"'"
        cursor.execute(selectquery)
        records2=cursor.fetchall()                                        
        for row2 in records2:
            print("\tUpdated Record:",row2) 
        Goto_()
            
    def fields_1():
        print("\n\tChoose Fields:\n\t1. Edit Only First Name \n\t2. Edit Only Last Name \n\t3. Edit Firstname and Lastname\n")
        u_id4 = input("Input Choice: ")
        if u_id4 == "1":
            fn1_()
        elif u_id4 == "2":
            ln1_()
        elif u_id4 == "3":
            fln1_()
        else:
            fields_1()
    fields_1()

def DELETERECORD():   # DELETE RECORD
    u_n1 = input("\nEnter First Name: ")
    cursor=conn.cursor()
    selectquery = "select * from players where firstname like '%"+ u_n1 +"%'"
    cursor.execute(selectquery)
    records=cursor.fetchall()
    a2 = ["ID Numbers Available"]   # Declared First the Variable
    print("\nID  Firstname  Lastname")
    for row in records:
        print(row)
        a2 = a2
        a2.append(row[0]) # Adding ID numbers in Database

    a1 = str(records)
    if a1 == "[]":
        print("No Record Found!")
        DELETERECORD()

    def del_2():
        print("\nChoose ID Numbers: ", a2[1:])
        global u_id4
        u_id4 = input("\nEnter ID Number: ")
        if not int(u_id4) in a2[1:]:        # Comparing Input ID number to ID numbers Filtered
            del_2()
    del_2()
    
    def d_r1():
        cursor=conn.cursor()
        selectquery = "select * from players where ID = '"+ u_id4 +"'"
        cursor.execute(selectquery)
        records=cursor.fetchall()            
        for row in records:    
            print("\n", row)
        u_idv = input("Do you want to Delete this Record?y/n: ")

        if u_idv == "n":
            s_2()
        elif not u_idv == "y":
            d_r1()

        cursor=conn.cursor()
        selectquery = "select * from players where ID = '"+ u_id4 +"'"
        cursor.execute(selectquery)
        records=cursor.fetchall()                
        for row in records:
            print("\nRecord Deleted: ",row)

        cursor=conn.cursor()
        s1 = "delete from players where ID = '"+ u_id4 +"'"     # DELETE QUERY
        cursor.execute(s1)
        conn.commit()            
        s_2()
    d_r1()
        
def SEARCHRECORD(): # SEARCH RECORD
    se2 = input("\nSearch ID, FirstName or Lastname: ")
    cursor=conn.cursor()
    selectquery = "select * from players where ID LIKE '%"+ se2 +"%' or firstname LIKE '%"+ se2 +"%' or lastname LIKE '%"+ se2 +"%'"
    cursor.execute(selectquery)
    records=cursor.fetchall()
    print("\nID  Firstname  Lastname")
    for row in records:
        print(row)
    a1 = str(records)
    if a1 == "[]":
        print("No Record Found!")
    id_x()
        
    
def main():
    if conn.is_connected():
        print("\nWelcome Players Records\n")
        v_list = "\t1. View All Record \n\t2. Add New Record \n\t3. Edit Record \n\t4. Delete Record \n\t5. Search Record \n\t6. Close Program"
        print(v_list)

        input1 = input("\nEnter Choice: ")

        if input1 == "1": # VIEW ALL RECORD
            VIEWALLRECORD()

        elif input1 == "2":  # ADD NEW RECORD
            ADDNEWRECORD()

        elif input1 == "3":  # EDIT/UPDATE RECORD
            UPDATERECORD()

        elif input1 == "4": # DELETE RECORD
            DELETERECORD()

        elif input1 == "5":   # SEARCH RECORD
            SEARCHRECORD()

        elif input1 == "6":
            exit()
            
        else:
            main() 
    #else:
        #print("Database Not Connected")
main()


