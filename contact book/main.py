while True:
 opt = input('''Add a contact-->(1)
Search a contact-->(2)
Remove a contact-->(3)
To view all contacts-->(4)
Delete all contacts-->(5)
To Exit-->(6)
Enter your Option:  ''').upper()

 if opt == "1":
  with open ('contact.txt','a') as f:
    name = input("name: ")
    phone = input("Phone number: ")
    f.writelines((name," : ",phone,"\n"))

 elif opt == "2":
  with open('contact.txt','r') as f:
    search = input("search: ")
    for i in f:
      if search in i:
        print(i)

 elif opt == "3":
        with open('contact.txt', 'r') as f:
            lines = f.readlines()       
        rem = input("Remove contact: ")
        with open('contact.txt', 'w') as f:
            removed = False
            for line in lines:
                if rem not in line:
                    f.write(line)
                else:
                    removed = True
            if removed:
                print(f"Contact '{rem}' removed.")
            else:
                print(f"Contact '{rem}' not found.")

 elif opt == "4":
    with open('contact.txt','r') as f:
       lines= f.readlines()
       for names in lines:
          print(names,end=" ")

 elif opt == "5":
    with open('contact.txt','w+') as f:
       for i in f:
          i.remove()
    print("All Contacts Deleted!!!")

 else:
    break
