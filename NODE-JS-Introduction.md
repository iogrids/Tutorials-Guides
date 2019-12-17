# :beginner: Introduction

Ryan Dahl first introduction of Node.js

https://www.youtube.com/watch?v=jo_B4LTHi3I

---

## what is javascript inside nodejs?

functions, addition, numbers, strings, arrays, objects

---

## What is not javascript inside nodejs?

Networking, HTTP server, TCP server, stdout(printing the information from the server) - all these are not part of javascript

---

## What is node.js?

Node.js is a c++ application that embeds the v8 js engine

```Javascript
eg: #include <v8.h>
```

## To execute node:

```Javascript
node index.js
```

## To setup node

Before creating a node application it is always better to create a package.json file using the below code

```Javascript
npm init
```

## To install a module and save it to package.json file

```Javascript
npm install express@4.14.0 --save
```

--save flag adds the express dependency in package.json file. Then express module is stored in node_modules folder inside thw working directory. If you want to migrate the code to a different platform, it is not necessary to copy the node_modules folder. 
