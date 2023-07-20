
import json

def make_values_map(columns, values_list):
    values_map = {}
    for i, column in enumerate(columns):
        values_map[column] = values_list[i]
    return values_map


def load_template():
    with open ('config/template.json', 'r', encoding='utf8') as t:
        return t.read()


def create_event_from_template(template, event, columns):
    line = event.strip().split(",")
    # Build dynamic map of values indexed by the column name
    values_map = make_values_map(columns, line)
    
    replaced_template = str(template)
    for key, value in values_map.items():
        # Replace all instances of a placeholder with its respective value
        replaced_template = replaced_template.replace("{"+key+"}", value)

    return json.loads(replaced_template)


def create_events():
    with open ('config/events.csv') as f:
        template = load_template()
        
        #make a list
        data_list = []
        
        #Read the first line
        columns = f.readline().strip().split(",")

        #For loop, so it reads every line of the text file
        for line in f.readlines():
            new_data = create_event_from_template(template, line, columns)
            data_list.append(new_data)
        return data_list
