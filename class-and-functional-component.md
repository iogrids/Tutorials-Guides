## Class component - React

//class component

```
import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
       <h1>Hi, I'm a React App</h1>
       <p>This is really working!</p>
      </div>
    );
  }
}

export default App;
```


## Functional component in React

```
// functional component

import React from 'react'

const person = () => {
  return <p>I'm a Person!</p>
}

export default person;

```

// To use the functional component in another js file

```
import Person from './component/Person.js'

<Person> </Person>

```





