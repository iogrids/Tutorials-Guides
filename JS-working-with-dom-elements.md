## Working with text fields

```
<input type ="number" id="txt-a-bball" size="3" placeholder="0">
```

//To get the above element in javascript

```javascript
 document.getElementById('txt-a-bball') 
 ```

  returns
```
<input type ="number" id="txt-a-bball" size="3" placeholder="0">
```

//To get the value inside this input box use

```javascript

document.getElementById('txt-a-bball').value 

```

 returns the value inside the textbox

//You can also set the value like this

```javascript

document.getElementById('txt-a-bball').value = 4

```

---

## Working with forms

//If you want to print all the forms on the page, then use this

```javascript

document.forms[0]  -> prints the first form on the html file

```

returns

```

<form  class="cart" id="cart-hplus" method ="get" action="http://google.com">...</form>

```

//to access all the elements inside the form

```javascript

document.getElementById('cart-hplus').elements

```

returns

```

<input type ="number min="0" id="txt-q-bball" size="3">,
<input type ="number min="0" id="txt-q-bball" size="3">,
<input type ="number min="0" id="txt-q-bball" size="3">,

```

```javascript
document.getElementById('cart-hplus').elements[0] -> will return the first elements

```

returns

```

<input type ="number min="0" id="txt-q-bball" size="3">

```

---

## How to access dom element which does not have an id but has a name element

eg: 

<input type="radio" value="pickup" name="r_method" id="r-method-pickup" checked>

```javascript

document.getElementById('cart-hplus').r_method

```

returs

```
<input type="radio" value="pickup" name="r_method" id="r-method-pickup checked>,
<input type="radio" value="usps" name="r_method" id="r-method-usps">,
<input type="radio" value=ups" name="r_method" id="r-method-ups">
```

---

## Working with Select boxes

```
<select id="s-state">
  <option value="volvo">Volvo car</option>
  <option value="saab">Saab car</option>
  <option value="mercedes">Mercedes car</option>
  <option value="audi">Audi car</option>
</select>
```

How to access the value of a select box

```javascript
    
    document.getElementById('s-state').value
 
```

returns the current selected value in select box

returns -> Volvo if selected in the check box

you can also assign values

```javascript
   document.getElementById('s-state').value = "audi"
``` 

If you want to return all the options of a list box you can use the code below

```javascript
   document.getElementById('s-state').options
```

returns

```
  <option value="volvo">Volvo car</option>
  <option value="saab">Saab car</option>
  <option value="mercedes">Mercedes car</option>
  <option value="audi">Audi car</option>
```

If you want to return the selectedIndex of a select box like 1 for volvo, 2 for saab 3 for mercedes, use the code below

```javascript
document.getElementById('s-state').selectedIndex 
```

returns -> 1 if Volvo is selected, returns 2 if saab is selected and so on

You can use options and selectedIndex together if value is not available in certain browsers

```javascript
  
var selectedIdx = document.getElementById('s-state').selectedIndex;
var selectedValue = document.getElementById('s-state').option[selectedIdx].value;

```

---

### Working with Radio buttons and check boxes

#### Checkboxes

```
<input type="checkbox" value="apple" id="myCheck">
```

To return the value use the code below

```javascript
document.getElementById('myCheck').value -> returns
```
apple

To check whether the checkbox is checked use the code below

```javascript
document.getElementById('myCheck').checked   -> returns false if not checked and returns true of checked
```

To get the value of the checked radio button

#### Radio button

```
<input type="radio" value="apple" name="r_method" id="myCheck">
```

```javascript
document.querySelector('input[name=r_method]:checked') returns
```

```
<input type="radio" value="apple" name="r_method" id="myCheck">
```

To get the value

```javascript
document.querySelector('input[name=r_method]:checked').value
```

returns

apple

if you want to select all the radio buttons which has the same name property you can use querySelectorAll method

```javascript
document.querySelectorAll('input[name=r_method]') -> returns
```

```
<input type="radio" value="pickup" name="r_method" id="r-method-pickup checked>,
<input type="radio" value ="usps" name="r_method" id="r-method-usps">,
<input type="radio" value = "ups" name="r_method" id ="r-method-ups">
```

---

### Adding event listener

This code is used in situations like when a button is clicked. You can pretty much add an event listener to any element in DOM

<form class="cart" id="cart-hplus"> ... </form>

The below code takes two arguments first is the event (submit, or click or change) the second argument is the function that is to be executed when that event has happenned

```javascript
document.getElementById('cart-hplus').addEventListener('submit', function() { 
   //write function code here
}) -> used when form is submitted
```

```javascript
document.getElementById('cart-hplus').addEventListener('click', function() { ... }) -> used when a link is clicked
document.getElementById('cart-hplus').addEventListener('change', function() { ... }) -> used for text field
```

//submit is usually used when form is submitted
//click is usually used for a link and when link is clicked
//if it's a form field you can use change event i.e when user enters a value in a text box and tabs over to another textbox


The above code is used using a unnamed function, you can also use a named function like this

```javascript
document.getElementById('cart-hplus').addEventListener('submit', estimateTotal);

function estimateTotal (event){
   //event referes to the event that was fired i.e whether it is click or submit or change
   //The preventDefault() method is used to stop any element form behaving its default behaviour. 
   event.preventDefault(); // So now nothing will happen except for the functionality which is written here. Any default actions on the form will be restricted.
   console.log('You submitted the form.')
}
```

---

### How to validate input

```javascript
function estimateTotal (event){
   //event referes to the event that was fired i.e whether it is click or submit or change
   //The preventDefault() method is used to stop any element form behaving its default behaviour. 
   
   event.preventDefault(); // So now nothing will happen except for the functionality which is written here. Any default actions on the form will be restricted.
   
   if (document.getElementById('s-state').value === '') {  //check if empty
      alert('Please choose your shipping state');
      document.getElementById('s-state').focus(); // this focuses the corresponding element i.e s-state
   }
}
```

You can also use the below HTML code instead of using focus()

```
<select id="s-state" required>...</state>
```

---

### DOM Loading !important

When do you want your javascript to run..?Sometimes you want to run your javascript only after all the DOM elements are loaded

sometimes your script might run before the DOM element is defined and that will cause issues.. In this case you can use DOMContentLoaded event or $.ready

```javascript

document.addEventListener('DOMContentLoaded', function(){
        document.getElementById('cart-hplus').addEventListener('submit', estimateTotal);


     });


```

#### DOM Loading in JQuery - the same script using jQuery:

```javascript

jQuery.ready(function(){
  document.querySelector('#my-awesome-el').innerHTML = new Date
});

// OR

$(function(){
  document.querySelector('#my-awesome-el').innerHTML = new Date
});

```

---

### Disable a button in javascript

```javascript

//if dom content is loaded
document.addEventListener('DOMContentLoaded', function(){
        // when user submits the form. cart-hplus is the id of the form
        document.getElementById('cart-hplus').addEventListener('submit', estimateTotal);
        
        //the below code is used .. when the page loads button should be disabled immediately
        
        document.getElementById('btn-estimate').disabled = true; 
        
         //adding event listener to state field (select box). Every time state is changed we check for change and fire the function
      if(document.getElementById('s-state').addEventListener('change', function() {
            // if the checkbox element is not selected by the user and it is empty. s-state is the id of the select box
          if(document.getElementById('s-state').value === ''){
            //disable the button. btn-estimate is the id of the button
            document.getElementById('btn-estimate').disabled = true;
           } else {
            document.getElementById('btn-estimate').disabled = false;
          }
       });
  });
```

---

## To get the elements of DIV -> use innerHTML

```
<div class ="credits section light-padding">

  <div class="credits-inner section-inner">

   <!--/Re
    &copy; 2016 <a href="http://google.com" title="H+ Sport </a>

   <p> class="fright">
      <span> <a href="http://google.com">Lynda.com </a></span><a title="To the top" href="#" class="tothetop">Up!</a>
   <p>

  </div>
</div>
```

### To get the complete DIV

```javascript
document.querySelector('.credits .fright');
```
returns

```
 <p> class="fright">
       <span> <a href="http://google.com">Lynda.com </a></span><a title="To the top" href="#" class="tothetop">Up!</a>
 <p>
```

### To get the inner DIV of the parent DIV

```javascript
document.querySelector('.credits .fright').innerHTML; -> returns
```
```
<span> <a href="http://google.com">Lynda.com </a></span><a title="To the top" href="#" class="tothetop">Up!</a>
```

To get the text content -> will strip of all HTML tags and return the text content

```javascript
document.querySelector('.credits .fright').textContent;
```

returns Lynda.com - Up!

## To set the elements of a DOM element

```javascript
var results = document.getElementById('results');
results.innerHTML = 'Total items:' + 23;
```


