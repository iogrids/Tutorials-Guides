## Designing the Features Section

What are we going to build?

Output: 

![Features Section](images/features.png "Final Result")

Now the header part is over

```
<header> 
  
  ...//code here
  
</header>
```

HTML has an element called section. 

Now lets design the HTML for the above layout

We also use icons from http://ionicons.com. To use ionicons download ionicons.min.css and include it in css folder.Also download icon fonts of ionicons.

## HTML SECTION

```
<section class="section-features">
 <div class="row">
    <h2>Get food fast &amdash; not fast food </h2>
    <p class="long-copy">Hello, we're Omnifood, your new premium food delivery service. We know you're always busy. No time for cooking. So let us take care of that, we're really good at it, we promise!
    </p>
 </div>

 <div class="row">
   <!-- refer grid.css, col and span-1-of-4 are set in those files -->
   
   <!-- column 1 -->
    <div class="col span-1-of-4 box">
      <i class="ion-ios-infinite-outline icon-big"></i>
      <h3>Up to 365 days/year</h3>
      <p>Never cook again! We really mean that. Our subscription plans include up to 365 days/year coverage. You can also choose to order more flexibly if that's your style. 
      </p>      
    </div>
      
     <!-- column 2 --> 

    <div class="col span-1-of-4 box">
      <i class="ion-ios-stopwatch-outline icon-big"></i>
      <h3>Ready in 20 minutes</h3>
      <p>Never cook again! We really mean that. Our subscription plans include up to 365 days/year coverage. You can also choose to order more flexibly if that's your style. 
      </p>      
    </div>

     <!-- column 3 -->

     <div class="col span-1-of-4 box">
      <i class="ion-ios-nutrition-outline icon-big"></i>
      <h3>100% organic</h3>
      <p>Never cook again! We really mean that. Our subscription plans include up to 365 days/year coverage. You can also choose to order more flexibly if that's your style. 
      </p>      
    </div>

    <!-- column 4 -->

    <div class="col span-1-of-4 box">
      <i class="ion-ios-cart-outline icon-big"></i>
      <h3>Order anything</h3>
      <p>Never cook again! We really mean that. Our subscription plans include up to 365 days/year coverage. You can also choose to order more flexibly if that's your style. 
      </p>      
    </div>

 </div>

</section>
```

## CSS SECTION

Steps:

## Step 1:

/*-----------PUT THE GLOBAL STYLES ----------*/

```
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
 }


 html {
  background-color: #fff;
  color: #555;
  font-family: 'Lato', 'Arial', sans-serif;
  font-weight: 300;
  font-size: 20px;
  text-rendering: optimizeLegibility;  //using this is a good practise
 }
 
```

 /*-------- Styling the row -------*/

```
.row {
  max-width: 1140px;
  margin: 0 auto;
}
```

## Step 2:

/*------ Styling the ```<section>``` -------*/
  
```
section {
  padding: 80px 0;
}
```

/*------ styling the ```<h2>``` tag -------*/

```
h2 {
  font-weight: 300;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 180%;
  word-spacing: 2px;
  text-align: center;
  margin-bottom: 30px;
}
```

/*-----to put a small line below the ```<h2>``` tag -----*/

```
  h2:after {
   display:block;
   height: 2px;
   background-color: #e67322;
   content: " "; // this is mandatory. It refers to what content should be put
   width: 100px;
   margin: 0 auto; //to center the line
   margin-top: 30px; //margin between the h2 tag and the small line
}
```

/*----- Designing the .long-copy ------*/

```
.long-copy {
  line-height: 145%;
  width: 70%; 
  margin-left: 15%;
}
```

/*----- Designing the .box section ------*/

```
.box{
  padding: 1%;
}
```

/*----- Designing the ```<h3>``` element ------*/

```
h3{
  font-weight: 300;
  text-transform: uppercase;
  font-size: 100%;
  margin-bottom: 15px;
}
```

/*------- Designing all the paragraphs inside the box -------*/

```
.box p{
  font-size: 90%;
  line-height: 145%;  
}
```

/*----- Designing the ICONS -------*/

```
.icon-big {
  font-size" 350%;
  display: block;
  color: #e67e22;
  margin-bottom: 10px;
}
```
