import os
import getpass
os.system("tput setaf 79")
print ("\t\t\thello thise is my container\t\t\t")

passwd = getpass.getpass("enter the passward  :")
apass = "redhat"

if passwd != apass:
    os.system("tput setaf  10")
    print("---authenticator incorrect---")
    exit()

print("where wuld you like to perform (local/remote) :",end='')
location=input()
print (location)

if location == "remote":
    remoteIP = input("enter our IP :")

while True:
  if location == "local":
   print("""    press 1: to see date
    press 2: to create (directory/file)
    press 3: to create a user
    press 4: to config the web-server
    press 5: to all commad status
    press 6: to show all partision
    press 7: exit
    """)

   print("enter the option ::",end='')
   ch = input()
   print(ch)

   if int(ch) == 1:
      os.system("date")
   if int(ch) == 2:
            print("what you create (directory/file)  :", end='')
            create_type = input()
            print(create_type)

            if create_type == "directory":
                print("enter the directory name :", end='')
                root = input()
                os.system("mkdir  {}".format(root))

            elif create_type == "file":
                print("enter the file name :", end='')
                root = input()
                os.system("touch  {}".format(root))

            else:
                print("---option not available---")
   elif int(ch) == 3:
        print ("enter the user name :", end='')
        create_user = input()
        os.system("useradd  {}".format(create_user))
   elif int(ch) == 4:
        os.system("yum install httpd")
   elif int(ch) == 5:
        os.system("ps -aux")
   elif int(ch) == 6:
        # 1. Show available disks so the user knows what they can partition
        print("--- Available Disks and Partitions ---")
        os.system("fdisk -l | grep -E '^Disk /dev/'")
   elif int(ch) == 7:
        exit()
   else:
        print("---option not avilable---")
   input("enter to continue---")
   os.system("clear")

  elif location == "remote":
   print("""    press 1: to see date
    press 2: to see cal
    press 3: to create a user
    press 4: to config the web-server
    press 5: to see all command status
    press 6: to create file
    press 7: exit
    """)

   print("enter the option ::",end='')
   ch = input()
   print(ch)

   if int(ch) == 1:
       os.system("ssh {0} date".format(remoteIP))
   elif int(ch) == 2:
        print("what you create (directory/file)  :", end='')
        create_type = input().strip().lower()
        print(create_type)

        if create_type == "directory":
            print("enter the directory name :", end='')
            root = input()
            os.system("ssh {0} mkdir {1}".format(remoteIP, root))

        elif create_type == "file":
            print("enter the file name :", end='')
            root = input()
            os.system("ssh {0} touch {1}".format(remoteIP, root))

        else:
            print("---option not available---")
   elif int(ch) == 3:
        print ("enter the user name :", end='')
        create_user = input()
        os.system("ssh {0} useradd  {1}".format(remoteIP,create_user))
   elif int(ch) == 4:
        os.system("ssh {0} yum install httpd".format(remoteIP))
   elif int(ch) == 5:
        os.system("ssh {0} ps -aux".format(remoteIP))
   elif int(ch) == 6:
        os.system("")
   elif int(ch) == 7:
        exit()
   else:
        print("---option not avilable---")
   input("enter to continue---")
   os.system("clear")
  else:
      os.system("tput setaf  4")
      print("----location not avilable----")
      exit()
