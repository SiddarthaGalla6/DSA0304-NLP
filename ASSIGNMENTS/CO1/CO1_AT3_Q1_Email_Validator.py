import re
email = input("Enter Email: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")
email_pat = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'
mobile_pat = r'^[6-9][0-9]{9}$'
if re.fullmatch(email_pat, email):
    print("Valid Email")
else:
    print("Invalid Email")
strong = (len(password) >= 8 and
          re.search(r'[A-Z]', password) and
          re.search(r'[a-z]', password) and
          re.search(r'\d', password) and
          re.search(r'[@#$%&!]', password))
print("Strong Password" if strong else "Weak Password")
if re.fullmatch(mobile_pat, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


Output :
Enter Email: siddarthagalla@gmail.com
Enter Password: siddu1
Enter Mobile Number: 8555066377
Valid Email
Weak Password
Valid Mobile Number
