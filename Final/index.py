import sys
import os
import glob
folder_path = 'Final/Input/'
index=0
for filename in glob.glob(os.path.join(folder_path, '*.c')):
    index+=1
    with open(filename, 'r') as f:
        fileData = f.read()
    with open("In/test.c","w") as file:
        for item in fileData:
            file.write(item)
    os.system("python Khan2/Lexical.py")
    with open("In/new.txt","r") as f:
        preProccess=f.read()
    with open("out/answer.txt","r") as f:
        lexical=f.read()
    with open("Final/Output/PrePreProcess%s.txt"%str(index),"w") as f:
        f.write(preProccess)
    with open("Final/Output/Lexical%s.txt"%str(index),"w") as f:
        f.write(lexical)
    os.system("python Khan3/Syntax.py")
    with open("out/ParseTree/ParseTree.gv.pdf","br") as f:
        parseTree=f.read()
    with open("Final/Output/ParseTree%s.pdf"%str(index),"bw") as f:
        f.write(parseTree)
    with open("out/ParseTree/StackProccess.txt","r") as f:
        stackProcess=f.read()
    with open("Final/Output/StackProccess%s.txt"%str(index),"w") as f:
        f.write(stackProcess)
    os.system("python Khan4/index.py")
    with open("Khan4/semanticTable.txt","r") as f:
        semanticTable=f.read()
    with open("Final/Output/semanticTable%s.txt"%str(index),"w") as f:
        f.write(semanticTable)
    os.system("python Khan5/index.py")
    with open("out/codeGeneration.txt","r") as f:
        codeGeneration=f.read()
    with open("Final/Output/codeGeneration%s.txt"%str(index),"w") as f:
        f.write(codeGeneration)
    print("-----------------------------------------------------------------------")
    
    
