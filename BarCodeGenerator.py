import os
import qrcode
s=0
def create():
               data = input("Enter the data:")
               f = qrcode.make(data)
               file_name = input("Enter the filename:")
               f.save(file_name+".png")
def viewfile():
               file = os.listdir()
               
               if(len(file)>1):
                              print("---FILES----")
                              for i in file:
                                             name,sep,ext = i.partition(".")
                                             if(ext=="png"):
                                                            print(i)
               else:
                              print("No files found")

while 1:
               s = int(input("1.Create 2.viewfiles 3.Exit:"))
               if(s==1):
                              create()
               elif(s==2):
                              viewfile()
               elif(s==3):
                              print("Exit")
                              break
