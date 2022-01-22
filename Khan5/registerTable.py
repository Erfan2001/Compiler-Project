def makeRegisterTable():    
    with open("Khan4\semanticTree.txt") as f:
        content = f.readlines()

    result = ""
    counter = 0
    
    for item in content:
        if(item.split(" ")[0] in ["char", "float", "int"]):
            result += "%s %s %s\n" % (item.split(" ")[1], str(counter), "0")
            counter += 1

    with open("Khan5\\registerTable.txt", "w") as f:
        f.write(result)