# Kafka Broadcaster

This is a simple Kafka broadcaster that reads from a CSV of events and a json templaet and sends the content to a Kafka topic.
It can also print out events sent to a topic when in listening mode.

# Usage
Populate `events.csv` with the information you want to use and `template.json` with how you want the events to look like when sent to Kafka.

Run this project using python:
```bash
cd ./app
python3 main.py send
```

See `python3 main.py --help` for more information.

## Example

Take this `events.csv`:
```csv
name,age,occupation,city
nicola,17,student,London
millie,15,student,London
antonina,15,student,London
dila,15,student,London
lasya,15,student,London
```

The header of the CSV will determine which placeholders are available to be replaced in `template.json`. In this case, the placeholders are `name`, `age`, `occupation` and `city`:
    
```json
{
    "name": "{name}",
    "age": "{age}",
    "occupation": "{occupation}",
    "city": "{city}",
    "department": "Technology",
    "type": "NewPerson"
}
```

Kafka Broadcaster will send 5 events to the topic:
```json
{ "name": "nicola", "age": "17", "occupation": "student", "city": "London", "department": "Technology", "type": "NewPerson" }
```
```json
{ "name": "millie", "age": "15", "occupation": "student", "city": "London", "department": "Technology", "type": "NewPerson" }
```
```json
{ "name": "antonina", "age": "15", "occupation": "student", "city": "London", "department": "Technology", "type": "NewPerson" }
```
```json
{ "name": "dila", "age": "15", "occupation": "student", "city": "London", "department": "Technology", "type": "NewPerson" }
```
```json
{ "name": "lasya", "age": "15", "occupation": "student", "city": "London", "department": "Technology", "type": "NewPerson" }
```