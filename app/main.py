#main code
import json


with open ('config/events.csv') as f:
    read = True

    #make a list
    data_list = []

    #while loop
    while read == True:
        
        f.readline()

        #For loop, so it reads every line of the text file
        for line in f.readlines():

            #split into into two sets of numbers and gets rid of the \n
            line = line.strip()
            line = line.split(",")

            #Data
            data_name = line[0]
            data_age = line[1]

            with open ('config/template.json', 'r', encoding='utf8') as t:
                data = str(t.read()).replace("{name}",data_name)
                data = str(data).replace("{age}",data_age)
                json_data = json.loads(data)
                #print(json_data)
                data_list.append(json_data)
            t.close()

        #end for
        read = False
        print(data_list)
                
            
           
f.close()