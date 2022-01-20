def makeSemanticTable():    
    with open('out/answer.txt') as f:
        content = f.readlines()
    identifierTable = []
    keywords = ["int", "float", "char"]
    keyword = None
    for i in range(len(content)):
        if (content[i].split(" ")[1][:-1] in keywords):
            keyword = content[i].split(" ")[1][:-1]
        if(content[i].startswith("identifier") and keyword):
            identifierTable.append((keyword,content[i].split(" ")[1][:-1]))
        if(content[i].split(" ")[1][:-1] == ";" and keyword):
            keyword=None
    writeContent=""
    for i in range(len(identifierTable)):
        writeContent+="%s %s\n"%(identifierTable[i][0],identifierTable[i][1])
    with open("out/identifierTable.txt","w") as f:
        f.write(writeContent)
