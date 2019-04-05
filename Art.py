## Business card excerice
name = "art vandelay" #capital the name correctly
position = "ceo" #capital all letters 
work = "vandaley industries" #capital the name correctly
phone = "7285553334" #2 other phone number ending with 5 and 6
email = "art.vandelay@vandelay.co" #check if ends with .com
site = "vandelay.com" #check if begins with www.
address= None

name_trial = name.upper() #test
name_capital = name.title() #capitalzing first letter of each word
position_capital = position.upper() #capital the entire word
work_capital = work.title() #capitalzing first letter of each word

correct_email = email.endswith(".com") #checking if the email is correct
correct_site = "www." + site #correcting the website address

#converting the phone number into strings and add the 2 additional phone numbers
phone1 = int(phone) #1st number

list_phone2 = list(phone) ## there has to be a better way to do this..
list_phone2[-1] = "6"

list_phone3 = list(phone) ## there has to be a better way to do this..
list_phone[-1] = "6"




