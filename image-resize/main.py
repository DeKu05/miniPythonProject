import cv2

#configurable Parameters
source = 'us.jpg'
destinantion = '143.jpg'
scale_percent = input("Enter the scale percentage you want: ")  # percent of original size

img = cv2.imread(source, cv2.IMREAD_UNCHANGED)
print('Original Dimensions : ', img.shape)

#Calculate the scale percentage of the image
width = int(img.shape[1] * int(scale_percent) / 100)
height = int(img.shape[0] * int(scale_percent)/ 100)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim,)
print('Resized Dimensions : ', resized.shape)
cv2.imshow("Resized image", resized)

cv2.imwrite(destinantion, resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
