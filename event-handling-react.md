Event Handling in React class component and changing the values of the state during run time

// Always try to use functional based component since they are easy to manage than class based component
// Props - values which are passed to the component from outside i.e from another component
// States - values which are passed within the component

// Class component

```

import React, { Component } from 'react';
import './App.css';

class App extends Component {

//If the state changes it will re-render the DOM

  state = {  
    persons: [
      { name: 'Max', age: 28 },
      { name: 'Manu', age:29 },
      { name: Stephanie, age: 26 }
    ],
    married: 'No'
  }

  switchNameHandler = () => {
    this.setState( {
      persons: [
        { name: 'Maximilian', age: 28 },
        { name: 'Manu', age:29 },
        { name: Stephanie, age: 27 }
      ]
    } )

  }

  render() {
    return (
      <div className="App">
      <button onClick={this.switchNameHandler}>Switch Name</button>
       <div> 
          Name: {this.state.persons[0].name} 
          Age: {this.state.persons[0].age}
       </div>

       <div> 
          Name: {this.state.persons[1].name} 
          Age: {this.state.persons[1].age}
       </div>

       <div> 
          Name: {this.state.persons[2].name} 
          Age: {this.state.persons[2].age}
       </div>

      </div>
    );
  }
}

export default App;

```
