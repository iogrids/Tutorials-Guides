# :beginner: Parsing command line arguments

Here you are parsing command line argruments using process.argv. process is a global object in nodejs like windows in javascript

console.log(process.argv) - can be used to print the command line arguments

eg: node app.js jeril jose 

now process.argv can be used to parse jeril, jose seperately from the command line.

An excellent 3rd party library called yargs can also be used to parse command line arguments

### Yargs usage

```
npm install yargs@4.7.1 --save
4.7.1 is the version of yargs in the tutorial
```

Add the below code in app.js

```Javascript
const yargs = require('yargs');
const argv = yargs.argv;
```

Yargs can be used to parse key value pairs from command line argruments

eg:

```Javascript
node app.js add --title=secrets
```
