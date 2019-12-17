## Javascript and JSON

JSON is created using key value pairs

eg:

```Javascript

{
  "name"     : "Jeril",
  "position" : "staff Author",
  "cources"  : [
     "Javascript and AJAX",
     "Building Facebook Applications",
     "jQuery Mobile Web Apps"
   ]
}


You can pass the above JSON object and pass it to a Javascript object using the function

var info = JSON.Parse(data);
//once you convert the above JSON to a javascript object then you can use the (DOT) notation to access the value (eg: info.name)
var name = info.name; //to get the name or
var name = info[name]
var course = info.courses[0] //prints -> Javascript and AJAX

```

---

## JSON Object vs Javascript Object

JSON object is always put in double quotes

```Javascript

{"fullname" : "Jeril"}  or
{"full name" : "Jeril"} -> Json object can have space (full name, which is not possible in Javascript object)


```

A javascript object will look like this. Notice full_name does not have double quotes

```Javascript
  
  var info ={ full_name: "Jeril"}
 
```

A javascript object can also have a function which is not possible in JSON object like shown below

var info = {
	full_name: "Jeril",
	getName : function() {
	  alert(this.full_name);
	}
};

---

## JSON validator

You can use jsoneditoronline.org to validate your JSON file and check for errors.
