# Sending a POST request with parameters

```python
payload = {'name': 'Jeril', 'job': 'Programmer'}
# The word is json is madatory. json converts the above dictionary payload into json object
r = requests.post('https://reqres.in/api/users', json=payload)
```