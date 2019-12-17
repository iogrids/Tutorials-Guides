## Mixing Javascript & HTML

The below code prints social media icons (images)

```Javascript

var socialMedia = {
    facebook : 'http://facebook.com',
    twitter: 'http://twitter.com',
    flickr: 'http://flickr.com',
    youtube: 'http://youtube.com'
};

var social = function() {
  var output = '<ul>',
  //querySelectorAll allows you to select en element in the dom with a certain class
  myList = document.querySelectorAll('.socialmediaicons');

 //arguments will contain all values of variable socialMedia. arguments is an inbuilt Javascript variable 
  for( var key in arguments[0]) {
     output += '<li><a href="' + socialMedia[key] + '">' +
     '<img src="images/' + key + '.png" alt="icon for ' + key + '">' + 
      '</a></li>';
  }

  output += '</ul>';

  for (var i = myList.length -1; i >=0; i--) {
    myList[i].innerHTML = output;
  }
}(socialMedia);

```

HTML

```
<nav class="socialmediaicons"></nav>

```

## You can mix Javascript and HTML also using Tagged templates which is a feature of ES6. The above functionality is written below using tagged templates

```
let facebook = 'http://facebook.com'
let twitter = 'http://twitter.com'
let flickr = 'http://flickr.com'
let youtube = 'http://youtube.com'
let lines = [
   facebook,
   twitter,
   flickr,
   youtube
];

function buildHTML(tags, lines){
  const newHTML = lines.map(function line(){
    return `${tags[0]}${line}${tags[1]}`
  })
  return newHTML;
}

const result = buildHTML`<li>${lines}</li>`
//console.log(result)
document.querySelector('quotes').innerHTML = result;


```
