## How to connect flask to an HTML file using render_template

1. Create a folder called templates
2. Create a file called basic.html inside the templates directory

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # using route decorator
def home():
    return render_template('basic.html')

if __name__ == '__main__':
    app.run(debug=True)

```

Flask will automatically look for HTML templates in the templates directory
We can render templates by the using the render_template function