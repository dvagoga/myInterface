def result(inputFilesNames):
    with open('fileExec.py', 'wt') as outFile:
        for ifn in inputFilesNames:
            name = "actions/" + ifn[0] + ".txt"
            with open(name, 'rt') as inFile:
                outFile.write('##' + '\n')
                firstLine = "inputParameter = " + '"' + ifn[1] + '"'
                outFile.write(firstLine + '\n')
                for line in inFile.readlines():
                    outFile.write(line + '\n')
    return "fileExec.py"
