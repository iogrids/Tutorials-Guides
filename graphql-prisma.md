# 1. Send data from the client to the server

```
const typeDefs = `
  type Query {
    greeting(name: String, position: String): String!
  }
`

const resolvers = {
  Query: {
      greeting(parent, args, ctx, info) {
      // args will contain all the values passed from the client
        if (args.name && args.position) {
            return `Hello, ${args.name}! You are my favourite ${args.position}.`
        } else{
            return 'Hello!'
        }
      }
   }
}

```

## Executing the above query in graphQL playground

```
greeting(name: "Andrew", position: "teacher")
```

---

# 2. Graphql - Send arrays from the server to the client

```
const typeDefs = `
  type Query {
    grades: [Int!]!
  }
`

const resolvers = {
  Query: {
      grades(parent, args, ctx, info) {
        return [10, 20, 30]]
      }
   }
}

```

---

# 3. Graphql - Send array of data from the client to the server

```
const typeDefs = `
  type Query {
    add(): Float!
  }
`

const resolvers = {
    Query: {
      add(parent, args, ctx, info) {
        if (args.numbers.length === 0){
            return 0
        }

        return args.numbers.reduce((total, currentValue) => {
            return total + currentValue
        })
      }
    }
}

# Executing the above query in graphQL playground

query {
    add(numbers: [1,5,10,2])
}

Result:

{
  "data": {
     "add": 18
  }
}

```

---

# 4. Working with array of objects

```
// array declaration

const = [{
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

//typedefs

const typeDefs = `
  type Query {
    users: [User!]!
  }

  type User {
    id: ID!
    name: String!
    email: String!
    age: Int
  }
`
// resolver function for the typedef

const resolvers = {
  Query: {
      users(parent, args, ctx, info) {
         return users
      }
   }
}

//querying results in Graphql Playground

query{
   users {
     id
     name
     email
     age
   }
}

```

# 5. Working with array filters (Filter value and show the results)

```
// array declaration

const = [{
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

//typedefs

const typeDefs = `
  type Query {
    users(query: String): [User!]!
  }

  type User {
    id: ID!
    name: String!
    email: String!
    age: Int
  }
`
// resolver function for the typedef

const resolvers = {
  Query: {
      users(parent, args, ctx, info) {
         if (args.query) {
           //if there is no filter, then return all the users
           return users
         }
         return users.filter((user) => {
           //convert everything to lowercase
           //The includes() method determines whether a string contains the characters of a specified string.
           return user.name.toLowerCase().includes(args.query.toLowerCase())
         })
      }
   }
}

// querying results in Graphql Playground
// the below lists all the users who have the letter 'a' in them

query{
   users(query: "A") {
     id
     name
     email
     age
   }
}

```
