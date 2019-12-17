# ES6 ES7 ES8

## let, var and const

var does not have block level scoping so use let or const for block level scoping. Avoid using var always

use let, const instead of var

Reference video

https://www.udemy.com/es6-es7-and-es8-its-time-to-update-your-javascript/learn/v4/t/lecture/9673416?start=1065

## Template literals

```
const name = "Rob"
const hello = `Hello, ${name}`;
console.log(hello);

```
## Tagged templates

Tagged Templates transform a Template String by placing a function name before the template string.
Tagged templates is usually used to mix HTML and Javascript. 

Check the example here

https://github.com/jeriljose/Reference/blob/gh-pages/mixing%20javascript%20and%20HTML.md

or check this tutorial: https://www.udemy.com/es6-es7-and-es8-its-time-to-update-your-javascript/learn/v4/t/lecture/12174224?start=195 

Check the above video from 13:36

For example:

```
function doSomething() {
        return "Hello";
    }

    const name = "Kelvin";
    const food = "Rice";

    const sentence = doSomething`My name is ${name} and I love eating ${food}`;
    console.log(sentence);// "Hello"
```

Another example:

```
let harry = “How are you”
let lotr = “When Mr. Bilbo beggins of bag announced”
let orwell = “It was bright cold day in April”
let lines = {
   harry,
   lotr,
   orwell
];

function buildHTML(string, expr) {
   console.log(strings)
   console.log(expr);
}

const result = buildHTML ‘<li>${lines[0]}</li>’;

Result:

[‘<li>’,’</li’]  -> //console.log(strings)
How are you     -> lines[0] //console.log(lines[0])

```

For more information check here: https://dev.to/sarah_chima/tagged-template-literals-2ho
