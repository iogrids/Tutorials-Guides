# Sending images to the server as POST data using REQUEST library

```python

"""
  If you send images to server, the server automatically recieves a header type called multipart
  as shown below

  Content-Type: multipart/form-data;
  
  image/jpeg - informs the server that we are sending a jpeg image mime type. If you want to send other kind of files mention the appropriate mime type

"""

# rb - refers to open the file cat.jpg in read mode and binary mode

files = {'file' : ('cat.jpg', open('cat.jpg', 'rb'), 'image/jpeg')}
# The word is data is madatory which sends data to a form
r = requests.post('https://reqres.in/wpo4xjwp', files=files)

```