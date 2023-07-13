#main code
with open ('.txt') as f:
    read = True

    #while loop
    while read == True:

        #For loop, so it reads every line of the text file
        for line in f.readlines():

            #split into into two sets of numbers and gets rid of the \n
            line = line.strip()
            line = line.split(",")
