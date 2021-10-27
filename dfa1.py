import re
with open('test.c') as f:
    lines = f.readlines()

output: list = []

mapper: dict = {}


def dfa(str1: str):
    state = 'a'
    begin = 0
    for item in str1:
        if(re.findall("^[a-zA-Z_0-9]*", item)[0]):
            if(item == "i" and state == "a"):
                state = "b"
            elif(item == "f" and state == "b"):
                state = "c"
            elif(re.findall("[a-eg-zA-Z_0-9]*", item)[0] and state == "b"):
                state = "d"
            elif(re.findall("^[a-zA-Z_0-9]*", item)[0] and state == "c"):
                state = "d"
            elif(re.findall("^[a-zA-Z_0-9]*", item)[0] and state == "d"):
                state = "d"
        else:
            if(state == "c"):
                output.append(("keyword", "if"))
                begin = str1.find(item)+1
            elif(state == "d"):
                output.append(("identifier", str1[begin: str1.find(item)]))
                begin = str1.find(item)+1
            if(item == "("):
                output.append(("punctuation", "("))
                begin = str1.find(item)+1
            if(item == ")"):
                output.append(("punctuation", ")"))
                begin = str1.find(item)+1
            state = "a"


for i in lines:
    dfa(i.strip())
print(output)
# print(re.findall("^[a-zA-Z_0-9]*", "if9"))
