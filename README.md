# AirBnB_clone

The AirBnB clone project starts now until the end of the first year. The goal of the project is to deploy on your server a simple copy of the <a href="https://www.airbnb.com/">AirBnB website.</a>

## Steps

### `The console`

- create your data model.
- manage (create, update, destroy, etc) objects via a console / command interpreter.
- store and persist objects to a file (JSON file).

![The console](https://github.com/danaelshrbiny10/AirBnB_clone/assets/54659424/66abac04-da73-4e91-9747-f1ef3e51adf2)

### `Web static`

- learn HTML/CSS.
- create the HTML of your application.
- create template of each object.

![Web static](https://github.com/danaelshrbiny10/AirBnB_clone/assets/54659424/3a09f8aa-43db-408e-89b9-b13341a97a3a)

### `MySQL storage`

- replace the file storage by a Database storage.
- map your models to a table in database by using an O.R.M.

![MySQL storage](https://github.com/danaelshrbiny10/AirBnB_clone/assets/54659424/d82d9d3a-674a-480c-bc5b-b451f54b9fe6)

### `Web framework - templating`

- create your first web server in Python.
- make your static HTML file dynamic by using objects stored in a file or database.

![Web framework - templating](https://github.com/danaelshrbiny10/AirBnB_clone/assets/54659424/ed359454-5993-482b-804b-d348bb769fc8)

### `RESTful API`

- expose all your objects stored via a JSON web interface.
- manipulate your objects via a RESTful API.

![RESTful API](https://github.com/danaelshrbiny10/AirBnB_clone/assets/54659424/52ebf658-4899-4764-8ee3-ef56668d475c)

### `Web dynamic`

- learn JQuery.
- load objects from the client side by using your own RESTful API.

![Web dynamic](https://github.com/danaelshrbiny10/AirBnB_clone/assets/54659424/8a459893-da68-4006-99fd-1d7265054193)

## Files and Directories

- `models` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- `tests` directory will contain all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
  - attributes: `id`, `created_at` and `updated_at`
  - methods: `save()` and `to_json()`
- `models/engine` directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

## Storage

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

## How can I store my instances?

```bash
class Student():
    def __init__(self, name):
        self.name = name

students = []
s = Student("John")
students.append(s)
```

Here, I’m creating a student and store it in a list. But after this program execution, my Student instance doesn’t exist anymore.

```bash
class Student():
    def __init__(self, name):
        self.name = name

students = reload() # recreate the list of Student objects from a file
s = Student("John")
students.append(s)
save(students) # save all Student objects to a file
```

## `*args, **kwargs`

```bash
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")
```

But with this function definition, you must call my_fct with 2 parameters

```bash
def my_fct(*args, **kwargs):
    ...

my_fct("Best", "School")
```

## `datetime`

you create an instance of datetime with the current date and time.

```bash
from datetime import datetime

date_now = datetime.now()
print(type(date_now)) # <class 'datetime.datetime'>
print(date_now) # 2017-06-08 20:42:42.170922
```

date_now is an object, so you can manipulate it

```bash
from datetime import timedelta

date_tomorrow = date_now + timedelta(days=1)
print(date_tomorrow) # 2017-06-09 20:42:42.170922
```

you can also store it

```bash
a_dict = { 'my_date': date_now }
print(type(a_dict['my_date'])) # <class 'datetime.datetime'>
print(a_dict) # {'my_date': datetime.datetime(2017, 6, 8, 20, 42, 42, 170922)}
```

## `Data digram`

![Data digram](https://github.com/danaelshrbiny10/AirBnB_clone/assets/54659424/d4d58a7b-6a1c-4b03-b8aa-83129be474b8)
