from math import fabs
import re
import sys
sys.path.append( './' )
from Khan1.PreProcessing import PreProcess


# Get Value from regex

def finder(arr: list):
    return [x for x in arr if x]


# Run Khan1
PreProcess()


# Operation Regex
operationRegex = "[\+|\-|\*|\/|\%]+[\=]|[\+]+[\+]|[\-]+[\-]|[\+|\-|\*|\/|\%]|[\=]"
# Comparison Regex
comparisonRegex = "[\<|\>|\=|\!]+[\=]|[\<]|[\>]"
# Punctuation Regex
punctuationRegex = "\(|\)|\;|\,|\{|\}"
# Keywords
keyword = ["if", "else", "main", "while", "int","char",
           "float", "for", "string", "do", "#include"]



# Tokens saved in output list
output: list = []


def dfa(str1: str, lineNumber: int):
    begin = 0
    flag = False
    arrayFlag=False ;
    temp =[]

    for i in range(len(str1)):
        if(finder(re.findall("^[a-zA-Z_0-9\.]*", str1[i]))):
            continue

        else:
            token = str1[begin:i]
            if((str1[begin-1]=='"' and str1[i]=='"') or (str1[begin-1]=="'" and str1[i]=="'")):
                output.append(("number",token,lineNumber))
            # elif((str1[begin-1] not in ["'",'"'] and str1[i] in ["'",'"'] )or (str1[begin-1] in ["'",'"'] and str1[i] not in ["'",'"'] )):
            #     print("lexical error that happened in line : %d " % lineNumber)
            else:
                
                if(token in keyword):
                    output.append(("keyword", token,lineNumber))

                if(arrayFlag and str1[i]=='[') :
                    temp += str1[i]
                if(arrayFlag and finder(re.findall("^[0-9]+$", token))):
                    temp += token 
                if(arrayFlag and str1[i]==']') :
                        arrayFlag = False  
                        output.pop()
                        output.append(("identifier", temp,lineNumber))

                #Identifier startWith number
                elif(finder(re.findall("^[0-9]+[a-df-zA-Z_]+[a-zA-Z_0-9]*", token))):
                    print("lexical error that happened in line : %d " % lineNumber)

                #Identifier + dot
                elif(finder(re.findall("^[a-zA-Z]+[.]+[a-zA-Z_0-9]*", token))):
                    print("lexical error that happened in line : %d " % lineNumber)

                #9.9eq2 => Error
                elif(finder(re.findall("^[0-9]+[.]+[0-9]*[e][a-zA-Z_]+[a-zA-Z_0-9]*", token))):
                    print("lexical error that happened in line : %d " % lineNumber)

                #9.9e => Error
                elif(finder(re.findall("^[0-9]+[.]+[0-9]*[e]$", token))):
                    print("lexical error that happened in line : %d " % lineNumber)

                #9.9a => Error
                elif(finder(re.findall("^[0-9]+[.]+[0-9]*[a-df-zA-Z_]+[a-zA-Z_0-9]*", token))):
                    print("lexical error that happened in line : %d " % lineNumber)

                #9.9
                elif(finder(re.findall("^[0-9]+[.][0-9]+$", token)) ):
                    output.append(("number", token,lineNumber))


                elif(finder(re.findall("^[0-9]+[x][0-9]+$", token)) ):
                    output.append(("number", token,lineNumber))

                #99
                elif(finder(re.findall("^[0-9]+$", token)) ):
                    output.append(("number", token,lineNumber))

                #9.9e9
                elif(finder(re.findall("^[0-9]+[.][0-9]+[e][0-9]+$", token))):
                    output.append(("number", token,lineNumber))

                #9e223
                elif(finder(re.findall("^[0-9]+[e][0-9]+$", token))):
                    output.append(("number", token,lineNumber))
            
                    
                elif(finder(re.findall("^[a-zA-Z_][a-zA-Z_0-9]*", token))):
                    temp = token ;
                    arrayFlag = True ;
                    if( temp not in keyword) :
                        output.append(("identifier", token,lineNumber))
                        

                if(finder(re.findall(punctuationRegex, str1[i])) ):
                    if (not str1[i]=="[") :
                        output.append(("punctuation", str1[i],lineNumber))

                if(i <= len(str1)-2 and finder(re.findall(comparisonRegex, str1[i]+str1[i+1]))):
                    if(not(flag) and len(re.findall(comparisonRegex, str1[i]+str1[i+1])[0]) == 2):
                        output.append(("comparison", str1[i]+str1[i+1],lineNumber))
                        flag = True

                    elif(not(flag) and len(re.findall(comparisonRegex, str1[i]+str1[i+1])[0]) == 1):
                        output.append(("comparison", str1[i],lineNumber))

                    else:
                        flag = False
                elif(i <= len(str1)-2 and finder(re.findall(operationRegex, str1[i]+str1[i+1]))):
                    if(not(flag) and len(re.findall(operationRegex, str1[i]+str1[i+1])[0]) == 2):
                        if( not str1[i] == "]" and not str1[i+1]=="]") :
                            output.append(("operation", str1[i]+str1[i+1],lineNumber))
                            flag = True

                    elif(not(flag) and len(re.findall(operationRegex, str1[i]+str1[i+1])[0]) == 1):
                        if( not str1[i] == "]" ) :
                            output.append(("operation", str1[i],lineNumber))

                    else:
                        flag = False

            begin = i+1


# Read Lines from Source File

with open("In/new.txt") as f:
    lines = f.readlines()


lineNumber = 1


# remove Space between words

for i in lines:
    lineWords = []
    newArr = i.split(" ")
    if  not i.startswith("#") :
        for i in range(len(newArr)):
            try:
                if(newArr[i] in keyword):
                    lineWords.append(newArr[i]+" ")

                elif(newArr[i][0:3] == "for" and newArr[i].split("(")[1] in keyword):
                    lineWords.append(newArr[i]+" ")

                else:
                    lineWords.append(newArr[i])
            except IndexError as e:
                raise Exception("Keyword Not Found")

        dfa("".join(lineWords), lineNumber)
        lineNumber += 1


# Write in Output File

with open("out/answer.txt", "w") as f:
    for i in output:
        f.write(i[0])
        f.write(":: ")
        f.write(i[1])
        f.write("\n")

with open("Khan2/linesNumber.txt", "w") as f:
    for i in output:
        f.write(i[0])
        f.write(":: ")
        f.write(i[1])
        f.write(":: ")
        f.write(str(i[2]))
        f.write("\n")


# def errorHandling(data: str):
    # # Default Value should be 1 for "int main()"
    # loopsCount = 1
    # parenthesesCount = 0
    # # Loops Count
    # for item in ["for", "while", "if", "else"]:
    #     loopsCount += data.count(item)
    # # Parentheses Count
    # for item in ["{", "}"]:
    #     parenthesesCount += data.count(item)
    # res = data.split("\n")
    # for index in range(len(res)):
    #     # Parentheses Checking in while and for loop
    #     if(res[index].startswith("for") or res[index].startswith("while")):
    #         if(not(finder(re.findall("\)", res[index]) and finder(re.findall("\(", res[index]))))):
    #             print("In Line %d Has Error!!!!" % index)
    #     # Semicolon Checking
    #     if finder(re.findall("^int|float|string|char", res[index])):
    #         if(res[index][-1] != ";" and not finder(re.findall("main", res[index]))):
    #             print("In Line %d Has Error!!!!" % index)
    #      # ParenthesesCount in forLoop Checking
    #     if finder(re.findall("^for", res[index])):
    #         if(res[index].count(";") != 2):
    #             print("In Line %d Has Error!!!!" % index)
    #     # ParenthesesCount Checking
    #     if(loopsCount*2 != parenthesesCount):
    #         print("ParenthesesCount Error!!!!")
    #     # Check File Exist
    #     if(res[index].startswith("#include")):
    #         fileName = res[index].split(" ")[1:]
    #         if(not os.path.isfile(fileName)):
    #             print("In Line %d Has Error!!!!" % index)
