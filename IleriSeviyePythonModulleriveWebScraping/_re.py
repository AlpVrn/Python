import re

result = dir(re)

# re module
str = "Python Kursu : Pyton Programlama Rehberi |40 saat"

# re.findall()

# result = re.findall("Python",str)
# result = len(result)

# re.split()

result = re.split(" ",str)
result = re.split("R",str)

#re.sub()

result = re.sub(" ","-",str)

# regular expression
 

print(result)