# !/usr/bin/venv python3
from bs4 import BeautifulSoup

################################################################# BeautifulSoup Explain #############################################################

# HTML Parsing

# Sample HTML content
html_content = """
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome to Beautiful Soup</h1>
    <p>This is a sample page for illustration.</p>
    <a href="https://example.com">Visit Example</a>
    <a href="https://openai.com">Visit OpenAI</a>
</body>
</html>
"""

# Parse the HTML
HTML_Soup = BeautifulSoup(html_content,'html.parser')


# Find all anchor tags
value = HTML_Soup.find_all('a')

# Print the URLs and link text
for i in value:
  print(f"Link is {i['href']} and text is {i.text}")


# XML Parsing

xml_content = """
<data>
    <person>
        <name>John Doe</name>
        <age>30</age>
    </person>
    <person>
        <name>Jane Smith</name>
        <age>25</age>
    </person>
    <person>
        <name>khaled yassen</name>
        <age>22</age>
    </person>
</data>
"""

# Parse the XML
XML_Soup = BeautifulSoup(xml_content,'xml')

# Find all 'person' elements
person_ = XML_Soup.find_all('person')
# print(person_)

# Extract the name and age for each person tag
for person in person_:
  name = person.find('name').text
  age = person.find('age').text
  print(f"Name is {name} and Age is {age}")


#################################################################  JSON parsing #############################################################

import json

json_string = '''
{
    "person": {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "Wonderland",
            "zipcode": "12345"
        },
        "hobbies": ["reading", "gardening"]
    },
    "company": {
        "name": "TechCo",
        "employees": [
            {"name": "Bob", "position": "Developer"},
            {"name": "Charlie", "position": "Designer"}
        ]
    }
}
'''

#  If you have the json file so 
# with open('test2.json', 'r') as file:
#     data = json.load(file)

data = json.loads(json_string)
# # Accessing nested structures
# person_name = data["person"]["name"]
# person_city = data["person"]["address"]["city"]
# person_hobbies = data["person"]["hobbies"]

# company_name = data["company"]["name"]
# employee_names = [employee["name"] for employee in data["company"]["employees"]]

# print(f"Person: {person_name}, City: {person_city}, Hobbies: {person_hobbies}")
# print(f"Company: {company_name}, Employees: {employee_names}")


# Open the JSON file
with open('test.json', 'r') as file:
    # Load JSON data from the file
    data = json.load(file)

result = data['results'][0]['geometry']
print(result['lat'])
print(result['lng'])


# CSV Parsing


import csv
# For reading the content of the CSV file 
with open('learn_pars.csv', 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV
    for row in csv_reader:
        # Each row is a list of fields (columns)
        print(row)
        # pass

# Open the CSV file
with open('learn_pars.csv', 'r') as file:
    # Create a CSV reader with a header
    csv_reader = csv.DictReader(file)

    # Iterate over each row in the CSV
    for row in csv_reader:
        # Each row is a dictionary with headers as keys
        # print(row)
        pass

# For writing content for the file.csv

import csv

# Data to be written to CSV
data = [
    ['Name', 'Age', 'City'],
    ['John', 28, 'New York'],
    ['Alice', 22, 'San Francisco'],
    ['Bob', 35, 'Los Angeles']
]

# Open or create a CSV file for writing
with open('learn_pars.csv', 'w', newline='') as file:
    # Create a CSV writer
    csv_writer = csv.writer(file)

    # Write the data to the CSV file
    csv_writer.writerows(data)
