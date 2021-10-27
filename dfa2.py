import re
import string
with open('test.c') as f:
    lines = f.readlines()

output: list = []

keyword = ["if", "else", "main", "while", "int",
           "float", "for", "string", "do", "#include"]
punctuations = ["(", ")", ";", ",", "[", "]", "{", "}"]
comparison = [">", "<", "<=", "==", ">=", "!="]
# operations = ["+", "-", "*", "/", "%", "=",
#               "++", "--", "+=", "-=", "/=", "*=", "%="]
operations = ["+", "-", "*", "/", "%", "="]


def dfa(str1: str):
    state = 'a'
    begin = 0
    str1 = str1.replace(" ", "")
    flag = False
    for i in range(len(str1)):
        if(re.findall("^[a-zA-Z_0-9]*", str1[i])[0]):
            continue
        else:
            token = str1[begin:i]
            if(token in keyword):
                output.append(("keyword", token))
            elif(re.findall("^[0-9]*", token)[0]):
                output.append(("number", token))
            elif(re.findall("^[a-zA-Z_0-9]*", token)[0]):
                output.append(("identifier", token))
            if(str1[i] in punctuations):
                output.append(("punctuation", str1[i]))
            if(str1[i] in comparison):
                output.append(("comparison", str1[i]))
            if(str1[i] in operations and str1[i+1] == "="):
                output.append(("operation", str1[i]+str1[i+1]))
                flag = True
            elif(str1[i] in operations and not(flag)):
                output.append(("operation", str1[i]))
            begin = i+1


for i in lines:
    dfa(i.strip())
print(output)
