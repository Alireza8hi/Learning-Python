# JSON: JSON is a string for storing and exchanging data, between different languages for connecting server and client
# XML is something like JSON

# api: codes that receive data from database(mysql-sqlserver-...) in server, and give them to client with JSON,XML,...

"""    convert from Python to JSON:
Python	JSON
dict  ->	Object
list  ->	Array
tuple  ->	Array
str	  ->	String
int  ->	    Number
float  ->	Number
True  ->	true
False  ->	false
None  ->	null
"""

import json

x = '{"name":"John", "age":30, "city":"New York", "Teacher": true, "married": false, "lastname": null}'  # json(string)

y = json.loads(x)  # change json(string) to python(dictionary)

print(type(x))
print(type(y))
print(x)
print(y)

z = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "isTeacher": True,
    "isMarried": False,
    "lastname": None
}
w = json.dumps(z)  # change python(dictionary) to json(string)
w2 = json.dumps(z, indent=2)  # new point
w3 = json.dumps(z, indent=10)
w4 = json.dumps(z, indent=4, sort_keys=True, separators=("s", "s"), skipkeys=True)  # new points

print(type(z))
print(type(w))
print(z)
print(w)
print(w2)
print(w3)
print(w4)



print({"name": "John", "age": 30}, type({"name": "John", "age": 30}))
print(json.dumps({"name": "John", "age": 30}), type({"name": "John", "age": 30}))
print(["apple", "bananas"], type(["apple", "bananas"]))
print(json.dumps(["apple", "bananas"]), type(json.dumps(["apple", "bananas"])))
print(("apple", "bananas"), type(("apple", "bananas")))
print(json.dumps(("apple", "bananas")), type(json.dumps(("apple", "bananas"))))
print("hello", type("hello"))
print(json.dumps("hello"), type(json.dumps("hello")))
print(42, type(42))
print(json.dumps(42), type(json.dumps(42)))
print(31.76, type(31.76))
print(json.dumps(31.76), type(json.dumps(31.76)))
print(True, type(True))
print(json.dumps(True), type(json.dumps(True)))
print(False, type(False))
print(json.dumps(False), type(json.dumps(False)))
print(None, type(None))
print(json.dumps(None), type(json.dumps(None)))
