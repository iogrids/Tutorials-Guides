
## Rendering Dynamic HTML files in Nodejs

// Create a file called server.js


const express = require('express');

//the below code to require handlebars. 
// Install handlebars -> npm install hbs@4.0.0 --save
// https://www.npmjs.com/package/hbs

const hbs = require('hbs');

var app = express();

// app.set is used to set various express related configurations
// You are passing a key value pair inside app.set. Here key is 'view engine' and value is hbs
// hbs means handle bars. We are setting the engine to be handle bars using app.set
app.set('view engine', 'hbs');

app.get('/', (req, res) => {
	// if you want to render any of the template you have set up in your current view folder then you use ```res.render()```
	// if you want to just pass a text then you can use ```res.send()```
	// home.hbs is the name of the template that you want to render
  res.render('home.hbs', {
   // these are the variables that you want to render inside home.hbs
    pageTitle: 'Home Page',
    welcomeMessage: 'Welcome to my website',
    currentYear: new Date().getFullYear()
  });
});

app.get('/about', (req, res) => {
  res.render('about.hbs', {
  	// these are the variables that you want to render inside about.hbs
    pageTitle: 'About Page',
    currentYear: new Date().getFullYear()
  });
});

// /bad - send back json with errorMessage
app.get('/bad', (req, res) => {
	// if you want to just send a text to the browser then you can use ```res.send()```
  res.send({
    errorMessage: 'Unable to handle request'
  });
});

app.listen(3000, () => {
  console.log('Server is up on port 3000');
});

/* --------------------  */
Now create a folder named views inside the root directory
Views is the default directory that express uses for your templates
Create a file called abouts.hbs and home.hbs
/* -------------------- */

### about.hbs

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Some Website</title>
  </head>
  <body>
    /* rendering the pageTitle variable set inside server.js */
    <h1>{{pageTitle}}</h1>
    <p>Some text here</p>

    <footer>
    /* rendering the currentYear variable set inside server.js */
      <p>Copyright {{currentYear}}</p>
    </footer>
  </body>
</html>

### home.hbs   //index file

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Some Website</title>
  </head>
  <body>
    <h1>{{pageTitle}}</h1>
    <p>{{welcomeMessage}}</p>

    <footer>
      <p>Copyright {{currentYear}}</p>
    </footer>
  </body>
</html>
