## Rendering Dynamic HTML files and partials using handlebars in Nodejs

/* -----Partials are small piece of code. You break up your HTML file into various sections like header section, footer section etc so that it is easier to read ------- */

```Javascript
const express = require('express');
const hbs = require('hbs');

var app = express();

/* ---- In order to use partials you will have to use registerpartials and mention the directory where the partial is stored. Partial should always be stored inside /views/partials/header.hbs or footer.hbs etc ------ */
hbs.registerPartials(__dirname + '/views/partials')
app.set('view engine', 'hbs');
app.use(express.static(__dirname + '/public'));

/* if you want to print the return value of any function inside the hbs template then you can use registerHelper function */
/* In the template just call {{getCurrentYear}} to print the return value from the below function */

hbs.registerHelper('getCurrentYear', () => {
  return new Date().getFullYear()
});


/* If you want to pass value to a function then you can use registerHelper function like shown below */
/* You can call registerHelper function inside the template like this {{screamIt welcomeMessage}} welcomeMessage is the paramater that you will pass. welcomeMessage is passed and it is converted as uppercase and shown in the template*/

hbs.registerHelper('screamIt', (text) => {
  return text.toUpperCase();
});

app.get('/', (req, res) => {
  res.render('home.hbs', {
    pageTitle: 'Home Page',
    welcomeMessage: 'Welcome to my website'
  });
});

app.get('/about', (req, res) => {
  res.render('about.hbs', {
    pageTitle: 'About Page'
  });
});

// /bad - send back json with errorMessage
app.get('/bad', (req, res) => {
  res.send({
    errorMessage: 'Unable to handle request'
  });
});

app.listen(3000, () => {
  console.log('Server is up on port 3000');
});
```

/* ---------------home.hbs --------------------- */

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Some Website</title>
  </head>
  <body>
    {{> header}}

<!----- screamIt is a function and you are passing wlecomeMessage as the variable to screamIt function ----- !>
    
    <p>{{screamIt welcomeMessage}}</p>

    {{> footer}}
  </body>
</html>
```

/* -------------------------about.hbs ------------------- */

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Some Website</title>
  </head>
  <body>

    <!-- {{>}} - this is the way to mention a partial. Here you have included a header partial
     which is created inside views/partials/footer.hbs -->

    {{> header}}

    <p>Some text here</p>

   <!-- {{>}} - this is the way to mention a partial. Here you have included a footer partial
     which is created inside views/partials/footer.hbs -->

    {{> footer}}
  </body>
</html>
```

/* ---------------------------header.hbs -------------------- */

//this file is inside root/views/partials/header.hbs

```
<header>
  <h1>{{pageTitle}}</h1>
  <p><a href="/">Home</a></p>
  <p><a href="/about">About</a></p>
</header>
```

/* ------------------------ footer.hbs ------------------ */

//this file is inside root/views/partials/footer.hbs

```
<footer>
  <p>Created By Andrew Mead - Copyright {{getCurrentYear}}</p>
</footer>
```

/* -------------------- Executing the code using nodemon ---------------- */

> nodemon.server.js -e js,hbs

-e - mentions all the extensions that we should watch for change. So if you make changes in hbs file and js nodemon will watch for changes and auto reload the web server
