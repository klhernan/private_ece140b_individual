import cv2
import numpy as np
from PIL import Image
import pytesseract

def get_contours(img, dilated, tree=False):

    # Get contours
    if not tree:
        contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    print(len(contours))
    imgCpy = img
    cv2.drawContours(imgCpy, contours, -1, (0, 255), 3)
    cv2.imwrite("imgCon.png", imgCpy)
    # Find the largest 15 contours
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:15]

    # Find best polygon and get location
    location = None

    # Finds rectangular contour
    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02*peri, True) 
        if len(approx) == 4:
            location = approx
            break

    # Handle cases when no quadrilaterals are found        
    if type(location) != type(None):
        print("Corners of the contour are: ",location)
    else:
        print("No quadrilaterals found")

    # Sudoku Specific: Transform a skewed quadrilateral
    def get_perspective(img, location, height = 900, width = 900):
        pts1 = np.float32([location[0], location[3], location[1], location[2]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        # Apply Perspective Transform Algorithm
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(img, matrix, (width, height))
        return result

    if type(location) != type(None):
        result = get_perspective(img, location)
        result = cv2.rotate(result, cv2.ROTATE_90_CLOCKWISE)
        # cv2.imwrite("Result.png", result)

    else:    
        no_plate_found = np.array = [[-1,-1], [-1,-1], [-1, -1], [-1,-1]]
        print("No plate found!\n")
        return no_plate_found



def detect_plate(img):

    """
    Input : 
        Img ( img_arr)
        
    Output : 
        roi( crop_img, np_arr)
        coord(roi_center, np_arr)

    """

    # dilated = preprocess_img(img)
    dilated = preprocess_color_img(img, lower_bound = (120, 120, 0), upper_bound = (255,255,200))
    result = get_contours(img, dilated, tree=False)



if __name__ == "__main__":

    images = ["./public/images/Arizona_47.jpg" ,"./public/images/Contrast.jpg" ,"./public/images/Delaware_Plate.png"]
    
    # for im in images()
    img = cv2.imread("./public/images/Arizona_47.jpg")
    imggray = cv2.imread("./public/images/Arizona_47.jpg",0)
    gray_image = cv2.bilateralFilter(imggray, 11, 17, 17)
    cv2.imwrite("some solution idk.png", gray_image) 
    edged = cv2.Canny(gray_image, 30, 200) 
    cv2.imwrite("some other solution.png",edged)
    # normimg = cv2.normalize(imggray, imggray, 0, 210, cv2.NORM_MINMAX)
    # someimage = preprocess_color_img(img)
    # blur = cv2.GaussianBlur(normimg.copy(), (9, 9), 0)
    # thresh = cv2.threshold(blur, 140, 255, cv2.THRESH_TOZERO_INV)[1] # [1]
    (h,w) = imggray.shape[:2]
    (cX,cY) = (w//2, h//2)
    rotaIMG = cv2.getRotationMatrix2D((cX,cY),5,1.0)
    rotated = cv2.warpAffine(imggray, rotaIMG, (w,h))
    cv2.imwrite("rotatedimage.png", rotated)



    img_hsv = cv2.imread("./public/images/Arizona_47.jpg",cv2.COLOR_HSV2BGR)
    img = img_hsv.copy()
    bilateral_blur = cv2.medianBlur(img,3)
    cv2.imwrite("bilateralimag.png",cv2.cvtColor(bilateral_blur,cv2.COLOR_BGR2RGB))



    kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]], np.uint8)
    # blur = cv2.GaussianBlur(imggray.copy(), (9, 9), 0)
    kernel5 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

    # threshimg = cv2.adaptiveThreshold(bilateral_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,2)
    # cv2.imwrite("threshimg.png", threshimg)
    # opening = cv2.morphologyEx(threshimg, cv2.MORPH_CLOSE, kernel)    
    # cv2.imwrite("opening gray gaussian.png", opening)
    # dilated = cv2.dilate(threshimg, kernel)
    # cv2.imwrite("dilated gray gaussian.png", dilated)
    # plate = get_contours(imggray, dilated)
  
    blurColor = cv2.GaussianBlur(img.copy(), (15, 15), 0)
    cv2.imwrite("blurred color image.png", blurColor)
    colorToGray = cv2.cvtColor(bilateral_blur, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayed color image.png", colorToGray)
    colorToGray = 255 - colorToGray



    threshimg = cv2.adaptiveThreshold(colorToGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,2)
    cv2.imwrite("threshimg.png", threshimg)



    scale = 1
    delta = 0
    ddepth = cv2.CV_16S
    sobel_xright = cv2.Sobel(colorToGray, ddepth, 1, 0, ksize=3, scale=1, delta=delta, borderType=cv2.BORDER_DEFAULT)
    cv2.imwrite("sobel_xright color image.png", sobel_xright)

    sobel_xleft = cv2.Sobel(colorToGray, ddepth, 1, 0, ksize=3, scale=-1, delta=delta, borderType=cv2.BORDER_DEFAULT)
    cv2.imwrite("sobel_xleft color image.png", sobel_xleft)

    sobel_ytop = cv2.Sobel(colorToGray, ddepth, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    cv2.imwrite("sobel_ytop color image.png", sobel_ytop)
    
    sobel_ybot = cv2.Sobel(colorToGray, ddepth, 0, 1, ksize=3, scale=-1, delta=0, borderType=cv2.BORDER_DEFAULT)
    cv2.imwrite("sobel_ybot color image.png", sobel_ybot)
    
    
    abs_grad_xright = cv2.convertScaleAbs(sobel_xright)
    abs_grad_xleft = cv2.convertScaleAbs(sobel_xleft)
    abs_grad_ytop = cv2.convertScaleAbs(sobel_ytop)
    abs_grad_ybot = cv2.convertScaleAbs(sobel_ybot)
    
    grad1 = cv2.addWeighted(abs_grad_xright, 1, abs_grad_xleft, 1, 0)
    cv2.imwrite("grad1 color image.png", grad1)
    
    grad2 = cv2.addWeighted(abs_grad_ytop, 1, abs_grad_ybot, 1, 0)
    cv2.imwrite("grad2 color image.png", grad2)
    
    gradtotal = cv2.addWeighted(grad2, 1, grad1, 1, 0)
    cv2.imwrite("gradtotal color image.png", gradtotal)
    

    inv = 255 - gradtotal
    cv2.imwrite("inv color image.png", inv)
    tophat = cv2.morphologyEx(inv, cv2.MORPH_OPEN, kernel5)
    
    dilated = cv2.dilate(inv, kernel)

    # opening = cv2.morphologyEx(inv, cv2.MORPH_CLOSE, kernel5)    
    cv2.imwrite("dilated color image.png", tophat)

    
    edges = cv2.Canny(colorToGray,150,150)
    cv2.imwrite("canny edge.png", edges)
    plate = get_contours(imggray, dilated)
    # threshimg = cv2.adaptiveThreshold(colorToGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,13,2)
    # cv2.imwrite("threshimg.png", threshimg)
    # opening = cv2.morphologyEx(threshimg, cv2.MORPH_CLOSE, kernel)    
    # cv2.imwrite("opening gray gaussian.png", opening)
    # dilated = cv2.dilate(threshimg, kernel)
    # cv2.imwrite("dilated gray gaussian.png", dilated)
    # plate = get_contours(imggray, dilated)
    

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # kernel = np.ones((3,3), dtype=np.uint8)
    # closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    # cv2.imwrite('bullshit img.png', closing)
    # _, contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # cnt = max(contours, key=cv2.contourArea)
    # x,y,w,h = cv2.boundingRect(cnt)
    # cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 1)
    # cv2.imwrite('img.png', img)

    