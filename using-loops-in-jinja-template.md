## How to use if-loop and for-loop in HTML using jinja template

```
 from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')  # using route decorator
  def home():
      puppies = ['Fluffy', 'Rufus', 'Spike']
      return render_template('basic.html',puppies=puppies)

  if __name__ == '__main__':
      app.run(debug=True)
```

Calling the variable in HTML file

```
<!DOCTYPE html>
<html>
<body>  
  
  <ul>
    <!-- in Jinja templates for for loop use % symbol -->
    {% for pup in puppies %}
      <li> {{pup}} </li>
    {% endfor %}
  </ul>

  {% if 'Rufus' in puppies %}
     <p>Found you Rufus!</p>
  {% else %}
    <p> Rusus is not in this list </p>
  {% endif %}

</body>
</html>

```

Result

Fluffy
Rufus
Spike

Found you Rufus!
