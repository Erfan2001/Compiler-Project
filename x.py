import re
with open('a.c') as f:
    lines = f.readlines()

output: list = []

mapper: dict = {}


def dfa(str1: str):
    state = 'a'
    begin = 0
    for item in str1:
        # print(item)
        if(re.findall("^[a-zA-Z_0-9]*", item)[0]):
            if(item == "i"):
                state = "b"
            elif(item == "f" and state == "b"):
                state = "c"
            elif(re.findall("^[a-zA-Z_0-9]*", item)[0] and state == "c"):
                state = "d"
        else:
            # print(state)
            if(state == "c"):
                output.append(("keyword", "if"))
                begin = str1.find(item)
            elif(state == "d"):
                # mapper[str1[begin, str1.find(i)]] = None
                output.append(("identifier", str1[begin: str1.find(item)]))
                begin = str1.find(item)
            if(item == "("):
                output.append(("punctuation", "("))
                begin = str1.find(item)
            if(item == ")"):
                output.append(("punctuation", ")"))
                begin = str1.find(item)
            state = "a"


for i in lines:
    dfa(i.strip())
print(output)
# print(re.findall("^[a-zA-Z_0-9]*", "if9"))
