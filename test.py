import re
keyword: dict = {
    "keyword": []
}
with open('a.c') as f:
    lines = f.readlines()
for i in lines:
    arr = re.findall("[\w]+", i)
    print(arr)
