import cv2
import numpy as np

width = 256
height = 256
n_channels = 3

image = np.zeros(shape=(height, width, n_channels), dtype=np.uint8)

def get_point(prompt):
    while True:
        try:
            
            point = int(input(prompt))
            
            if 0 <= point < width:
                return point
            else:
                print(f"Please enter a value between 0 and {width-1}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

try:
    x1 = get_point("Enter x1 (0-255): ")
    y1 = get_point("Enter y1 (0-255): ")
    x2 = get_point("Enter x2 (0-255): ")
    y2 = get_point("Enter y2 (0-255): ")

    if (x1 == x2 and y1 == y2):
        raise ValueError("The two points must be different.")

    point1 = (x1, y1)
    point2 = (x2, y2)

    for i in range(width):
        for j in range(height):

            numerator = ((i - point1[0]) * (point2[1] - point1[1]) - (j - point1[1]) * (point2[0] - point1[0]))
            denominator = ((point2[0] - point1[0]) * (point2[1] - point1[1]))

            if denominator != 0:  
                ratio = numerator / denominator
            else:
                ratio = 0  

            ratio = np.clip(ratio, 0, 1)  

            purple = [128, 0, 128]  
            red = [0, 0, 255]      
            image[j, i] = [(1 - ratio) * purple[k] + ratio * red[k] for k in range(n_channels)]


    cv2.imshow('Gradient Image', image)
    cv2.waitKey(0)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()  












