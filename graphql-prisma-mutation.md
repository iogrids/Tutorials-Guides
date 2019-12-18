# Mutation

// query

```
mutation {
    createUser(name: "Andrew", email: "test@gmail.com") {
        id
        name
        email
        age
    }
}

```

```
// array declaration

const users = [{
  id: '1',
  name: 'Jeril',
  email: jeril@gmail.com,
  age: 36
}, {
  id: '1',
  name: 'Sarah',
  email: sarah@gmail.com,
  age: 30
}, {
  id: '3',
  name: 'Mike',
  email: mike@gmail.com,
  age: 31
}]

```



// typedefs

```
const typeDefs = `
  type Query {
    //queries here
  }

  type Mutation {
    createUser(name: String!, email: String!, age: Int): User!
  }

  type User {
      id: ID!
      name: String!
      email: String!
      age: Int      
  }
`
```
// Resolvers

```
const resolvers = {
    Query: {

    },
    Mutation: {
        createUser(parent,args, ctx, info) {
           const user = {
             id: 'sdsdsdx10282'
             name: args.name,
             email: args.email,
             age: args.age
           }
           users.push(user)
           return user
        }
    }
}

```
