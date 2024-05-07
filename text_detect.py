import cv2 as cv
import easyocr
import matplotlib.pyplot as plt

# reading the image
img_path = './data/test3.png'
img = cv.imread(img_path)

# intantiate easyOCR reader
reader = easyocr.Reader(['en'],gpu=False)

# detect text on image
text = reader.readtext(img)

for t in text:
    print(t)
    bbox,text,score=t
    cv.rectangle(img,bbox[0],bbox[2],(255,0,0),thickness=1)
    cv.putText(img,text,bbox[0],cv.FONT_ITALIC,0.75,(0,0,255),2)

plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))
plt.show()
