import re

str1="SDC(My name is dinesh" \
     "I'm from vijayawada" \
     "I'm studying in lavada KL )"
matches1=re.findall("is",str1)
print(matches1)
matches2=re.search("I'm",str1)
print(matches2)

