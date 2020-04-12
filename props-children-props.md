Using props and props children in Functional component - React

// functional component

```
import React from 'react'

const person = (props) => {
  return (
      <p>I'm {props.name} and I am {props.age} years old</p>
      <p>{props.children}</p>
  )
}

export default person;


// To use the functional component in another js file

import Person from './component/Person.js'

// Now {Max} and {28} are called props. {My Hobbies: Racing} is called children prop.
// Any content within <Person></Person> is called children prop
// You can pass these values to the react component 
<Person name="Max" age="28">My Hobbies: Racing </Person>
```