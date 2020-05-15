# Receiving images by the client/browser using GET request using the REQUEST library

```python
r = requests.get('https://httpbin.org/image/jpeg')
# print(r.headers)

# To know whether it is a jpeg image try printing the headers(as shown above) and check the image type
# wb stands for write in binary mode
# r.iter_content - iterates over the image file in a size of 500 pieces of chunks rather than writing the whole image
# If you write the whole image and if the image size is big the writing process may fail
# It writes only a single image
# If the image size is 1000 chunks the below code will write it twice 500 chunks + 500 chunks to write the complete file
with open('image.jpeg', 'wb') as fd:
   for chunk in r.iter_content(chunk_size=500):
      fd.write(chunk)
      
```