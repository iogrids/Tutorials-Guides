# This is an example of using voluptuous library for validation. 

Documentation: https://github.com/alecthomas/voluptuous

### this is how validation can be used in the main file

### Copy the below file in app.py and execute the file

``` python
from validators import comment_schema, employee_schema

thisdict = [{ 
  "q": "Ford",
  "per_page": 10  
}]

employees = [{
    "name": "jeril",
    "age": 37,
    "sex": "male"
}]

comment_schema(thisdict)

employee_schema(employees)

```

# For validation create a script called validators.py and copy and paste the code below

```python

from voluptuous import Schema, Required, All, Length, Range

# schema for validating comments
# this only validates whether the values are string or integer
comment_schema = Schema({
   'q': str,
   'per_page': int,
   'page': int,
})

# schema for validating employees
# this only validates whether the values are string or integer
employee_schema = Schema({
   'name': str,
   'age': int,
   'sex': str,
})

# For various other validation styles refer the documentation mentioned above

# To use the below ```from voluptuous import Required, All, Length, Range```
# Here q, per_page are required. This is been checked by Required library. Range library is also used
comment_schema2 = Schema({
    Required('q'): All(str, Length(min=1)),
    Required('per_page', default=5): All(int, Range(min=1, max=20)),
    'page': All(int, Range(min=0)),
})

comment_schema = Schema([comment_schema])
employee_schema = Schema([employee_schema])

```