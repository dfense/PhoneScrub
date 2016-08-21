import re


def phone_format(phone_number):
  # remove all the non-digits for clean number
  clean_phone_number = re.sub('[^0-9]+', '', phone_number)
  
  # add in the parens and hyphen
  return '(' + clean_phone_number[:3] + ') ' + clean_phone_number[3:6] + '-' + clean_phone_number[6:]
  
  
names_file = open("names.txt", encoding="utf-8")
data=names_file.read()
names_file.close()

last_name=r'Love'
first_name=r'Kenneth'

#print(re.match(last_name, data))
#print(re.search(first_name, data))

count = 13
re_str = r'\w{count,}'
re_pattern = re.compile(re_str)
#print(re.findall(r'\w{' + str(count) + ',}', data))
#print(re.findall(re_pattern, data))
  
print(re.findall(r'\bTreehouse\b', data, re.I))
                 
list = re.findall(r'\(?\d{3}\D*\d{3}\D*\d{4}', '7028559636 +1 850.456.3213 9099090909 (987) 444 - 4567  912.855.9456 - 3214 leson LEEsotree Brick', re.I)

for i in range(len(list)):
  list[i] = phone_format(list[i])
  #print(phone_format(list[i]))
  
print(list)