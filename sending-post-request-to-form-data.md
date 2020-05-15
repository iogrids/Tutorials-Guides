# Sending POST request to a HTML FORM 

```python

""" 
If you have a form with fields email and password and if you want to send data to the form the 
below example could be used or in other words the below code can help you programatically login.

Someone can create a huge list of dictionary like payload with various fake email and password 
combinations and send a POST request to his registration form. This could flood his database with
tons of registrations. It is to avoid this people use captcha in their registration forms. 
"""

payload = {'email': 'jerilcj3@gmail.com', 'password': 'johnjose'}
# The word is data is madatory which sends data to a form
r = requests.post('https://reqres.in/api/users', data=payload)

```