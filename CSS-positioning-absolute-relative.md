## Postion: absolute and position: relative

![alt text](images/position.png "floating a DIV")

``` 	     
.red{
	background-color: red;
	position: relative; //put relative for the parent DIV
}
``` 

``` 
.blue{
    background-color: blue;
    position: absolute; //put absolute for the child DIV
    top:0;
    right:0;
}
``` 
 
``` 
<div class ="red">

    This is red    
    <div class = "blue" > This is blue</div>   
 </div>

```
