# Sending a POST request using request library

```python
r = request.get('https://requestbin.com/wp04xjwp?key1=value1&key2=value2')
```

The above can also be represented as

```python
payload = {'first': 'one', 'second': 'two'}

r = request.get('https://requestb.in/wp04xjwp', params=payload)

```