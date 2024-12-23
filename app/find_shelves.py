import cv2
import numpy as np

def image_resize(picture_path, x, y):
    img = cv2.imread(picture_path)

    # Resize to a standard size (e.g., 600x800)
    # resized_img = cv2.resize(img, (600, 800))
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, (7, 7), 0)
    edges = cv2.Canny(blurred_img, 50, 150)
    #_, thresh_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
    #contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=50, maxLineGap=20)

    #filter the lines
    lines_filtered = filter_lines(lines)

    #point to find

    # Step 4: Draw detected straight lines on the original image
    if lines_filtered is not None:
        for dim in lines_filtered:
            for line in dim:
                x1, y1, x2, y2 = line[0]  # Each line is represented by two points (x1, y1) and (x2, y2)
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(img, (x, y), radius=10, color=(0, 0, 255), thickness=-1)
    
    region = classify_region((x, y), lines_filtered)
    # print(name_region(region))
    region_name = name_region(region)

    return region_name, img


#returns true if the line is horizontal, false if the line is vertical, takes vector of length = 4
def classify_line(line_vec):
    if abs(line_vec[0] - line_vec[2]) == 0:
        return False
    return abs(line_vec[1] - line_vec[3])/abs(line_vec[0] - line_vec[2]) < 1 #it's horizontal if both y-coordinates are very similar

#takes a vector of lines, return a thinned out vector of lines, with no lines close together, also sorts them by horizontal or vertical
def filter_lines(lines):
    horiz_lines = []
    vert_lines = []
    out = [horiz_lines, vert_lines]
    for i in lines:
        flag = True
        for dimension in out:
            for j in dimension:
                #if one is horizontal and the other is vertical don't compare
                if classify_line(i[0]) == classify_line(j[0]):
                    if classify_line(i[0]):
                        if abs(i[0][1] - j[0][1]) < 40:
                            flag = False
                    else:
                        if abs(i[0][0] - j[0][0]) < 40:
                            flag = False
        if flag:
            if (classify_line(i[0])):
                horiz_lines.append(i)
            else:
                vert_lines.append(i)
    return out

#takes an x-y coordinate and fridge lines, classifies what part of the fridge it is in        
def classify_region(coord, lines):
    row = 0
    column = 0
    #loop through horizontal lines, if the y-coordinate of the line is less than coord[1], increment row
    for i in lines[0]:
        if i[0][1] > coord[1]: #and i[0][0] < coord[0] and i[0][2] > coord[0]:
            row += 1
    for i in lines[1]:
        if i[0][0] < coord[0]: #and i[0][1] < coord[1] and i[0][3] > coord[1]:
            column += 1
    return (row, column)

def name_region(coord):
    out = "is " + str(coord[0])
    if str(coord[0]) == 1:
        out += " shelf"
    else:
        out += " shelves"
    out += " up and " + str(coord[1]) + " to the right."
    return out

if __name__ == "__main__":
    region_name, img = image_resize("C:\\Users\\jdfab\\fa24_cs222_johnf8\\main-project-team81_fridgevision\\fridge-pics\\fridge_pic_0.png")

    print(region_name)
    cv2.imshow('Straight Lines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
