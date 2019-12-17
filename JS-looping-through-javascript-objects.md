## Looping through Javascript Objects

Lets find how we can traverse through Javascript JSON objects

```Javascript

<body>
<h2>Links</h2>
<ul id="links">
</ul>

<script>

var info = {
"full_name" : "Ray Villalobos",
"title" : "Staff Author",
"links" : {
    		"blog"     : "http://iviewsource.com",
    		"facebook" : "http://facebook.com/iviewsource",
    		"youtube"  : "http://www.youtube.com/planetoftheweb",
    		"podcast"  : "http://feeds.feedburner.com/authoredcontent",
    		"twitter"  : "http://twitter.com/planetoftheweb" 
	}
};

//this will hold the things that you want to output
var output = "";

for ( key in info.links ) {
//not sure what is the purpose of info.links.hasOwnProperty(key)
	if (info.links.hasOwnProperty(key)) {
		output += '<li>' +
		'<a href = "' + info.links[key] +
		'">' + key + '</a>' +
		'</li>';
	} //if the links has the key property
} // for...go through each link

var update = document.getElementById('links');
//update with the parsed values
update.innerHTML = output;


</script>
</body>

```

## Result: The above code prints

* blog
* facebook
* youtube
* podcast
* twitter
