## Understanding the float and clearfix property

![alt text](images/float-left-1.png "floating a DIV")

After giving float:left then it would look like this but see the yellow box also has moved to the right side. 

![alt text](images/float-left-2.png "floating a DIV")

To resolve such issue use clearfix property shown below

![alt text](images/float-left-3.png "floating a DIV")

```
  .clearfix:after {
   content: "",
   display: table;
   clear: both;
}

```

---

/*---------------- CSS CODE -------------------------------*/

```
	.div1{
		float:left;
		width:50%;
		background-color: green;
	}

	.div2{
		float: left;
		width:50%;
		background-color: red;
	}

	.clearfix:after {
		content: "";
		display: table;
		clear: both;
	}
	
```


/*-----------------------HTML CODE ---------------------*/


```	
<div class="div1">		
	<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
</div>
```


```
<div class="div2">
	<p>Contrary to popular belief</p>
</div>
```

```
<div class="clearfix"></div>
```

```
<div class="div3">
	<p>This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. </p></div>
```

---

[![CSS Floating Elements](http://img.youtube.com/vi/xara4Z1b18I/0.jpg)](http://www.youtube.com/watch?v=xara4Z1b18I)

