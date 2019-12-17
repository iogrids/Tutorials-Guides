## Working with Images

When you put an image use the below css. auto is used to maintain the aspect ratio of the image

```
img{
   height: 150px;
   width: auto;
}
```

---
 
## Putting text over images

If you put text directly on an image it will only look good if the image is dark and text is white. 

There are few techniques for making the image and text look good.

1. Overlay the image with a color. The most easiest to use is a black overlay on the top of image and then write text on it. Apart from black you can also use various other color gradients.

2. The second option is to blur the image and the text is shown on the blurred image part on all screen resolutions

3. The third option is to use a technique called "Floor fade technique". Here the image subtly fades towards black at the bottom and white text written over it.

4. Simply putting text on a box like the image shown below. The box should be opaque so that you can still see the image beneath it. In the below case a white color with some transperancy is used. 

![alt text](images/images-box.png "image-box")

---
