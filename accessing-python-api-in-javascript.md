# Accessing python API in javascript file using fetch

```

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# CORS(app)


@app.route('/')  # using route decorator
@cross_origin()
def home():
    return jsonify({'data': 'Welcome Jeril'})


if __name__ == '__main__':
    app.run(debug=True)
    
```

# Javascript Code

How to access the above json in HTML

```
<body>
<h1 id="display"> Display some test </h1>

<script>
fetch('http://localhost:5000/')
.then(function(response) {
    return response.json();
})
.then(function(myJson) {
    document.getElementById('display').innerHTML = myJson['data'];
})

</script>
</body>
```