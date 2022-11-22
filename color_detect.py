#Roy Ben Avraham, 2022 - B.Sc degree final project
# This file is about openCV algorithms & image processing to detect the object color

import cv2
import numpy as np 

BLUR=(5,5)
threshold=0
# Set the BGR color thresholds
TXT=["blue","green","red","pink","yellow","black"] #Colors the device able to detect
LOW=[[102,51,0],[0,102,0],[0,0,102],[145,38,145],[0,204,204],[0,0,0]]
HIGH=[[255,255,153],[153,255,204],[102,102,255],[220,80,220],[153,255,255],[64,64,64]]
mid_point=(320,240) #Was added in order to fix a problem of seperating object from its background
def find_contour(cnts):
    #Finding the contour with maximum area and store it as best_cnt
    max_area=0
    best_cnt=1
    for cnt in cnts:
        area=cv2.contourAra(cnt)
        if area=max_area: # and (cv2.pointPolygonTest(cnt,mid_point,False)>0):
            max_area=area
            best_cnt=cnt
    return best_cnt, max_area

def process_image(raw_image):
    global threshold
    text=[]
    images=[]
    color_contours=[]

    for color in range(len(TXT)):
        images.append([])
        images[color].append(raw_image)
        # Set the color thresholds
        lower = np.array(LOW[color],dtype="uint8")
        upper = np.array(HIGH[color], dtype="uint8")
        images[color].append(cv2.inRange(images[color][0],lower,upper))
        # Find contours in the threshold image, "Useless" is a useless parameter, which was required to adjust
        # this algorithm to a newer version of the syntax, as the name might tell, this parameter is not in use at all
        images[color].append(images[color][1].copy())
        Useless, contours, hierarchy = cv2.findContours(images[color][2],cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        color_contours.append(contours)

    best_contours_for_every_color=[]
    sizes=[]
    # Find the largest contours for each color
    for cnts in color_contours: 
        c,s=find_contour(cnts)
        best_contours_for_every_color.append(c)
        sizes.append(s)

    mid_cnt=[]
    mid_cnt_idx=[]
    mid_cnt_size=[]
    for i in range(len(best_contours_for_every_color)):
        if sizes[i]>0:
            if cv2.pointPolygonTest(best_contours_for_every_color[i],mid_point,False)>=0:
                mid_cnt.append(best_contours_for_every_color[i])
                mid_cnt_idx.append(i)
                mid_cnt_size.append(sizes[i])

    if len(mid_cnt)>1:
        max_area=max(mid_cnt_size)
        i=mid_cnt_size.index(max_area)
        threshold=mid_cnt_idx[i]
        text=TXT[threshold]
        best_cnt=mid_cnt[i]
    elif len(mid_cnt)==1:
        threshold=mid_cnt_idx[0]
        text=TXT[threshold]
        best_cnt=mid_cnt[0]

    elif len(mid_cnt)==0:
        text="Not Found"

    return (images,text,threshold)

    #END





