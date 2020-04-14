## Hello World in Flask

```
from flask import Flask

app = Flask(__name__)

@app.route('/')  # using route decorator
def home():
    return "Hello, World"

app.run(port=5000)


```