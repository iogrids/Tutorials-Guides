## add this code in script.js file
```javascript
function init(){

 function fruits(){
         function apple(){
            return '<div id="main">'+
                  '   <div>'+
                  '   This is apple'+
                  '   </div>'+
                  '</div>';            
         }
         
         function mango(){
            return '<div id="main">'+
                  '   <div>'+
                  '   This is mango'+
                  '   </div>'+
                  '</div>';            
         }

         return{
            apple: apple,
            mango: mango
         }
  }

   function print(var1){
      //fruits.mango is passed to var1. So var1 is a function and to call the function use var1()
      document.write(var1())
   }
   
   return {
      fruits:fruits,
      print: print
   }
}

```

## call the below code in index.html file

```javascript
 <script>

              var object = init();
              var fruits = object.fruits();

              object.print(fruits.mango);

 </script> 
```
