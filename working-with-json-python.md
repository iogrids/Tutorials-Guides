When you work with JSON, there are basically two kinds of function

1. Parsing functions            - used to parse text into JSON  [ load(), loads() ]
2. Serialization functions      - used to serialize an object into JSON [ dump(), dumps() ]


# Python objects to JSON conversion/serialization

python converts or serializes object into JSON according to the following table

As shown in the table below 

    * python dictionary is converted to object in JSON
    * python strings are converted to Javascript strings in JSON

| Python Object          | JSON Representation |
|------------------------|---------------------|
| dict                   | object              |
| list, tuple            | array               |
| str                    | string              |
| int,long, float, Enums | number              |
| True                   | true                |
| False                  | false               |
| None                   | null                |


# JSON object to python conversion/serialization

JSON converts or serializes JSON object according to the following format

| JSON Data             | Python Object |
|-----------------------|---------------|
| object                | dict          |
| array                 | list          |
| string                | str           |
| Integer number        | int           |
| Floating point number | float         |
| true, false           | True, False   |
| null                  | None          |


# JSON to python Code

```python
def main():
    # define a string of JSON code
    jsonStr = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "toppings" : [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickles"
            ],
            "price" : 8.99
        }'''

    # TODO: parse the JSON data using loads
    # The below line will convert the above JSON object to python dictionary. 
    # Once converted to python dictionary you can use any python dictionary methods on it.
    
    data =  json.loads(jsonStr)

    # TODO: print information from the data structure


if __name__ == "__main__":
    main()


```