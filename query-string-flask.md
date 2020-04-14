## Using query string in Flask

It retrieves value from the query string and based on it the result is returned

# TODO 

  http://localhost:5000/query_example?language=Python

  Result: The language is Python

```
from flask import Flask, request

app = Flask(__name__)

@app.route('/query_example')
def query_example():
    language = request.args.get('language')
    return '<h1> The language is : {language}</h1>'.format(language)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```