
import json

def replace_template(event):
    line = event.strip().split(",")

    #Data
    data_name = line[0]
    data_age = line[1]
    with open ('config/template.json', 'r', encoding='utf8') as t:
        data = str(t.read()).replace("{name}",data_name)
        data = str(data).replace("{age}",data_age)
        return json.loads(data)
    #end for
#end function

def program():
    with open ('config/events.csv') as f:

        #make a list
        data_list = []
        
        #Read the first line
        f.readline()

        #For loop, so it reads every line of the text file
        for line in f.readlines():
            new_data = replace_template(line)
            data_list.append(new_data)
        #end for
        return data_list
#end function
