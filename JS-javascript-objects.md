## Working with JSON

```Javasctipt

var info = {
	"full_name" : "Ray Villalobos",
	"title" : "Staff Author",
	"links" : [
			{ "blog"     : "http://iviewsource.com" },
			{ "facebook" : "http://facebook.com/iviewsource" },
			{ "youtube"  : "http://www.youtube.com/planetoftheweb" },
			{ "podcast"  : "http://feeds.feedburner.com/authoredcontent" },
			{ "twitter"  : "http://twitter.com/planetoftheweb" }
		]
	};
  
```

Try this in the Javascript console

```
> info
```

returns object

```
> info.full_name
```

returns 

Ray Villalobos

```
info.links[1].facebook
```

returns 

http://facebook.com/iviewsource

---

## To Modify variables

info.full_name = "Eric"

---

## To delete an element

```
delete(info.title);
```

returns 

true

