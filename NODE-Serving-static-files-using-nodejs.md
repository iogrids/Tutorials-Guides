## Serving a static directory of HTML files using nodejs

```Javascript

const express = require('express');

var app = express();

// Here we have create a file named help.html inside the public folder which is inside the working directory.  
// express.static is a built in middle ware function which is used to serve static files
// __dirname is a nodejs global object which returns the current working folder of the project
// public is where the static files are located. You can add as many static files like index.html, about.html, help.html
// you can access the static files like localhost:3000/help.html 

app.use(express.static(__dirname + '/public'));



app.get('/', (req, res) => {
  res.send('Welcome Page');
});


app.listen(3000, () => {
  console.log('Server is up on port 3000');
});

```
