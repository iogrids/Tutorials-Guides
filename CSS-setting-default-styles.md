## Remove default margins 

All browsers set default margins for HTML elements if we dont specify any. To remove the default margins use the below code

```
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

---

## What is box sizing?

![alt text](images/box-sizing.jpg "Box Sizing Images")

---


## Including normalize.css

Normalize.css makes browsers render all elements more consistently and in line with modern standards. Include this file before adding any css file

```
<link rel="stylesheet" type="text/css" href="normalize.css">
```

---

## Fluid Grid

We will be using fluid grid to develop our website. The fluid grid that we would be using is 

http://www.responsivegridsystem.com/

Inlcude the above grid.css after normalize.css

```
<link rel="stylesheet" type="text/css" href="grid.css">
```

Note: The downloaded file will have seperate file as 2cols.css, 3cols.css. Combine everything into one and rename it as grid.css and include it here

Using this grid all our content will be in columns. You can have from 1 column in a row to 12 columns in a row.

When using this grid we will be using only one value in px and rest we would be using in percentages

---

## Including grid.css

[grid.css](https://github.com/jeriljose/Reference/blob/gh-pages/grid.css)

---

## Default Styles

/* ---------------------------HTML SECTION --------------------------------- */

```
<head>
  <title></title>
  <link rel="stylesheet" type="text/css" href="https://necolas.github.io/normalize.css/8.0.0/normalize.css">
  <link rel="stylesheet" type="text/css" href="https://raw.githubusercontent.com/jeriljose/Reference/gh-pages/grid.css">  
  <link href="https://unpkg.com/ionicons@4.2.2/dist/css/ionicons.min.css" rel="stylesheet">  
  <link rel="stylesheet" type="text/css" href="style.css">
  <link href='http://fonts.googleapis.com/css?family=Lato:100,300,400,300italic' rel='stylesheet' type='text/css'>
</head>

```

/* ----------------------------CSS SECTION ----------------------------------- */

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
 
 .row {
  max-width: 1140px;
  margin: 0 auto;
}
```
