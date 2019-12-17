## How to use pseudo class

Suppose there is a ```<h2>``` tag

  ```<h2>How are you</h2>``` If you want to put a small line below this text.

  you can do it like shown below

```
h2:after{
   display:block;
   height: 2px;
   background-color: #e67322;
   content: " "; // this is mandatory. It refers to what content should be put
   width: 100px;
   margin: 0 auto; //to center the line
   margin-top: 30px; //margin between the h2 tag and the small line
}
```
