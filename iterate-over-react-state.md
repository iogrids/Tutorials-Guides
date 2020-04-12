How to iterate over react state using javascript map function - Props, State Complete Example

Tutorial: https://www.youtube.com/watch?v=1OoS-s-pdXc&list=PL7sCSgsRZ-sm3BZx2Mq5MTaPy_JT5uJJU&index=1

```
this.state = {
            people: [{
                name: 'David Davidson',
                company: "Texmo Industries",
                Description: "Met at a Party"
            },
            {
                name: 'Mark Markson',
                company: "Planet Media",
                Description: "Met at a Party"
            },
            {
                name: 'John Paul',
                company: "Some Company Inc",
                Description: "Met at a Party"
            }
           
            ]
        };

```        

// Here we iterate and pass the array to another component which is available in PeopleCard.js

```
        let peopleCards = this.state.people.map(person => {
          return(
            <Col sm="4">
               <PeopleCard person = {person}/> 
            </Col>
          )
        })
```
        State can be accessed in every javascript file. So to access the above values in state 

        {this.props.person.name}
        {this.props.person.company}
        {this.props.person.description}

### Complete Example:

Filename: Layout.js 

```
import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import PeopleCard from './PeopleCard'

class Example extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            people: [{
                name: 'David Davidson',
                company: "Texmo Industries",
                Description: "Met at a Party"
            },
            {
                name: 'Mark Markson',
                company: "Planet Media",
                Description: "Met at a Party"
            },
            {
                name: 'John Paul',
                company: "Some Company Inc",
                Description: "Met at a Party"
            }
           
            ]
        };
    }

    render() {

        let peopleCards = this.state.people.map(person => {
          return(
            <Col sm="4">
               <PeopleCard person = {person}/> 
            </Col>
          )
        })
        return (
            <Container fluid>
                <Row>
                    {peopleCards}
                </Row>
            </Container>
        );
    }
}

export default Example;  
```

Filename: PeopleCard.js

```
import React from 'react';
import {
  Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button
} from 'reactstrap';

class Example extends React.Component {
    constructor(props) {
        super(props);       
    }

    render() {
        return (
            <div>
                <Card>
                    <CardImg top width="100%" src="https://reactstrap.github.io/assets/318x180.svg" alt="Card image cap" />
                    <CardBody>
                        <CardTitle>{this.props.person.name}</CardTitle>
                        <CardSubtitle>{this.props.person.company}</CardSubtitle>
                        <CardText>{this.props.person.description}</CardText>
                        <Button>Button</Button>
                    </CardBody>
                </Card>
            </div>
        );
    }
}

export default Example;
```

# Looping through a state

```
this.state = {
            people: [
                { name: 'Bob', count: 0 },
                { name: 'Tina', count: 0 },
                { name: 'Louise', count: 0 },
                { name: 'Linda', count: 0 },
                { name: 'Gene', count: 0 }
            ]
        }
```

// Accessing the above values in JSX as shown below

```
<div className="App">
  {
     //looping through the array and copying the values to another array called person.
     this.state.people.map((person) => (
        <li> {person.name} </li>))
     }
</div>
```


# Iterate over react state and if a condition is met change the state. Example shown below

```
import React, { Component } from 'react'

export default class Component1 extends Component {

    constructor() {
        super();
        this.state = {
            people: [
                { name: 'Bob', count: 0 },
                { name: 'Tina', count: 0 },
                { name: 'Louise', count: 0 },
                { name: 'Linda', count: 0 },
                { name: 'Gene', count: 0 }
            ]
        }
    }

 // the below function loops through the state array people and if a condition is met changes the exisiting value of the state to another value

    changeState = (e) => {
        e.preventDefault();
        let per = this.state.people.map((person) => {
            if (person.name === 'Tina') {
                person.name = 'Jeril'
            }
            return person;
        })
// copies the new array per to exisiting array people and replaces it completely.
        this.setState({ people: per })
    }

    render() {
        return (
            <div className="App">
                {
                    this.state.people.map((person) => (
                        <li> {person.name} </li>
                    ))

                }
//call the change state function
                <button onClick={this.changeState}> Change State </button>
            </div>
        )
    }
}

```