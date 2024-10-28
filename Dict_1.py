
d1={}

while True :
      ch=int(input("Enter the choice :\n 1. Add  \t  2.show \t 3.Delete \t  4.Update  \t 5. Exist "))
      if ch==1:
        c = int(input("Enter number of students u want to add :"))
        for i in range(c):
            contact_name = input("Enter ur name :")
            mob_no = int(input("Enter ur Mobile Number : "))
            d1[mob_no]=contact_name
            print("Added your Name & Mob No")
      elif ch==2:
           print(d1)
      elif ch==3:
          n=int(input("Enter a mob no to delete the record : "))
          for i in list(d1.keys()):
              if i==n:
                 print(d1[i], "Ur Information is Deleted ")
                 d1.pop(i)
                 #print(d1[i], "Ur Information is Deleted ")
      elif ch==4:
          b=int(input("Enter a mob no to update ur name : "))
          for i in list(d1.keys()):
                if i==b:
                    d=input("Enter ur name :")
                    d1[i]=d
                    print(d1[i], "Ur information is Updated")
      elif ch==5:
         break
      else:
        print(ch, "Ur choice is wrong")













