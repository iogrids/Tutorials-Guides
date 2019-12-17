#  Send data from the client to the server

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

# Graphql - Send arrays from the server to the client

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

# Graphql - Send array of data from the client to the server

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