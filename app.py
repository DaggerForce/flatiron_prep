# Business card excerice
# Git test
name = "art vandelay"  # capital the name correctly
position = "ceo"  # capital all letters
work = "vandaley industries"  # capital the name correctly
phone = "7285553334"  # 2 other phone number ending with 5 and 6
email = "art.vandelay@vandelay.co"  # check if ends with .com
site = "vandelay.com"  # check if begins with www.

name_trial = name.upper()  # test
name_capital = name.title()  # capitalzing first letter of each word
position_capital = position.upper()  # capital the entire word
work_capital = work.title()  # capitalzing first letter of each word

correct_email = email.endswith(".com")
correct_site = "www." + site
print(correct_email)
print(correct_site)
