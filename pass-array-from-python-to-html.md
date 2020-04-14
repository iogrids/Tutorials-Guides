## How to pass arrays from python code to the HTML file.

```
 from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')  # using route decorator
  def home():
      mylist = [1,2,3,4,5]
      return render_template('basic.html',mylist=mylist)

  if __name__ == '__main__':
      app.run(debug=True)

```

Calling the variable in HTML file

```
<!DOCTYPE html>
<html>
<body>  
  
  <h1> {{mylist}} </h1>
  <ul>
    <!-- in Jinja templates for for loop use % symbol -->
    {% for item in mylist %}
      <li> {{item}} </li>
    {% endfor %}
  </ul>

</body>
</html>

```

Result:
[1,2,3,4,5]

* 1.
* 2.
* 3.
* 4.
* 5.