## Installing Flask

```
pip3.5 install flask
```

```
# POST - used to recieve data
# GET  - used to send data back only
```

```python
# All classes in python starts with a capital letter - here Flask is a class and flask is a package
from flask import Flask,jsonify,request,render_template

# __name__ is a variable. It essentially gives each file a unique name. So this Flask object gets a unique name 
# Here you are creating an object of class Flask
app = Flask(__name__)

# Dictionary inside a list example shown below
# Here stores is a list which is referred as []. This list has a dictionary which is referred as {}
# Similiarly items is a list and it has a dictionary
stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]

#GET means send data to the browser. You can send HTML or json data 
#@app.route('/') is called a decorator in python
@app.route('/')
def home():
  return render_template('index.html')

#POST means receive data and use it.
#post /store data: {name :}
#To recieve the data we need request package which is imported
#new_store is a dictionary
#request.get_json converts JSON to python dictionary
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)
  #pass

# get /store/<name> data: {name :}
# URL: http://localhost/store/My Store 
@app.route('/store/<string:name>')
# get_store(name) -> name = some_name
def get_store(name):
# Iterate over the stores which is a list data structure
# If the store name matches return the store
# If the store name does not match then respond with 'store not found'
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': 'store not found'})
  #pass

# get /store
# URL - http://localhost/store
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})
  #pass

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})
  #pass

# get /store/<name>/item data: {name :}
# URL: http://localhost/store/My Store/item 
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})

  #pass

app.run(port=5000)

```

## To run the code

```
python 3.5 app.py
```

## Calling the above API using javascript from client side 

### The XMLHttpRequest object is a developers dream, because you can:

	#### Request data from a server - after the page has loaded
	#### Receive data from a server  - after the page has loaded
	#### Send data to a server - in the background

```

<html>
<head>
<script type="text/javascript">
    function httpGetAsync(theUrl, callback) {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                callback(xmlHttp.responseText);
        }
        xmlHttp.open("GET", theUrl, true); // true for asynchronous
        xmlHttp.send(null);
    }
    <!-- calling the api ->
    httpGetAsync('http://127.0.0.1:5000/store', function(response) {
        alert(response);
    } )
</script>
</head>
<body>

<div id="myElement">
    Hello, world!
</div>

</body>
</html>

```
