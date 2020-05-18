When you work with JSON, there are basically two kinds of function

1. Parsing functions            - used to parse text into JSON  [These functions are used load(), loads() ]
2. Serialization functions      - used to serialize an object into JSON [These functions are used dump(), dumps() ]


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


# Convert python data to JSON data - Example


```python

# use the JSON module
import json


def main():
    # define a python ditcionary
    pythonData = {
        "sandwich": "Reuben",
        "toasted": True,
        "toppings": ["Thousand Island Dressing",
                     "Sauerkraut",
                     "Pickles"
                     ],
        "price": 8.99
    }

    # TODO: serialize to JSON using dumps
    # converts the above python object to JSON string
    
    jsonStr = json.dumps(pythonData)
    

    # TODO: print the resulting JSON string
    print("JSON Data: --------")
    # indent=4, will format the JSON data and show the results in a clean manner
    print(jsonStr, indent=4)
    

if __name__ == "__main__":
    main()
```