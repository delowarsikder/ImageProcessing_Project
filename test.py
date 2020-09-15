import cv2
cat=cv2.imread("images/cat.png")
while True:
    cv2.imshow("cat Image",cat)
    #if we,ve waited at least 1 ms and we,ve pressed ese from keyboard destroy window
    if cv2.waitKey(10) & 0xFF ==27:
        break 
    #if we,ve waited at least 1 ms and we,ve pressed q from keyboard destroy window
    elif cv2.waitKey(0) & 0xFF ==ord('q'):
        break
        
        
cv2.destroyAllWindows()
        