#IT20
#Mark Metshein
#Harjutus 10
import re
f = open("fail.txt")
r = f.readlines()
for i in range(len(r)):
       if re.search("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", r[i]):
            print(r[i], end="")