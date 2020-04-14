//this is an example of post using axios.
// We get the values in the form. The values entered in the form are stored in the state variable
// axios.post is then called along with the values in the state object
// The newly available values are then captured by the api

```
import React, { Component } from 'react'
import axios from 'axios'

export default class ExampleAxiosPost extends Component {

    state = {
        name: '',
        email: ''
    };

    /* this function tracks what is entered in the text fields and 
       keeps them insync in the state object */
    handleChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    }

    handleSubmit = e => {
        e.preventDefault();
        /* to the axios post we are sending two arguments 
         - https://jsonplaceholder.typicode.com/users - URL of the api
         - this.state - values in the state or values entered in the form by the user
        */
        axios
            .post(`https://jsonplaceholder.typicode.com/users`, this.state)
            .then(res => {
                console.log(res);
                console.log(res.data);
            })
            .catch(err => {
                console.error(err)
            })
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label> Person Name:
                    <input
                        type="text"
                        name="name"
                        onChange={this.handleChange}
                    />
                </label>
                <label> Email:
                    <input
                        type="text"
                        name="email"
                        onChange={this.handleChange}
                    />
                </label>
                <button type="submit">Add</button>
            </form>
        )
    }
}

```

