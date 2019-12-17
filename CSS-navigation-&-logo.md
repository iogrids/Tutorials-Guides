## How to create a navigation & Logo
 
  Logo and Image will come on the same line. So put both image and logo in a row
  
  ![Menu and Logo](images/menu-logo.png "Menu and Logo")


```
<body>
	<header>		
		<nav>
           <div class="row">
              <img src="logo.png" alt="Logo" class="logo">

              <ul class="main-nav">
                  <li><a href="#">Food delivery</a></li>
                  <li><a href="#">How it works</a></li>
                  <li><a href="#">Our Cities</a></li>
                  <li><a href="#">Sign Up</a></li>
              </ul>
 
           </div>      
		</nav>
	</header>

</body>
```

CSS for Logo
/*always set image height as 100px and width you can set as auto. This will autoscale the image properly*/

```
.logo {
	height: 100px;
	width: auto;
	float: left;   /* put logo and menu in single row and float the logo to the left side */
	margin-top: 20px;
}
```

```
.main-nav{
	float: right /* put menu on the right side */
	list-style: none; /* <ul> tags comes with bullet points. So to remove bullet points use this tag */
        margin-top:55px;
	background-color: green;
}
```

```
.main-nav li{
   display: inline-block; /* <li> are by default block elements and change it to inline-block elements to display them side by side */
   margin-left: 40px; /* margin between each ```<li>``` tag */
 }
 ```

 /* code for the text or ```<a>``` tag and Writing effects for Menu */

```
 .main-nav li a:link,
 .main-nav li a:visited{
    padding: 8px 0; 
    color: #fff;
    text-decoration: none; /* to get rid of text underline */
    text-transform: uppercase
    font-size: 90% /* 90% of 20px which is defined in html{} */
    border-bottom: 2px solid transparent;
    transition: border-bottom 0.2s;
}
```

```
.main-nav li a:hover,
.main-nav li a:active{
     border-bottom: 2px solid #e67e22;
}

```
