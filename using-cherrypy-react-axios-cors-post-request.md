# Cherrypy, REACT, CORS, AXIOS example

In this example we will create a FORM in REACT and when user submits the FORM, the details are sent to the cherrypy server.

From REACT to call the cherrpy server we will use axios in react

We will also understand how CORS works in cherrypy. CORS allows us to access Cherrypy in REACT

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

Now lets create the PYTHON API using cherrypy

```python
import cherrypy
import cherrypy_cors

class HelloWorld(object):
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):
        
        if cherrypy.request.method == 'OPTIONS':
            cherrypy_cors.preflight(allowed_methods=['GET', 'POST'])

        if cherrypy.request.method == 'POST':
            name = cherrypy.request.json.get('name')
            age = cherrypy.request.json.get('age')
            sex = cherrypy.request.json.get('sex')
            print(name)
            print(age)
            print(sex)
            return {'name': name, 
                    'age': age,
                    'sex': sex
                   }

if __name__ == '__main__':
    cherrypy_cors.install()
    config = { 
        '/': {
            'cors.expose.on': True,
         },
    }
    cherrypy.quickstart(HelloWorld(),'/', config)


```