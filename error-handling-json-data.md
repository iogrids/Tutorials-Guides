
There would be situations where the json object i.e jsonStr might not be properly formatted like missed strings or missed semi-colons etc. These kind of errors
should be catched and informed to the programmer where the error has occurred while running the code. To implement this we use JSONDecodeError.

The below code is an example on how to use JSONDecodeError and print where the error has occurred in the JSON object

```python
# use the JSON module
import json
from json import JSONDecodeError

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

    # parse the JSON data using loads
    try:
       data = json.loads(jsonStr)
    except JSONDecodeError as err:
       print("Whoops, JSON decoding error")
       print(err.msg)  # prints the error message
       print(err.lineno, err.colno)  # prints the line number and the column where the error ocurred
       

    # print information from the data structure
    print("Sandwich: " + data['sandwich'])
    if (data['toasted']):
        print("And it's toasted!")
    for topping in data['toppings']:
        print("Topping: " + topping)


if __name__ == "__main__":
    main()

```