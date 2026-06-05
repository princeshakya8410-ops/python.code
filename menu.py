import os

os.system("tput setaf 79")
print ("\t\t\thello thise is my container\t\t\t")

print("where wuld you like to perform (local/remote) :",end='')
location=input()
print (location)

if location == "remote":
    remoteIP = input("enter our IP :")
while True:
  if location == "local":
   print("""  press 1: to see date
    press 2: to see cal
    press 3: to create a user
    press 4: to config the web-server
    press 5: to create dirctory
    press 6: to create file
    press 7: exit
    """)

   print("enter the option ::",end='')
   ch = input()
   print(ch)

   if int(ch) == 1:
      os.system("date")
   elif int(ch) == 2:
        os.system("cal")
   elif int(ch) == 3:
        print ("enter the user name :", end='')
        create_user = input()
        os.system("useradd  {}".format(create_user))
   elif int(ch) == 4:
        os.system("yum install httpd")
   elif int(ch) == 5:
        print ("enter the directory name :", end='')
        root = input()
        os.system("mkdir  {}".format(root))
   elif int(ch) == 6:
        print ("enter the file name :", end='')
        root = input()
        os.system("touch  {}".format(root))
   elif int(ch) == 7:
        exit()
   else:
        print("---option not avilable---")
   input("enter to continue---")
   os.system("clear")

  elif location == "remote":
   print("""  press 1: to see date
    press 2: to see cal
    press 3: to create a user
    press 4: to config the web-server
    press 5: to create dirctory
    press 6: to create file
    press 7: exit
    """)

   print("enter the option ::",end='')
   ch = input()
   print(ch)

   if int(ch) == 1:
       os.system("ssh {0} date".format(remoteIP))
   elif int(ch) == 2:
        os.system("ssh {0} cal".format(remoteIP))
   elif int(ch) == 3:
        print ("enter the user name :", end='')
        create_user = input()
        os.system("ssh {0} useradd  {1}".format(remoteIP,create_user))
   elif int(ch) == 4:
        os.system("ssh {0} yum install httpd".format(remoteIP))
   elif int(ch) == 5:
        print ("enter the directory name :", end='')
        root = input()
        os.system("ssh {0}mkdir  {1}".format(remoteIP,root))
   elif int(ch) == 6:
        print ("enter the file name :", end='')
        root = input()
        os.system("ssh {0}touch  {1}".format(remoteIP,root))
   elif int(ch) == 7:
        exit()
   else:
        print("---option not avilable---")
   input("enter to continue---")
   os.system("clear")
  else:
      print("----location not avilable----")
