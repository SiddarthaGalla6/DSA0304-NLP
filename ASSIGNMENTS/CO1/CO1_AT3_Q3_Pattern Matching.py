import re
text = input("Enter text: ")
print("1.Date  2.Phone  3.Hashtag")
print("4.Mention  5.Prefix  6.Suffix")
choice = input("Enter choice: ")
if choice == '1':
    result = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
elif choice == '2':
    result = re.findall(r'\b[6-9]\d{9}\b', text)
elif choice == '3':
    result = re.findall(r'#\w+', text)
elif choice == '4':
    result = re.findall(r'@\w+', text)
elif choice == '5':
    prefix = input("Enter prefix: ")
    result = re.findall(r'\b' + re.escape(prefix) + r'\w*', text)
elif choice == '6':
    suffix = input("Enter suffix: ")
    result = re.findall(r'\b\w*' + re.escape(suffix) + r'\b', text)
else:
    result = []
print("Matches:", result if result else "No matches found")


Output :
Enter text: My name is Siddartha and date is 27/07/2026 and phone number is 8555066377 and @siddartha and meeting is #NLP 
1.Date  2.Phone  3.Hashtag
4.Mention  5.Prefix  6.Suffix
Enter choice: 1
Matches: ['27/07/2026']
