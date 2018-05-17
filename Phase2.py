file1 = raw_input ("what is the name of the file you want to open?  ")
phase1File = ('{}.txt').format(file1)
with open(phase1File, 'r+') as openTerm:
    rest = 0
    print openTerm
    while rest != 100:
        old = openTerm.read()
        openTerm.seek(rest)
        openTerm.write("new line/n" + old)
        print openTerm
        rest = rest + 1



#propInfo = raw_input("What information would you like? For order -o, for inputfile -i, for outputdirectorypath -p")
#if propInfo == ('-o')

    #foundInfo = propInfo.find('')
