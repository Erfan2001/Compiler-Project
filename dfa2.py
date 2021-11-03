import re

# Input Path
# inputFile = input("Enter Input Path\n")

# Output Path
# outputFile = input("Enter Output Path\n")

# Remove Comments Function


def remove_Comments(fileContent):
    removeMultipleComments = re.sub(
        "/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", fileContent)
    removeSingleComments = re.sub(
        "//.*", "", removeMultipleComments)
    result = removeSingleComments
    return result

# Remove Spaces Function


def removeSpaces(data: str):
    res = data.split("\n")
    res = [x for x in res if x]
    return "\n".join(res)

# Replace Includes


def replaceIncludes(data: str):
    res = data.split("\n")
    for index in range(len(res)):
        if(res[index].startswith("#include")):
            res[index] = res[index].replace(" ", "")
            fileName = res[index].split("#include")[1][1:-1]
            with open(fileName) as f:
                fileData = f.read()
            res[index] = fileData+"\n"
        else:
            res[index] += "\n"
    return "".join(res)

# Replace Defines


def replaceDefines(data: str):
    res = data.split("\n")
    definesDic: dict = {}
    for index in range(len(res)):
        if(res[index].startswith("#define")):
            key = res[index].split(" ")[1]
            value = " ".join(res[index].split(" ")[2:])
            definesDic[key] = value
    for index in range(len(res)):
        for key, value in definesDic.items():
            res[index] = res[index].replace(key, value)
        res[index] += "\n"
    res = [x for x in res if not x.startswith("#")]
    return "".join(res)


# Read Lines from Source File
with open("In/test.c") as f:
    lines = f.readlines()

# Read FileData from Source File
with open("In/test.c") as f:
    fileData = f.read()

# Calling remove Comments
program = remove_Comments(fileData)
# Calling remove Includes
result = replaceIncludes(program)
# Calling remove Defines
result2 = replaceDefines(result)
# Calling remove Spaces
result3 = removeSpaces(result2)
# Write In New File
with open("In/new.txt", "w") as f:
    f.write(result3)

# Operation Regex
operationRegex = "[\+|\-|\*|\/|\%]+[\=]|[\+]+[\+]|[\-]+[\-]|[\+|\-|\*|\/|\%]|[\=]"
# Comparison Regex
comparisonRegex = "[\<|\>|\=|\!]+[\=]|[\<]|[\>]"
# Punctuation Regex
punctuationRegex = "\(|\)|\;|\,|\[|\]|\{|\}"
# Keywords
keyword = ["if", "else", "main", "while", "int",
           "float", "for", "string", "do", "#include"]

output: list = []


def finder(arr: list):
    return [x for x in arr if x]


def dfa(str1: str):
    begin = 0
    # str1 = str1.replace(" ", "")
    flag = False
    for i in range(len(str1)):
        if(finder(re.findall("^[a-zA-Z_0-9]*", str1[i]))):
            continue
        else:
            token = str1[begin:i]
            if(token in keyword):
                output.append(("keyword", token))
            elif(finder(re.findall("^[0-9]*", token))):
                output.append(("number", token))
            elif(finder(re.findall("^[a-zA-Z_0-9]*", token))):
                output.append(("identifier", token))
            if(finder(re.findall(punctuationRegex, str1[i]))):
                output.append(("punctuation", str1[i]))
            if(i <= len(str1)-2 and finder(re.findall(comparisonRegex, str1[i]+str1[i+1]))):
                if(not(flag) and len(re.findall(comparisonRegex, str1[i]+str1[i+1])[0]) == 2):
                    output.append(("comparison", str1[i]+str1[i+1]))
                    flag = True
                elif(not(flag) and len(re.findall(comparisonRegex, str1[i]+str1[i+1])[0]) == 1):
                    output.append(("operation", str1[i]))
                else:
                    flag = False
            if(i <= len(str1)-2 and finder(re.findall(operationRegex, str1[i]+str1[i+1]))):
                if(not(flag) and len(re.findall(operationRegex, str1[i]+str1[i+1])[0]) == 2):
                    output.append(("operation", str1[i]+str1[i+1]))
                    flag = True
                elif(not(flag) and len(re.findall(operationRegex, str1[i]+str1[i+1])[0]) == 1):
                    output.append(("operation", str1[i]))
                else:
                    flag = False
            begin = i+1


# Write in Output File
with open("out/answer.txt", "w") as f:
    for i in output:
        f.write(i[0])
        f.write(":: ")
        f.write(i[1])
        f.write("\n")
