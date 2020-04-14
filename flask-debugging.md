## Enable debugging in Flask

```
from flask import Flask

app = Flask(__name__)

@app.route('/')  # using route decorator
def home():
    return "Hello, World"

app.run(debug=True)


```