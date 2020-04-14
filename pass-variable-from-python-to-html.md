## How to pass a variable from python code to the HTML file.

```
from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')  # using route decorator
  def home():
      some_variable = "Jose"
      pup_dictionary = {'pup_name': 'sammy'}
      return render_template('basic.html',my_variable=some_variable, pup_dictionary = pup_dictionary)

  if __name__ == '__main__':
      app.run(debug=True) 

```

Calling the variable in HTML file

```
<!DOCTYPE html>
<html>
<body>  
  <h1>Hello! {{my_variable}}</h1>
  <h1>{{pup_dictionary['pup_name']}} </h1>
</body>
</html>
```

Result: 

Hello! Jose

You can also apply python logic in HTML file like {{my_variable[0]}}
