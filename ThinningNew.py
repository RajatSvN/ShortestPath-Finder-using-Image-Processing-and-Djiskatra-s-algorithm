import cv2
import numpy as np

#Reading the Grid Image
im = cv2.imread("New.png",0).astype(np.uint8)
# Making skel and temp numpy zeros array to be used in calculations
skel = np.zeros((im.shape[0],im.shape[1]),dtype = np.uint8)
temp = np.zeros((im.shape[0],im.shape[1]),dtype = np.uint8)
eroded = np.zeros((im.shape[0],im.shape[1]),dtype = np.uint8)
# Different Structuring Elements for Morphological Transformations
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# (-1,-1) used for centering while morphing
element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7),(-1,-1))
element3 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7),(-1,-1))
im=cv2.erode(im,element)

done = False 

# skeletonization process through erosion , dilation etc.
eroded = cv2.erode(im,element,iterations=1)
temp=cv2.dilate(eroded,element,iterations=1)
temp=cv2.subtract(im,temp)
skel=cv2.bitwise_or(skel,temp)
im=eroded.copy()
if cv2.countNonZero(im) == 0:
    done = True 
        

while done==False:
    eroded = cv2.erode(im,element,iterations=1)
    temp=cv2.dilate(eroded,element,iterations=1)
    temp=cv2.subtract(im,temp)
    skel=cv2.bitwise_or(skel,temp)
    im=eroded.copy()
    
    if cv2.countNonZero(im)==0:
        done = True 
    
skel=cv2.dilate(skel,element2)
skel=cv2.erode(skel,element3)
cv2.imshow("Skeleton",skel)



# Thresholding , removing non black and white noises
for i in range(1,im.shape[0] - 1):
                for j in range(1,im.shape[1] - 1):
                        if im[i,j]<200 :
                                im[i,j]=0
                        else :
                                im[i,j]=255
cv2.imshow("thr",im)


# Thinning method
def thinningIteration(im,iter):
        
        marker=im-im
        print(marker.shape[0],marker.shape[1],marker[10][10])
        
        for i in range(1,im.shape[0] - 1):
                for j in range(1,im.shape[1] - 1):
                    # Checking neighbours for a given pixel
                        p2 = im[i-1,j]
                        p3 = im[i-1,j+1]
                        p4 = im[i,j+1]
                        p5 = im[i+1,j+1]
                        p6 = im[i+1,j]
                        p7 = im[i+1,j-1]
                        p8 = im[i,j-1]
                        p9 = im[i-1,j-1]
                        A = (p2 == 0 and p3 == 1)+(p3 == 0 and p4 == 1)+(p6 == 0 and p7 == 1)+(p7 == 0 and p8 == 1)+(p8 == 0 and p9 == 1)+(p9 == 0 and p2 == 1)+(p4 == 0 and p5 == 1)+(p5 == 0 and p6 == 1)
                        B = p2+p3+p4+p5+p6+p7+p8+p9
                        if iter==0:
                                m1=(p2*p4*p6)
                                m2=(p4*p6*p8)
                        else:
                                m1=(p2*p4*p8)
                                m2=(p2*p6*p8)
                        
                        if A == 1 and (B >= 2 and B <= 6) and m1 == 0 and m2 == 0:
                                marker[i,j] = 1
        cv2.imshow("marker"+str(iter),marker)
        im = cv2.bitwise_and(im,cv2.bitwise_not(marker))

# Thinning main method , skeletonized image is sent here
def thinning(im,ct):
    # making pixel values 0 or 1
        im = im / 255
        prev = np.zeros((im.shape[0],im.shape[1]),dtype = np.uint8)
        

        thinningIteration(im,0)
        thinningIteration(im,1)
        diff=abs(im-prev)
        prev=im.copy()
        
        while cv2.countNonZero(diff)>0 :
                thinningIteration(im,0)
                thinningIteration(im,1)
                diff=abs(im-prev)
                prev=im.copy()
        cv2.imshow("diff"+str(ct),diff)
        ct+=1
        im = im * 255
        return im

resultim = thinning(skel,0)
# Showing the processed image
cv2.imshow("Result",resultim)
cv2.imwrite("NewThinned.png",resultim)
cv2.waitKey(0)
cv2.destroyAllWindows()	








			
			


