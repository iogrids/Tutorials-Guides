## &#x1F4D7; Selecting DOM elements in D3

You can refer the below section to select HTML dom elements in D3. Selecting an element is provided by default in D3 and it is not necessary to use JQuery selector to select elements in D3

```
<body>

<div class="container">
	<h2>D3 Graphic</h2>
	<section id="chart">
		<div class="item">John</div>
		<div class="item">James</div>
		<div class="item">Jeril</div>
		<div class="item">Jose</div>
		<div class="item">Jany</div>
	</section>
</div>

<script src="https://d3js.org/d3.v5.min.js"></script>

<script>
	

</script>
</body>
```

## &#x1F4D7; D3 DOM selector

Refer the below documentation on how to select DOM elements in D3

> :fire: [Selecting DOM elements in D3](https://github.com/d3/d3/blob/master/API.md#selecting-elements)

You can use the below methods to select a DOM element using D3

```Javascript
d3.select - select an element from the document.
d3.selectAll - select multiple elements from the document.
```

### Example:

//this will pick the first item i.e "John" and change the text "John" to "George"

```Javascript
 d3.select('.item').text('George')
 ```

//if you want to select all the items having the class "item" then you can use selectall

```Javascript
 d3.selectAll('.item').text('select')
 ```
 
// using id -> the below code selects "item" under "#chart"

```Javascript
d3.select('#chart .item').text('select')
d3.selectAll('#chart .item').text('select')
```

//the below code will select the second element which has the class name "item"
// to know more about nth child selector you can [click here](https://css-tricks.com/how-nth-child-works/)

```Javascript
d3.select('.item:nth-child(2)').text('select')
```

//this will select every other odd elements

```Javascript
d3.select('.item:nth-child(odd)').text('select')
```
//this will select every element after the 3rd element including the 3rd element

```Javascript
d3.select('.item:nth-child(n+3)').text('select')
```

//this will select the 2nd element and every other element after that

```Javascript
d3.select('.item:nth-child(2n)').text('select')
```

---

## &#x1F4D7; Working with HTML DOM Elements using D3(Inserting, appending, removing HTML elements)

So how do you insert HTML elements like ```<div>```, ```<span>``` inside the DOM?

```
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>

<div class="container">
	<h2>D3 Graphic</h2>
	<section id="chart">
		<div class="item">John</div>
		<div class="item">James</div>
		<div class="item">Jeril</div>
		<div class="item">Jose</div>
		<div class="item">Jany</div>
	</section>
</div>
<script src="https://d3js.org/d3.v5.min.js"></script>

<script> 

//write code to insert, append or remove here

</script>

```

:fire: Using the append functionality

```Javascript
<script>
d3.select('.item')   //selects the element with the class name .item, similiarly you can use #chart
  .append('div')
  .html('<strong>selection</strong>')
</script>

</body>
</html>
```

:fire: Using the insert functionality - To Insert a DOM element in-between another DOM element

```Javacript
d3.select('#chart')   
  .insert('span', ':nth-child(3)')
  .html('<strong>selection</strong>')
```

:fire: Using the remove functionality - To Delete a DOM element

```Javascript
d3.select('#chart .item:nth-child(3)')
  .remove()
```

### BROWSER OUTPUT: 

A new element named selection is added

* John
* **selection**
* James
* Jeril
* Jose
* Jany

### HTML OUTPUT for APPEND: 

The above code selects the first item and creates a ```<div>``` under it and then creates a ```<strong>``` element under the ```<div>```

```
  <div class="item">John</div>  
  <div>
   	 <strong>selection</strong>
  </div>
  <div class="item">James</div>
  <div class="item">Jeril</div>
  <div class="item">Jose</div>
  <div class="item">Jany</div>
```

---

## &#x1F4D7; Working with CSS and styling - 

You can style elements using the ```attr()``` method of D3. You can also control any element using ATTR method

```Javascript
d3.selectAll('.item')
  .attr('class', 'highlight')
```

```Javascript
d3.selectAll('.item:nth-child(3)')
  .attr('class', 'highlight')
```

#### CSS

```
.highlight{
  color: #C64C6F
  font-weight: 600;
}
```

You can also style directly like shown below.
//style is an object {}

```Javascript
d3.selectAll('.item:nth-child(3)')
  .style({
     'background': '#268BD2',
     'padding' : '10px',
     'margin' : '5px',
     'color' : '#EEE8D5'
  })
```

---

## &#x1F4D7; Binding data to the DOM

Here we will see on how to use the ```data()``` function in data.js

### HTML Structure

```
<section id="chart">
   <div class="item">John</div>
   <div class="item">James</div>
   <div class="item">Jeril</div>
   <div class="item">Jose</div>
   <div class="item">Jany</div>
</section>

```

### Javascript Code

```Javascript

var myStyles = [
  '#A57706',
  '#BD3613',
  '#D11C24',
  '#C61C6F',
  '#595AB7',
  '#2176C7'
];


//Here style is a function which takes 2 paramaters. The first parameter is 'background' and the second parameter is function.

// function(d) -> d contains what is passed inside .data i.e myStyles
// It becomes like this style = background: #A57706, background: #BD3613. So here the first ```<li>``` tag gets #A57706 color, the second ```<li>``` tag gets #BD3613 color etc.

d3.selectAll('.item')
  .data(myStyles)
  .style('background', function(d) {
    return d
  })
  
// Now in the above you are only passing a single variable which is background, in the below code lets see how to pass an object
  
//In myStyles you are passing multiple objects {}, {}

var myStyles = [
  { width: 200,
    color: '#A57706'},
  { width: 230,
    color: '#BD3613'},
  { width: 220,
    color: '#D11C24'},
  { width: 290,
    color: '#C61C6F'},
  { width: 236,
    color: '#595AB7'},
  { width: 230,
    color: '#2176C7'}
];  
   

// In style function you are passing a set of objects {}, {}, {}. style({}, {} ,{})
// Remember an object can have variables and functions
// myStyles is passed to data as data(myStyles) and you can access the values inside myStyles as ```myStyles.color``` or ```myStyles.width```
// function(d) -> d contains the value inside the data function ie. ```data(myStyles)```

d3.selectAll('.item')
  .data(myStyles)
  .style({
     'color'; 'white',
     'background' : function(d) {
        return d.color;
   },
    width: function(d) {
      return d.width + 'px';
    }
  })
  

```

---

## &#x1F4D7; Creating DIV elements dynamically without using HTML tags

In the earlier section we created various DIV elements under ```<section id="chart">```. Refer the code below

```
<section id="chart">
   <div class="item">John</div>
   <div class="item">James</div>
   <div class="item">Jeril</div>
   <div class="item">Jose</div>
   <div class="item">Jany</div>
   <div class="item">George</div>
</section>
```

Now in this section we are not going to create those ```<DIV>``` elements dynamically and our HTML code looks like shown below

```
<section id="chart">

</section>
```

#### D3.JS Code

Here we put those contents in HTML inside the below javascript object. We will be using the ```enter()``` function to insert HTML elements dynamically.

```Javascript

var myStyles = [
  { width: 200,
    name: 'John',
    color: '#A57706'},
  { width: 230,
    name: 'James',
    color: '#BD3613'},
  { width: 220,
    name: 'Jeril',
    color: '#D11C24'},
  { width: 290,
    name: 'Jose',
    color: '#C61C6F'},
  { width: 236,
    name: 'Jany',
    color: '#595AB7'},
  { width: 230,
    name: 'George',
    color: '#2176C7'}
];  

//```enter()``` function goes through all pieces of data and adds a ```<DIV>``` whenever we're entering one of these pieces of data

//the below code says d3, select the chart element and bind DIV's inside the chart element. The DIV's are inserted by the ```enter()``` function. So selectAll selects all the DIV which is created by the ```enter()``` function.

d3.selectAll('#chart').selectAll('div')
  .data(myStyles)
  .enter().append('div') //goes through all pieces of data and enters a DIV
  .classed('item', true) //true toggles the item class on - highlights the item which is hovered
  .text(function(d) {
     return d.name;
   }
  .style({
     'color'; 'white',
     'background' : function(d) {
        return d.color;
   },
    width: function(d) {
      return d.width + 'px';
    }
  }).exit() // exit function is always used when an enter command is used.

```

// The above code will create a ```<DIV>``` like shown below

```
<section id="chart">
  <div class="item" style="color:white; width:200px; background:#A57706"> John </div>
  <div class="item" style="color:white; width:230px; background:#BD3613"> James </div>
  <div class="item" style="color:white; width:220px; background:#D11C24"> Jeril </div>
  <div class="item" style="color:white; width:220px; background:#C61C6F"> Jose </div>
  ...
  ...
</section>
```
