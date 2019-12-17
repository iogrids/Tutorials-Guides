# :beginner: How to use require in nodejs?

To require an module from npm use

```Javascript
  const fs = require('fs');
```

To require a custom module created by me then

1. Create a file named notes.js in the root directory then use the following code in index.js which is your entry file

const notes = require('./notes.js')

In the notes.js file

```Javascript
console.log('Starting notes.js');
module.exports.age=25;
```

If you want the value 25 in index.js then add the following code in index.js

```Javascript
const notes = require('./notes.js')
console.log(`Hello ${notes.age}.`);   //this is an ES6 Syntax

So in ES6 you can call any variable like this ${variable}

```

To export functions written in notes.js add the below code

```Javascript
module.exports.addNote = function () {
   console.log('hello world');
   return 'New note';
}
```

You can also write the above code using arrow function as shown below. You are using => symbol instead of the keyword function

```Javascript
module.exports.addNote = () => {
   console.log('hello world');
   return 'New note';
}; 
```

To print the value from notes.js to index.js, write the below code in index.js

```Javascript
var res = notes.addNote();
console.log(res);
```

returns -> New note

---
