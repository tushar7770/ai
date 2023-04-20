# # # import cv2
# # # import numpy as np

# # # # Load the image
# # # img = cv2.imread("./lab12/a.jpeg")

# # # # Convert RGB to HSV
# # # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# # # # Threshold the image to detect black color
# # # lower_black = np.array([0, 0, 0])
# # # upper_black = np.array([180, 255, 30])
# # # mask = cv2.inRange(hsv, lower_black, upper_black)

# # # # Blob/contour detection
# # # contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # # # Pen edge detection
# # # edges = cv2.Canny(mask, 50, 150, apertureSize=3)

# # # # Pen middle line detection
# # # lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)
# # # for line in lines:
# # #     x1, y1, x2, y2 = line[0]
# # #     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# # # # Pen tip detection
# # # tip_x, tip_y = None, None
# # # for cnt in contours:
# # #     area = cv2.contourArea(cnt)
# # #     if area > 10:
# # #         M = cv2.moments(cnt)
# # #         cx = int(M['m10']/M['m00'])
# # #         cy = int(M['m01']/M['m00'])
# # #         if cv2.pointPolygonTest(cnt, (cx, cy), False) == -1:
# # #             tip_x, tip_y = cx, cy
# # #             cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)
# # #             break

# # # # Display the result
# # # cv2.imshow("Result", img)
# # # cv2.waitKey(0)
# # # cv2.destroyAllWindows()

# # import cv2
# # import numpy as np

# # # Load the image
# # img = cv2.imread("pen_image.jpg")

# # # Convert RGB to HSV
# # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# # # Threshold the image to detect black color
# # lower_black = np.array([0, 0, 0])
# # upper_black = np.array([180, 255, 30])
# # mask = cv2.inRange(hsv, lower_black, upper_black)

# # # Gaussian blur to reduce noise
# # blur = cv2.GaussianBlur(mask, (5, 5), 0)

# # # Blob/contour detection
# # contours, _ = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # # Pen edge detection
# # edges = cv2.Canny(blur, 50, 100, apertureSize=3)

# # # Pen middle line detection
# # lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)
# # for line in lines:
# #     x1, y1, x2, y2 = line[0]
# #     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# # # Pen tip detection
# # tip_x, tip_y = None, None
# # for cnt in contours:
# #     area = cv2.contourArea(cnt)
# #     if area > 10:
# #         hull = cv2.convexHull(cnt)
# #         defects = cv2.convexityDefects(cnt, cv2.convexHull(cnt, returnPoints=False))
# #         if defects is not None:
# #             for i in range(defects.shape[0]):
# #                 s, e, f, d = defects[i][0]
# #                 far = tuple(cnt[f][0])
# #                 if far[1] < img.shape[0]/2 and far[0] > img.shape[1]/3 and far[0] < 2*img.shape[1]/3:
# #                     tip_x, tip_y = far
# #                     cv2.circle(img, (tip_x, tip_y), 5, (0, 0, 255), -1)
# #                     break
# #         if tip_x is not None:
# #             break

# # # Display the result
# # cv2.imshow("Result", img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# import cv2
# import numpy as np

# # Load the image
# img = cv2.imread("drs_probe_image.jpg")

# # Convert RGB to HSV
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# # Threshold the image to detect green color
# lower_green = np.array([45, 50, 50])
# upper_green = np.array([75, 255, 255])
# mask = cv2.inRange(hsv, lower_green, upper_green)

# # Morphological operations to remove noise and fill gaps
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
# mask = cv2.erode(mask, kernel, iterations=2)
# mask = cv2.dilate(mask, kernel, iterations=2)

# # Contour detection
# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Find largest contour and its bounding box
# if len(contours) > 0:
#     probe_contour = max(contours, key=cv2.contourArea)
#     x, y, w, h = cv2.boundingRect(probe_contour)

#     # Edge detection
#     edges = cv2.Canny(mask[y:y+h, x:x+w], 50, 150, apertureSize=3)
#     lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)

#     # Find midline of probe
#     if lines is not None:
#         x1, y1, x2, y2 = lines[0][0]
#         m = (y2 - y1) / (x2 - x1)
#         b = y1 - m * x1
#         mid_y = int(h/2) + y
#         mid_x = int((mid_y - b) / m)

#         # Tip detection
#         midline_mask = np.zeros(mask.shape, dtype=np.uint8)
#         cv2.line(midline_mask, (x+mid_x, y+mid_y), (x+mid_x, y+mid_y), 255, 3)
#         midline_mask = cv2.dilate(midline_mask, kernel, iterations=2)
#         tip_mask = cv2.bitwise_and(mask, midline_mask)
#         tip_contours, _ = cv2.findContours(tip_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         if len(tip_contours) > 0:
#             tip_contour = max(tip_contours, key=cv2.contourArea)
#             tip_moment = cv2.moments(tip_contour)
#             tip_x = int(tip_moment["m10"] / (tip_moment["m00"] + 1e-5))
#             tip_y = int(tip_moment["m01"] / (tip_moment["m00"] + 1e-5))
#             cv2.circle(img, (x+tip_x, y+tip_y), 5, (0, 0, 255), -1)

# # Display the result
# cv2.imshow("Result", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

# Load the image
img = cv2.imread("./lab12/a.jpeg")

# Convert RGB to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Threshold the image to detect blue color
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Morphological operations to remove noise and fill gaps
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask = cv2.erode(mask, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=2)

# Contour detection
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find largest contour and its bounding box
if len(contours) > 0:
    probe_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(probe_contour)

    # Edge detection
    edges = cv2.Canny(mask[y:y+h, x:x+w], 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)

    # Find midline of probe
    if lines is not None:
        x1, y1, x2, y2 = lines[0][0]
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        mid_y = int(h/2) + y
        mid_x = int((mid_y - b) / m)

        # Tip detection
        midline_mask = np.zeros(mask.shape, dtype=np.uint8)
        cv2.line(midline_mask, (x+mid_x, y+mid_y), (x+mid_x, y+mid_y), 255, 3)
        midline_mask = cv2.dilate(midline_mask, kernel, iterations=2)
        tip_mask = cv2.bitwise_and(mask, midline_mask)
        tip_contours, _ = cv2.findContours(tip_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(tip_contours) > 0:
            tip_contour = max(tip_contours, key=cv2.contourArea)
            tip_moment = cv2.moments(tip_contour)
            if tip_moment["m00"] != 0:
                tip_x = int(tip_moment["m10"] / tip_moment["m00"])
                tip_y = int(tip_moment["m01"] / tip_moment["m00"])
                cv2.circle(img, (x+tip_x, y+tip_y), 5, (0, 0, 255), -1)

# Display the result
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()