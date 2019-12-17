How to use foreach, callback function

```Javascript
var articles = [{
    "id": 1,
    "first name": "vacuum cleaners",
    "weight": 9.9,
    "price": 89.9,
    "brand_id": 2
}, {
    "id": 2,
    "first name": "washing machine",
    "weight": 540,
    "price": 230,
    "brand_id": 1
}, {
    "id": 3,
    "first name": "hair dryer",
    "weight": 1.2,
    "price": 24.99,
    "brand_id": 2
}, {
    "id": 4,
    "first name": "super fast laptop",
    "weight": 400,
    "price": 899.9,
    "brand_id": 3
}];

articles.forEach(function(john) {
  console.log(john["first name"])  //if the key has space then print the value like this
  console.log(john.price) // if it does not have space then you can use the dot operator
});

```

### Output

```
vacuum cleaners
89.9
washing machine
230
hair dryer
24.99
super fast laptop
899.9
```
