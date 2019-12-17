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
# 6. Relationship between two types

     1. Here there are data types User and Post
     2. User type and Post type are related as follows
           1. Every Post is written by some user
           2. A user can have a collection of posts

To implement the above scenerio

```
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

const posts = [{
  id: '10',
  title: 'Graphql 101',
  body: 'This is how to use Graphql',
  published: true,
  author: '1',    // 1 is the id of user
}, {
  id: '11',
  title: 'Graphql 201',
  body: 'This is an advanced Graphql post',
  published: true,
  author: '1'     // 1 is the id of the user or written by the user whose id is 2
}, {
  id: '12',
  title: 'Programming basics',
  body: 'This is a programming post',
  published: false,
  author: '2'   // 2 is the id of the user
}]

const typeDefs = `
   type Query {
      // code here
   }

   type User {
      id: ID!
      name: String!
      email: String!
      age: Int
      posts: [Post!]!
   }

   type Post {
      id: ID!
      title: String!
      body: String!
      published: Boolean
      author: User!  
   }
`
```

---

# 6a. Querying based on relation (Single directional relation)

List all posts and also the author of each individual post. To implement this

## Query:

```
query{
  posts {
    id
    title
    body
    published
    author {
      name
    }
  }
}
```
## Result:

```
{
  "data": [
    {
      "id": "10",
      "title: "Graphql 101",
      "body": "This is how to use Graphql",
      "published": true,
      "author": {
        "name": "Jeril"
       }  
    }, {
      "id": "11",
      "title: "Graphql 201",
      "body": "This is an advanced Graphql post",
      "published": false,
      "author": {
        "name": "Jeril"
       }  
    },
    {
      "id": "12",
      "title": 'Programming basics',
      "body": 'This is a programming post',
      "published": false, 
      "author": {
        "name": "Mike"
       }  
    }]
}

```

// typedefs code

```
const typedefs = `
  type Query {
    posts(query: String): [Post!]!
  }

  type Post {
    id: ID!
    title: String!
    body: String!
    published: Boolean!
    author: User!
  }

  type User {
    id: ID!
    name: String!
    email: String!
    age: Int
  }
`
```
// resolvers

```
const resolvers = {
  Query: {
    posts(parent, args, ctx, info) {
      if (!args.query) {
        return posts
      }
       return posts.filter(post) => {
         const isTitleMatch = post.title.toLowerCase().includes(args.query.toLowerCase())
         const isBodyWatch = post.body.toLowerCase().includes(args.query.toLowerCase())
         return isTitleMatch || isBodyWatch
       }
    }
  }, 
  // When one of the of fields is not a scalar type we will have to set up a custom resolver function to teach graphql on how to get the correct data. Here for Post typedef author: User! is not a scalar type and hence the below code

  Post: {
    // if there are 3 posts, parent iterates over the first array and parent acts as the     // object of the first post
    // So you can access like this

    // parent.published , parent.author, parent.title etc   


    author(parent, args, ctx, info) {
      return users.find((user) => {
         return user.id === parent.author
      })
    }
  }
}

```

