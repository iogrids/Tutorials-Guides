# Forms using Cherrypy and REACT - uses axios, cherrypy, REACT, CORS, POST & GET - Example 2

To call the react files in App.js you can use the below code

```react
import CreateUser from './CreateUser'
import GetUser from './GetUser'

```

and then use

```react
 <CreateUser />
 <GetUser />
```

## Client code for POST request to an API

 - filename - CreateUser.js
 
```react 
// ** create-user.component.js ** //

import React, { Component } from 'react';
import axios from 'axios';

export default class CreateUser extends Component {

    constructor(props) {
        super(props)

        this.onChangeUserName = this.onChangeUserName.bind(this);
        this.onChangeUserAge = this.onChangeUserAge.bind(this);
        this.onChangeUserSex = this.onChangeUserSex.bind(this);
        this.onSubmit = this.onSubmit.bind(this);

        this.state = {
            name: '',
            age: '',
            sex: ''
        }
    }

    onChangeUserName(e) {
        this.setState({ name: e.target.value })
    }

    onChangeUserAge(e) {
        this.setState({ age: e.target.value })
    }

    onChangeUserSex(e) {
      this.setState({ sex: e.target.value })
  }

    onSubmit(e) {
        e.preventDefault()

        const userObject = {
            name: this.state.name,
            age: this.state.age,
            sex: this.state.sex
        };
     
        //cherrypy runs on PORT 8080 or the POST api is accessible on PORT 8080
        axios.post('http://localhost:8080', userObject)
            .then((res) => {
                console.log(res.data)
            }).catch((error) => {
                console.log(error)
            });

        this.setState({ name: '', age: '', sex: '' })
    }


    render() {
        return (
            <div className="wrapper">
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label>Add User Name</label>
                        <input type="text" value={this.state.name} onChange={this.onChangeUserName} className="form-control" />
                    </div>
                    <div className="form-group">
                        <label>Add User Age</label>
                        <input type="text" value={this.state.age} onChange={this.onChangeUserAge} className="form-control" />
                    </div>
                    <div className="form-group">
                        <label>Add User Sex</label>
                        <input type="text" value={this.state.sex} onChange={this.onChangeUserSex} className="form-control" />
                    </div>
                    <div className="form-group">
                        <input type="submit" value="Create User" className="btn btn-success btn-block" />
                    </div>
                </form>
            </div>
        )
    }
}

```

## Client code for GET request to an API

- filename - GetUser.js

```react  

import React from 'react';
import './CreateUser'
import axios from 'axios';

export default class GetUser extends React.Component {
  state = {
    persons: []
  }

  componentDidMount() {
    axios.get(`http://localhost:8080`)    
      .then(res => {
        let persons = [];
        /* axios res.data is an object. You will have to convert it to array 
           so that map() function can be used to iterate over the api values.
           The below for loop read the res.data object and pushes it to an array
           called persons. */

        for(var i in res.data){
            
            persons.push({name: i, value: res.data[i]})
        }
        this.setState({ persons: persons })
        
      })
  }

  render() {
    return (
      <ul>
      { this.state.persons.map(person => <li>{person.name} - {person.value}</li>)}
      </ul>
    )
  }
}

```

## Python Code to create an API

The below code runs on PORT 8080. The above API is accessed by REACT using a library called axios. When a GET request is sent by axios, cherrypy
automatically identifies which method to call and similiarly for POST. This automatic identification of which method to call based on the request sent by axios is done by cherrypy.dispatch.MethodDispatcher() which is an internal function in cherrypy

```python

import random
import string
import cherrypy
import cherrypy_cors

@cherrypy.expose
class StringGeneratorWebService(object):
    
    @cherrypy.tools.json_out()
    def GET(self):
        name = 'yohan' 
        age = '01'
        sex = 'male'

        return {'name': name,
                'age': age,
                'sex': sex
        }
                
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out() # If you do not provide this line JSON will not be returned
    def POST(self):
        input_json = cherrypy.request.json      
        print(input_json)
        return {'status': 'success', 'message': 'updated'}

    def PUT(self, another_string):
        pass

    def DELETE(self):
        pass

    def OPTIONS(self):
        cherrypy_cors.preflight(allowed_methods=['GET', 'POST'])

if __name__ == '__main__':
    cherrypy_cors.install()
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'cors.expose.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
```