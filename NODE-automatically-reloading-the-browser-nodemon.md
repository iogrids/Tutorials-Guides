## :beginner: To automaically reload the browser 

   If you make any changes to your node application and if you want to automatically reload the web server use nodemon. We will using nodemon only during local development and not in production.

  nodemon is a command line utility and not a npm package.

To install any command line utilities use the code below. -g install the utility as a global object and not specific to a project. -g also means you can use the package anywhere in your machine and for all the projects

```
npm install nodemon -g

```

To run the project use the code below

```
nodemon app.js
```
