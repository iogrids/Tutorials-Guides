## :beginner: Design pattern - Organizing your code in nodejs - This design pattern is similiar to closure

//code for app.js which is the entry file

```Javascript
//include notes.js external javascript file
console.log('Starting app.js');
const notes = require('./notes.js')

  notes.add(2,3);

  notes.sub(5,3);
```


//code for notes.js which is included in app.js

```Javascript
console.log('Starting notes.js');

var add = (num1, num2) => {
  console.log('Total', num1 + num2);
};

var sub = (num1, num2) => {
  console.log('Difference', num1 = num3);
};

module.exports = {
  add,
  sub
};

```

//you will have to run the code like this

```
node app.js -> 
```

---
