import shutil
import cv2 as cv

sets=['train2020',  'val2020', 'test2020']
for image_set in sets:
    image_ids = open('./%s.txt'%(image_set)).read().strip().split()
    for image_id in image_ids:
        img = cv.imread('images/total2020/%s.jpg' % (image_id))
        json='labelme/total2020/%s.json'% (image_id)
        cv.imwrite('images/%s/%s.jpg' % (image_set,image_id), img)
        cv.imwrite('labelme/%s/%s.jpg' % (image_set,image_id), img)
        shutil.copy(json,'labelme/%s/%s.json' % (image_set,image_id))
print("完成")
