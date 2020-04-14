## Dynamic routing in Flask - Routing based on query string

If app route is /puppy/tom
Result: This is a page for tom

If app route is /puppy/ginger
Result: This is a page for ginger

```
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}<h1>".format(name)

```