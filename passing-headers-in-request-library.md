# Passing headers to GET request using Request Library

Values passed in headers would be api-key, user-agent etc. 

```python
headers = {'my-token': '30703bkk3h3093uu3yg39828y2kh21212', 'user-agent': 'fakeagent'}
r = requests.get('https://requestb.in/wpo4xjwp', headers=headers)
```