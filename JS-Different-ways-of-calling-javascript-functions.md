/*-------------Traditional Functions ---------------*/

```Javascript
function plus(a,b){
	return (a+b);
}
plus(2,2);
```

---

/*-------------------Anonymous functions-----------*/

//this is called anonymous function because you do need to provide a name for it

```Javascript
var plus = function(a,b){
	return console.log(a+b);
}(2,2);
```

---

/*------------------Anonymous Closure-----------------*/

//this function will self execute itself and not necessary to call seperately

```Javascript
(function()) {
	console.log('foo');
})();
```

---

/*------------------Creating namespace modules-------------------*/

// Here ray is the namespace
//arguments are inbuilt variable of Javascript
// The below code will print 'howdy'

```Javascript
var ray = (function() {

  return {
    speak: function() {
      console.log(arguments[0].say);
    },
     
    run: function(){
      console.log("How are you");
    } 

  }
	
})();
```

---

//How to call the above function in HTML file

```Javascript
<script>
  ray.speak({say: 'howdy'});
  ray.run();
</script>
```

---

/*----------------Returning multiple values from a function-------*/

//Return itself is a function in javascript

```Javascript

function plus(a,b) {
	return (
       console.log(a+b);  //prints 4
       console.log(this),  //will print global window object
       console.log(arguments), //will print [2,2]
       console.log("How are you") 
	)
}

plus(2,2);

```

---

/*--- creating an object in JAVASCRIPT----*/

```Javascript

var info = {
full_name : "Jeril",
title: "Staff Author",
links : [
  {blog  : "http://google.com" },
  {twitter: "http://twitter.com"}
]
};

```

---

/*------Functions inside objects ------ */

```Javascript

var calc = {
  status: 'Awesome',
  plus: function (a,b) {
    return (
       console.log(this),  //returns local object
       console.log(a+b),   //returns 4
       console.log(arguments), //returns [2,2]
       console.log(this.status) //returns awesome
    )
  }
}

calc.plus(2,2);

```

---

/*------constructor function in JS --------*/

```Javascript

var Dog = function(){
   var name, breed;
}

firstDog = new Dog;
//you can also call like this with paranthesis, firstDog = new Dog() but paranthesis is optional.
firstDog,name = "Rover";
firstDog.breed = "Doberman";

secondDog = new Dog;
secondDog.name = "Fluffy";
secondDog.breed = "Poodle";

console.log(firstDog.name);

console.log(secondDog.name);

```

---

/*-------------------Inheritance & Prototype in Javascript------------------*/

```Javascript

var speak = function(saywhat) {
   console.log(saywhat);
}

var Dog = function(){
  var name, breed;
}

var Cat = function() {
  var name, breed;
}

//here the Dog object is inheriting the functionality of speak function
//cat object is inheriting the functionality of speak function. 
//Now it is not necessary to recreate the same function seperately for Dog and Cat
//So using prototype you will be able to create a relationship between Dog and speak and similiarly for Cat and Speak.
Dog.prototype.speak = speak;
Cat.prototype.speak = speak;

//Dog
firstDog = new Dog;
firstDog.name = "Rover";
firstDog.breed = "Doberman";
firstDog.speak('woof');  //prints woof from speak function

//Cat
firstCat = new Cat;
firstCat.name = "Sniggles";
firstCat.breed = "Manx";
firstCat.speak('meow');  //prints meow from cat function

```

---

/*-----------------Using the arguments parameter in function--------------------- */

//If you notice the below function we are not passing any arguments inside function(). All arguments are stored in a Javascript reserved variable called arguments. 

```Javascript
var plus = function(){
	var sum = 0;
	for(var i = arguments.length -1; i >=0; i--) {
       sum += arguments[i];       
    }
  return sum;
}

console.log(plus(2,2,2,3,2,3,4))

Result : 18

```

/*-----------------Callback function in Javascript------------------------------*/

```Javascript

var x = function(){
  console.log("This is x function");
}

var y = function(n){
  console.log("This is y function");
  n();
}

y(x);

```

The above code can be written like this


```Javascript
function y(n, callback){
  console.log("This is y function" +n);
  callback();
}

y('apple', function() {
	console.log("this is the callback function");
});


```

---
