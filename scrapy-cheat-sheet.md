```html
<!DOCTYPE html>
    <html lang="en">
        <head>
            <title>XPath and CSS Selectors</title>
        </head>
        <body>
            <h1>XPath Selectors simplified</h1>

            <div class="intro">
                <p>
                    I'm paragraph within a div with a class set to intro
                    <span id="location">I'm a span with ID set to location and i'm within a paragraph</span>
                </p>
                <p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p>
            </div>

            <div class="outro">
                <p id="unique">I'm in a div with a class attribute set to outro</p>
            </div>

            <p>Hi i'm placed immediately after a div</p>
            
            <span class='intro'>Div with a class attribute set to intro</span>

            <ul id="items">
                <li data-identifier="7">Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
                <li>Item 4</li>
            </ul>

            <a href="https://www.google.com">Google</a>
            <a href="http://www.google.fr">Google France</a>
        </body>
    </html>

```

---

# How to use xpath to select the appropriate element from the above HTML file    

```
1. //div[@class='intro']/p
```
Result:

```html
<p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location and i'm within a paragraph</span> </p>
<p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p>
```

---

```
2. //div[@class='intro' or @class='outro']/p
```
Result:

```html
<p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location and i'm within a paragraph</span> </p>
<p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p>
<p id="unique">I'm in a div with a class attribute set to outro</p>
```

---

```
3. //div[@class='intro' or @class='outro']/p/text()
```

Result:

```html
I'm paragraph within a div with a class set to intro
I'm a paragraph with ID set to outside and i'm within a div with a class set to intro
I'm in a div with a class attribute set to outro
```

---

```
4. //a/@href
```
Result:

```html
https://www.google.com
http://www.google.fr
```

---

```
5. //a[starts-with(@href, 'https')]
```

Result:

```html
<a href="https://www.google.com">Google</a>
```

---

```
6. //a[ends-with(@href, 'fr')]
```

```html
<a href="http://www.google.fr">Google France</a>
```

---


```
7. //a[contains(@href, 'google')]
```

Result: 

```html
<a href="https://www.google.com">Google</a>
<a href="http://www.google.fr">Google France</a>
```

---

```
8. //a[contains(text(), 'France')]
```
Result:

```html
<a href="http://www.google.fr">Google France</a>
```

---

```
9. //ul[@id='items']/li
```
Result:

```html
<li data-identifier="7">Item 1</li>
<li>Item 2</li>
<li>Item 3</li>
<li>Item 4</li>
```

---

```
10. //ul[@id='items']/li[1]
```

Result:

```html
<li data-identifier="7">Item 1</li>
```

---

```
11. //ul[@id='items']/li[1 or 4]
```
Result:

```html
<li data-identifier="7">Item 1</li>
<li>Item 2</li>
<li>Item 3</li>
<li>Item 4</li>
```

---

```
12. //ul[@id='items']/li[position() =  1 or position() = 4]
```
Result:

```html
<li data-identifier="7">Item 1</li>
<li>Item 4</li>
```

---

```
13. //ul[@id='items']/li[position() =  1 or position() = last()]
```

Result:

```html
<li data-identifier="7">Item 1</li>
<li>Item 4</li>
```

---

# Navigating using XPath - Going up

```
14. //ul[@id='items']/li[position() > 1]
```
Result:

```html
<li>Item 2</li>
<li>Item 3</li>
<li>Item 4</li>
```

---

```
14. //p[@id='unique']/parent::div
```

```html
<div class="outro"> <p id="unique">I'm in a div with a class attribute set to outro</p> </div>
```

---

```
15. //p[@id='unique']/parent::node()
```

```html

<div class="outro"> <p id="unique">I'm in a div with a class attribute set to outro</p> </div>

```

---

```
16. //p[@id='unique']/ancestor::node()
```

```html

<html lang="en"> <head> <title>XPath and CSS Selectors</title> </head> <body> <h1>XPath Selectors simplified</h1> <div class="intro"> <p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location and i'm within a paragraph</span> </p> <p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p> </div> <div class="outro"> <p id="unique">I'm in a div with a class attribute set to outro</p> </div> <p>Hi i'm placed immediately after a div</p> <span class="intro">Div with a class attribute set to intro</span> <ul id="items"> <li data-identifier="7">Item 1</li> <li>Item 2</li> <li>Item 3</li> <li>Item 4</li> </ul> <a href="https://www.google.com">Google</a> <a href="http://www.google.fr">Google France</a> </body> </html>

<body> <h1>XPath Selectors simplified</h1> <div class="intro"> <p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location and i'm within a paragraph</span> </p> <p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p> </div> <div class="outro"> <p id="unique">I'm in a div with a class attribute set to outro</p> </div> <p>Hi i'm placed immediately after a div</p> <span class="intro">Div with a class attribute set to intro</span> <ul id="items"> <li data-identifier="7">Item 1</li> <li>Item 2</li> <li>Item 3</li> <li>Item 4</li> </ul> <a href="https://www.google.com">Google</a> <a href="http://www.google.fr">Google France</a> </body>
<div class="outro"> <p id="unique">I'm in a div with a class attribute set to outro</p> </div>

```

---

```
17. //p[@id='unique']/ancestor-or-self::node()
```

```html
<html lang="en"> <head> <title>XPath and CSS Selectors</title> </head> <body> <h1>XPath Selectors simplified</h1> <div class="intro"> <p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location and i'm within a paragraph</span> </p> <p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p> </div> <div class="outro"> <p id="unique">I'm in a div with a class attribute set to outro</p> </div> <p>Hi i'm placed immediately after a div</p> <span class="intro">Div with a class attribute set to intro</span> <ul id="items"> <li data-identifier="7">Item 1</li> <li>Item 2</li> <li>Item 3</li> <li>Item 4</li> </ul> <a href="https://www.google.com">Google</a> <a href="http://www.google.fr">Google France</a> </body> </html>

<body> <h1>XPath Selectors simplified</h1> <div class="intro"> <p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location and i'm within a paragraph</span> </p> <p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p> </div> <div class="outro"> <p id="unique">I'm in a div with a class attribute set to outro</p> </div> <p>Hi i'm placed immediately after a div</p> <span class="intro">Div with a class attribute set to intro</span> <ul id="items"> <li data-identifier="7">Item 1</li> <li>Item 2</li> <li>Item 3</li> <li>Item 4</li> </ul> <a href="https://www.google.com">Google</a> <a href="http://www.google.fr">Google France</a> </body>

<div class="outro"> <p id="unique">I'm in a div with a class attribute set to outro</p> </div>

<p id="unique">I'm in a div with a class attribute set to outro</p>
```

---

```
18. //p[@id='unique']/preceding::node()
```

```html

<head> <title>XPath and CSS Selectors</title> </head>

<title>XPath and CSS Selectors</title>
XPath and CSS Selectors

<h1>XPath Selectors simplified</h1>
XPath Selectors simplified

<div class="intro"> <p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location and i'm within a paragraph</span> </p> <p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p> </div>

<p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location and i'm within a paragraph</span> </p>
I'm paragraph within a div with a class set to intro

<span id="location">I'm a span with ID set to location and i'm within a paragraph</span>
I'm a span with ID set to location and i'm within a paragraph

<p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p>
I'm a paragraph with ID set to outside and i'm within a div with a class set to intro


```

---

```
19. //p[@id='unique']/preceding::h1
```

```html

<h1>XPath Selectors simplified</h1>

```

```
20. //p[@id='outside']/preceding-sibling::node()

```

```html
<p> I'm paragraph within a div with a class set to intro <span id="location">I'm a span with ID set to location and i'm within a paragraph</span> </p>

```

# Navigating using XPath - Going down



