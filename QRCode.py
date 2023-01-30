#Importing usfull libraries

import pyqrcode # QR Code library
import csv #Csv library
import png #Help us to save in png 
import time


def one_csv():
    print('Enter the URL (https://example.com): ')
    url=input()
    print('Enter the name of the file')
    name=input()
    url=pyqrcode.create(url)
    url.png(name+'.png',scale=8)
    print('Creating Csv ...')
    time.sleep(0.5)
    print('QR Code Created')
    print('Thank you for using QR Code Generator')

def bulk_csv(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        data = list(reader)

    
    for i in range(len(data)):
        url = pyqrcode.create(data[i][0])
        url.png(data[i][0]+str(i)+'.png', scale=8)
        print('Creating Csv ...')
        time.sleep(0.4)
        
        


#Welcoming user

print('Welcome to QR Creater')
print('1. To Create One QR')
print('2. To Create Multiple QR')
print('3. To Exit')

#Taking input from user
choice=int(input("\nEnter your choice: "))
if choice==1:
    one_csv()
elif choice==2:
    print('Enter the name of the file')
    file_name=input()
    bulk_csv(file_name)
    print('QR Codes Created')
    print('Thank you for using QR Code Generator')









