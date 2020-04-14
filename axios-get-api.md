//this is an example of how to get names from a api
// Here we read the values using axios and save them in the state object
// All values are then displayed from the state object

```
import React, { Component } from 'react'
import axios from 'axios'

export default class ExampleAxiosGet extends Component {

    state = {
        persons: []
    };
    // this is one of the lifecycle method of class in react
    componentDidMount() {
        axios
            .get(`https://jsonplaceholder.typicode.com/users`, {
                //we are limiting the number of items to 10
                params: { _limit: 10 }
            })
            .then(res => {
                const persons = res.data;
                this.setState({ persons });
            })
            .catch(err => console.error(err))
    }

    render() {
        return (
            <ul>
                {this.state.persons.map(person => (
                    <li key={person.id}>{person.name}</li>
                ))}
            </ul>
        )
    }
}

```