## Block Elements and Inline Elements

In HTML there are block elements and inline elements

```
<h1> and <p> tags are examples of block elements. 

<img> <a href>, <strong> and <em> are examples of inline elements. 

```

You cannot set height and width for inline elements.

Block elements are stacked vertically one after another.

Inline elements are stacked vertically one aside another. 

![alt text](images/block-inline-elements.jpg "Block and Inline elements")


#### What are block level elements and Inline elements?

```<h1>``` is a block level element by default
```<span>, <a>``` etc. is a inline level element.

Now lets take this ```<h1>``` tag

```<h1>This is a simple text</h1>```

The above ```<h1>``` tag is a block level element and it will take full width of the browser or parent DIV.

Now if you make it like this

```<h1>This is a <span>simple<span> text</h1>```

and if you write the CSS as

```
span{
	display: block;
}
```

The above text would be printed like this

This is a - Line 1
Simple - Line 2
text - Line 3

Now ```<span> simple </span>``` is a block level element and it will take full width of the parent DIV thus takes the next line and "text" is moved to the third line.

Inline element do not take full width rather it takes only the corresponding text width.

For a block level element you can mention width and height as well as margin and padding, left, right, top and bottom.

Inline elements by default do not take any sort of width and you cannot assign them a width like shown below

```
span{
	width: 100% -> this is wrong and nothing will happen here
}
```

Inline elements also cannot have height, margin, top, bottom or padding.

So for an inline element if you want to set padding and margin, set it as inline-block.

eg:

```
span{
	display: inline-block; // not you can set margin, padding etc
}
```

It also dosen't force a line break since all block level elements will force a line break since it takes full width.
   

---
