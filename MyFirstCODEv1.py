def main():
    import mysql.connector 

    server = "localhost"
    user = "root"
    pasx = "your_password"
    db = "records"

    conn = mysql.connector.connect(host=server,username=user,password=pasx,database=db)

    if conn.is_connected():
        
        print("\nWelcome Players Records\n")
        v_list = "\t1. View All Record \n\t2. Add New Record \n\t3. Edit Record \n\t4. Delete Record \n\t5. Search Record \n\t6. Close Program"
        print(v_list)

        input1 = input("\nEnter Choice: ")

        if input1 == "1":  # VIEW ALL RECORD
            cursor=conn.cursor()
            selectquery = "select * from players order by ID desc"
            cursor.execute(selectquery)
            records=cursor.fetchall()
            print("\n\tNumber of Players:",cursor.rowcount)
            print("\t  ID  FirstName  LastName")
            for row in records:
                print("\t", row)
            def b1():
                res_1 = input("\nDo you want to go Main?y/n: ")
                if res_1 == "y":
                    main()
                elif res_1 == "n":
                    exit()
                else:
                    b1()
            b1()
        elif input1 == "2":    # ADD NEW RECORD
            def add_1():
                f_n = input("\nEnter your First Name:")
                l_n = input("Enter your Last Name:")

                if f_n == "" or l_n == "":
                    print("\n\tPlease Fill-up All Fields")
                    add_1()
                else:
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
                            add_1()
                        elif res_2 == "n":
                            def b2():
                                res_1 = input("\nDo you want to go Main?y/n: ")
                                if res_1 == "y":
                                    main()
                                elif res_1 == "n":
                                    exit()
                                else:
                                    b2()
                            b2()
                        else:
                            bx()
                    bx()
            add_1()
        elif input1 == "3":
            def edit_1():   # EDIT/UPDATE RECORD
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
                    edit_1()
                else:
                    def edit_2():
                        print("\nID Numbers Available: ", a2[1:])
                        u_id3 = input("\nEnter ID Number: ")
                        if int(u_id3) in a2[1:]:        # Comparing Input ID number to ID numbers Filtered
                            def fields_1():
                                print("\n\tChoose Fields:\n\t1. Edit Only First Name \n\t2. Edit Only Last Name \n\t3. Edit Firstname and Lastname\n")
                                u_id4 = input("Input Choice: ")
                                if u_id4 == "1":
                                    def fn1_():
                                        fn1 = input("\nInput New First Name: ")
                                        if fn1 == "":
                                            fn1_()
                                        else:
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
                                            
                                            def Goto_():
                                                u_idx = input("\nGo to Choose fields?y/n: ")
                                                if u_idx == "y":
                                                    fields_1()
                                                elif u_idx == "n":
                                                    def un_r():
                                                        u_idx1 = input("\nUpdate New Record?y/n: ")
                                                        if u_idx1 == "y":
                                                            edit_1()
                                                        elif u_idx1 == "n":
                                                            def mained1():
                                                                res_1 = input("\nDo you want to go Main?y/n: ")
                                                                if res_1 == "y":
                                                                    main()
                                                                elif res_1 == "n":
                                                                    exit()
                                                                else:
                                                                    mained1()
                                                            mained1()
                                                        else:
                                                            un_r()
                                                    un_r()
                                                else:
                                                    Goto_()
                                            Goto_()
                                    fn1_()
                                elif u_id4 == "2":
                                    def ln1_():
                                        ln1 = input("\nInput New Last Name: ")
                                        if ln1 == "":
                                            ln1_()
                                        else:
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
                                            
                                            def Goto1_():
                                                u_idx = input("\nGo to Choose fields?y/n: ")
                                                if u_idx == "y":
                                                    fields_1()
                                                elif u_idx == "n":
                                                    def un_r():
                                                        u_idx1 = input("\nUpdate New Record?y/n: ")
                                                        if u_idx1 == "y":
                                                            edit_1()
                                                        elif u_idx1 == "n":
                                                            def mained1():
                                                                res_1 = input("\nDo you want to go Main?y/n: ")
                                                                if res_1 == "y":
                                                                    main()
                                                                elif res_1 == "n":
                                                                    exit()
                                                                else:
                                                                    mained1()
                                                            mained1()
                                                        else:
                                                            un_r()
                                                    un_r()
                                                else:
                                                    Goto1_()
                                            Goto1_()  
                                    ln1_()
                                elif u_id4 == "3":
                                    def fln1_():
                                        fn3 = input("\nInput New First Name: ")
                                        ln3 = input("Input New Last Name: ")
                                        if fn3 == "" or ln3 == "":
                                            fln1_()
                                        else:
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
                                            
                                            def Goto1_():
                                                u_idx = input("\nGo to Choose fields?y/n: ")
                                                if u_idx == "y":
                                                    fields_1()
                                                elif u_idx == "n":
                                                    def un_r():
                                                        u_idx1 = input("\nUpdate New Record?y/n: ")
                                                        if u_idx1 == "y":
                                                            edit_1()
                                                        elif u_idx1 == "n":
                                                            def mained1():
                                                                res_1 = input("\nDo you want to go Main?y/n: ")
                                                                if res_1 == "y":
                                                                    main()
                                                                elif res_1 == "n":
                                                                    exit()
                                                                else:
                                                                    mained1()
                                                            mained1()
                                                        else:
                                                            un_r()
                                                    un_r()
                                                else:
                                                    Goto1_()
                                            Goto1_()  
                                    fln1_()
                                else:
                                    fields_1()
                            fields_1()
                        else:
                            edit_2()
                    edit_2()
            edit_1()
        elif input1 == "4": 
            def del_1():   # DELETE RECORD
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
                    del_1()
                else:  
                    def del_2():
                        print("\nChoose ID Numbers: ", a2[1:])
                        u_id3 = input("\nEnter ID Number: ")
                        if int(u_id3) in a2[1:]:        # Comparing Input ID number to ID numbers Filtered
                            def d_r1():
                                cursor=conn.cursor()
                                selectquery = "select * from players where ID = '"+ u_id3 +"'"
                                cursor.execute(selectquery)
                                records=cursor.fetchall()            
                                for row in records:    
                                    print("\n", row)
                                u_idv = input("Do you want to Delete this Record?y/n: ")
                                if u_idv == "y":
                                    cursor=conn.cursor()
                                    selectquery = "select * from players where ID = '"+ u_id3 +"'"
                                    cursor.execute(selectquery)
                                    records=cursor.fetchall()                
                                    for row in records:
                                        print("\nRecord Deleted: ",row)

                                    cursor=conn.cursor()
                                    s1 = "delete from players where ID = '"+ u_id3 +"'"     # DELETE QUERY
                                    cursor.execute(s1)
                                    conn.commit()

                                    def s_2():
                                        u_idv1 = input("\nDelete Another Record Again?y/n: ")
                                        if u_idv1 == "y":
                                            del_1()
                                        elif u_idv1 == "n":
                                            def mained1():
                                                res_1 = input("\nDo you want to go Main?y/n: ")
                                                if res_1 == "y":
                                                    main()
                                                elif res_1 == "n":
                                                    exit()
                                                else:
                                                    mained1()
                                            mained1()
                                        else:
                                            s_2()
                                    s_2()
                                elif u_idv == "n":
                                    def s_1():
                                        u_idv1 = input("\nSearch First Name Again?y/n: ")
                                        if u_idv1 == "y":
                                            del_1()
                                        elif u_idv1 == "n":
                                            def mained1():
                                                res_1 = input("\nDo you want to go Main?y/n: ")
                                                if res_1 == "y":
                                                    main()
                                                elif res_1 == "n":
                                                    exit()
                                                else:
                                                    mained1()
                                            mained1()
                                        else:
                                            s_1()
                                    s_1()
                                else:
                                    d_r1()
                            d_r1()
                        else:
                            del_2()
                    del_2()
            del_1()
        elif input1 == "5":   # SEARCH RECORD
            def sea_1():
                print("\n\tSearch Record By:\n\t1. ID Number \n\t2. First Name \n\t3. Last Name\n")
                se_1 = input("Input Choice: ")
                if se_1 == "1":
                    def r_1():
                        se2 = input("\nEnter ID Number: ")
                        cursor=conn.cursor()
                        selectquery = "select * from players where ID = '"+ se2 +"'"
                        cursor.execute(selectquery)
                        records=cursor.fetchall()
                        print("\nID  Firstname  Lastname")
                        for row in records:
                            print(row)
                        a1 = str(records)
                        if a1 == "[]":
                            print("No Record Found!")
                            r_1()
                        else:
                            def id_x():
                                res_1 = input("\nSearch Another ID Number?y/n: ")
                                if res_1 == "y":
                                    r_1()
                                elif res_1 == "n":
                                    def id_y():
                                        res_n = input("\nGo Back to Search Menu?y/n: ")
                                        if res_n == "y":
                                            sea_1()
                                        elif res_n == "n":
                                            def mained1():
                                                res_1 = input("\nDo you want to go Main?y/n: ")
                                                if res_1 == "y":
                                                    main()
                                                elif res_1 == "n":
                                                    exit()
                                                else:
                                                    mained1()
                                            mained1()
                                        else:
                                            id_y()
                                    id_y()
                                else:
                                    id_x()
                            id_x()
                    r_1()
                elif se_1 == "2":
                    def r_2():
                        se3 = input("\nEnter First Name: ")
                        cursor=conn.cursor()
                        selectquery = "select * from players where firstname like '%"+ se3 +"%'"
                        cursor.execute(selectquery)
                        records=cursor.fetchall()
                        print("\nID  Firstname  Lastname")
                        for row in records:
                            print(row)
                        a1 = str(records)
                        if a1 == "[]":
                            print("No Record Found!")
                            r_2()
                        else:
                            def id_x():
                                res_1 = input("\nSearch First Name Again?y/n: ")
                                if res_1 == "y":
                                    r_2()
                                elif res_1 == "n":
                                    def id_y():
                                        res_n = input("\nGo Back to Search Menu?y/n: ")
                                        if res_n == "y":
                                            sea_1()
                                        elif res_n == "n":
                                            def mained1():
                                                res_1 = input("\nDo you want to go Main?y/n: ")
                                                if res_1 == "y":
                                                    main()
                                                elif res_1 == "n":
                                                    exit()
                                                else:
                                                    mained1()
                                            mained1()
                                        else:
                                            id_y()
                                    id_y()
                                else:
                                    id_x()
                            id_x()
                    r_2()
                elif se_1 == "3":
                    def r_3():
                        se4 = input("\nEnter Last Name: ")
                        cursor=conn.cursor()
                        selectquery = "select * from players where lastname like '%"+ se4 +"%'"
                        cursor.execute(selectquery)
                        records=cursor.fetchall()
                        print("\nID  Firstname  Lastname")
                        for row in records:
                            print(row)
                        a1 = str(records)
                        if a1 == "[]":
                            print("No Record Found!")
                            r_3()
                        else:
                            def id_x():
                                res_1 = input("\nSearch Last Name Again?y/n: ")
                                if res_1 == "y":
                                    r_3()
                                elif res_1 == "n":
                                    def id_y():
                                        res_n = input("\nGo Back to Search Menu?y/n: ")
                                        if res_n == "y":
                                            sea_1()
                                        elif res_n == "n":
                                            def mained1():
                                                res_1 = input("\nDo you want to go Main?y/n: ")
                                                if res_1 == "y":
                                                    main()
                                                elif res_1 == "n":
                                                    exit()
                                                else:
                                                    mained1()
                                            mained1()
                                        else:
                                            id_y()
                                    id_y()
                                else:
                                    id_x()
                            id_x()
                    r_3()
                else:
                    sea_1()
            sea_1()
        elif input1 == "6":
            exit()
        else:
            main() 
    #else:
        #print("Database Not Connected")
main()