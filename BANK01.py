import random
#creating main lists
names=[]
phone=[]
passwords=[]
accno=[]
paisa=[]
main=[]

#class that holds user info
class account:
    i=[]
    j=[]
    k=[]
    l=[]
    m=[]
    z=[]
    def __init__(self,i,j,k,l,m,z):
        self.i=i
        self.j=j
        self.k=k
        self.l=l
        self.m=m
        self.z=z   
        print("\nWelcome to the BANK! ")
        while True:
            choice = int(input("\nMAIN MENU: \n1.Create Account\n2.Update Account\n3.Use Account\n4.Delete Account\n5.Quit\nChoose your option: "))

            if choice == 1:
                Name=input("Enter Name of the account holder: ") 
                i.append(Name)
                phone=int(input("Enter a valid Phone Number: "))
                j.append(phone)
                pasw=input("Enter a password: ")
                l.append(pasw)
                acc=random.randrange(1000,10000)
                k.append(acc)
                c=0
                m.append(c)
                print("\nAccount Created Successfully !")
                print("Your Account ID is: ",acc,"\n")

                
            elif choice == 2:
                messi=0
                update(names,phone,passwords,accno,paisa,main,messi)
            
            elif choice == 3:
                z.append(i)
                z.append(j)
                z.append(k)
                z.append(l)
                z.append(m)

                y=data(accno,passwords,names)
                

            elif choice == 4:
                accid=int(input("Enter ID:  "))
                password=input("Enter password: ")

                if password in l:
                    if accid in k:
                        print("\nLogin Successful!")
                        r=k.index(accid)
                        s=l.index(password)
                        if r == s:
                            l.remove(l[r])
                            i.remove(i[r])
                            j.remove(j[r])
                            k.remove(k[r])
                           
                            m.remove(m[r])
                            print(f"Account {accid} Deleted Successfully!")
                        else:
                            print("Someting's fishy")
                    else:
                        print("Somethin is worng.")
                else:
                    print("Try again.")           
            
            else :
                break
            
            

class data:

    def __init__(self,i,j,k):
        self.k=k
        accid=tuple(i)
        passw=tuple(j)
        useraccount=int(input("Enter the account number: "))
        userpassword=input("Enter password: ")
        self.k=i.index(userpassword)

        if useraccount in passw and userpassword in accid:
            if (accid.index(userpassword)) == (passw.index(useraccount)):
                print("Login Successful !")
                data.transactions(self,names,passwords,main)
            else:
                print("Something is wrong!") 
        else:
            print("Enter a valid ID or PASSWORD!")  
    def transactions(self,m,n,main):
        self.m=m
        self.n=n
        while True:
            choice=int(input("\nTRANSACTION MENU\n1.Transfer Money\n2.Deposit\n3.Withdraw\n4.Show Balance\n5.MAIN MENU\nChoose an option: "))
            if choice == 1:
                rname = input("Enter Reciever's name: ")
                racc = int(input("Enter Account number: "))
 
                if (racc in n) or (rname in m):
                    s=m.index(rname)
                    amt=int(input("Enter amount: "))  
                    x=main[4][self.k]
                    if x < amt :
                        print("Insufficient Balance Dalle!!!")
                    else:
                        x-=amt
                        main[4][self.k]=x
                        x=main[4][s]
                        x+=amt
                        main[4][s]=x
                     
                     
                        print("Transaction Successful!")
                else:
                    print("Somethin went wrong! ")  
                    
                
            if choice == 5:
                break

            if choice == 2:

                amt=int(input("Enter the amount to be deposit: "))
                x=main[4][self.k]
                x+=amt
                main[4][self.k]=x
                print(f"\nAmount {amt} Deposited Successfully!")

            if choice == 3:
                amt=int(input("Enter amount: "))  
                x=main[4][self.k]
                if x < amt :
                    print("Insufficient Balance Dalle!!!")
                else:
                    x-=amt
                    main[4][self.k]=x
                    print(f"\nAmount {amt} Withdrawn Successfully!")

            if choice == 4:
                x=main[4][self.k]
                print("\nCurrent balance: Rs.",x)

            if choice == 6:
                print(main)

            if choice == 5:
                x=account(names,phone,passwords,accno,paisa,main)

class update:
    messi=0
    def __init__(self,i,j,k,l,m,z,messi):
        accid=int(input("Enter ID:  "))
        password=input("Enter password: ")

        if password in l:
            if accid in k:

                r=k.index(accid)
                s=l.index(password)
                
                if r == s:
                    self.messi=r
                    print("\nLogin Successful!")
                
                    while True:
                        choice = int(input("\nUPDATION MENU :\n1. Name\n2. Phone Number\n3. Password\n4. Balance\n5.Print Records\n6.Main Menu\nChoose an option: "))
                        if choice == 1:
                            newname=input("Enter New name: ")
                            i[self.messi]=newname
                            if len(z) == 0:
                                continue
                            else:
                                z[0][self.messi]=newname


                    
                    
                        if choice == 2:
                            newphone=int(input("Enter new phone number: "))
            
      
                            j=newphone

                            if len(z) == 0:
                                continue
                            else:
                                z[1][self.messi]=newname
                                print(z)
                
                        if choice == 3:
                            newpasscode=input("Enter new password: ")
     
                        
                        #print(j[self.messi])
                            l[self.messi]=newpasscode

                            if len(z) == 0:
                                continue
                            else:
                                z[2][self.messi]=newpasscode
   

                        if choice == 4:
                            newbalance=int(input("Enter Updated Balance: "))
     
                

                        #print(j[self.messi])
                            m[self.messi]=newbalance
                   
                            if len(z) == 0:
                                continue
                            else:
                                z[4][self.messi]=newbalance
                     
                        if choice == 5:
                            print(i,j,k,l,m,z,messi)


                        if choice == 6:
                            x=account(names,phone,passwords,accno,paisa,main)
            else:
                print("Something is wrong!")
                        
        else:
            print("Enter a valid ID or PASSWORD!")

            




x=account(names,phone,passwords,accno,paisa,main)



              


