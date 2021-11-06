# import re
# keyword: dict = {
#     "keyword": []
# }
# with open('a.c') as f:
#     lines = f.readlines()
# for i in lines:
#     arr = re.findall("[\w]+", i)
#     print(arr)

a: dict = {}
a["ali"] = "1"
a["reza"] = "12"
print(a)
t = "34ali12"
for key, value in a.items():
    t=t.replace(key, value)
print(t)
