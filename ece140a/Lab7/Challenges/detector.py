import cv2
import numpy as np
from PIL import Image
import pytesseract



def preprocess_img(img, dilatIt = False):
    """
    Similar to sodoku tutorial 2, get the center of the img
    """
    # img = cv2.imread(img_path, 0)
    # 0 is a simple alias for cv2.IMREAD_GRAYSCALE

    # Add a Gaussian Blur to smoothen the noise
    blur = cv2.GaussianBlur(img.copy(), (9, 9), 1)

    # Threshold the image to get a binary image
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Invert the image to swap the foreground and background
    invert = 255 - thresh

    # Dilate the image to join disconnected fragments
    
    # kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]], np.uint8)
    kernel = np.ones((5,5),np.uint8)
    dilated = cv2.dilate(invert, kernel)
    return dilated



def get_contours(img, dilated, tree=False):

    # Get contours
    if not tree:
        contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print("get_contours  tree is: ", tree)
    print(len(contours))

    # Find the largest 15 contours
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

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
        # result = get_perspective(img, location)
        # result = cv2.rotate(result, cv2.ROTATE_90_CLOCKWISE)
        return location
        # cv2.imwrite("Result.png", result)

    else:    
        no_plate_found = np.array = [[-1,-1], [-1,-1], [-1, -1], [-1,-1]]
        print("No plate found!\n")
        return no_plate_found

def cropImg(img, plate):
    print(plate)
    xVals = plate[:,:,0]
    yVals = plate[:,:,1]
    xmin = min(xVals)
    xmax = max(xVals)
    ymin = min(yVals)
    ymax = max(yVals)
    croppedImg = img[ymin[0]:ymax[0], xmin[0]:xmax[0]]
    return croppedImg

def detect_plate(img, tree = False):
    print("detect plate tree is: ", tree)
    dilated = preprocess_img(img)
    result = get_contours(img, dilated, tree)
    croppedImg = cropImg(img, result)
    return croppedImg

 

def get_text(img, numberOnly = False):

    if numberOnly:
        text = pytesseract.image_to_string(img, lang='eng', config='--psm 11 -c tessedit_char_whitelist=1234567890')
        return text[:6]

    else :
        text = pytesseract.image_to_string(img,lang='eng',config='--psm 11')


    return text
def giveFilename(number):
    images = ["Arizona_47.jpg" ,"Contrast.jpg" ,"Delaware_Plate.png"]
    
    return images[number]

def getImagetoText(number):
    cropped_images = ["./public/images/Arizona_47_Cropped.jpg", "./public/images/Contrast_Cropped.jpg","./public/images/Delaware_Cropped.jpg"]
    numerical = False
    
    if 2 == number:
        numerical = True
    value = get_text(cropped_images[number], numerical)
    if 2 > number:
        return value[:8]
    return value

if __name__ == "__main__":
    images = ["./public/images/Arizona_47.jpg" ,"./public/images/Contrast.jpg" ,"./public/images/Delaware_Plate.png"]
    imageName = ["Arizona_47.jpg", "Contrast.jpg", "Delaware_Plate.png"]
    tree = True
    for i in range(3):
        img = cv2.imread(images[i], 0)
        if 2==i:
            tree = False
        cv2.imwrite(("Cropped "+imageName[0]),detect_plate(img, tree))
    cropped_images = ["./public/images/Arizona_47_Cropped.jpg", "./public/images/Contrast_Cropped.jpg","./public/images/Delaware_Cropped.jpg"]
    values = []
    number = False
    for i in range(len(cropped_images)):
        if 2 == i:
            number = True
        values.append(get_text(cropped_images[i], number))
        
        print(values[i])
