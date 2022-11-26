def findAngle(hh, mm):
    hh = hh % 12
    h = (hh * 360) // 12 + (mm * 360) // (12 * 60)
    m = (mm * 360) // (60)
    angle = abs(h - m)
    if angle > 180:
        angle = 360 - angle
    return angle
 

if __name__ == '__main__':
 
    hh =5
    mm = 30
 
print(findAngle(hh, mm))