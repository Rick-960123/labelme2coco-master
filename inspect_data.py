import os
import sys,cv2
import numpy as np
from mrcnn import visualize
import mdf as coco
from pycocotools.coco import COCO
ROOT_DIR = os.path.abspath("./")
sys.path.append(ROOT_DIR)
config = coco.CocoConfig()
dataDir='.整体测试图片/train2020'
dataType='train'
# annFile='{}/instances_{}.json'.format(dataDir,dataType)
annFile='整体测试图片/train2020/instances_train2020.json'
COCO_DIR = "./整体测试图片"
coco_1=COCO(annFile)
# Load dataset
dataset = coco.CocoDataset()
dataset.load_coco(COCO_DIR, "train")
dataset.prepare()

print("Image Count: {}".format(len(dataset.image_ids)))
print("Class Count: {}".format(dataset.num_classes))
for i, info in enumerate(dataset.class_info):
    print("{:3}. {:50}".format(i, info['name']))
# Load and display random samples
image_ids = np.random.choice(dataset.image_ids, 10,False)
print(image_ids)
for image_id in image_ids:
    image = dataset.load_image(image_id)
    print(dataset.image_info)
    mask, class_ids = dataset.load_mask(image_id)
    annIds = coco_1.getAnnIds(imgIds=image_id, iscrowd=None)
    anns = coco_1.loadAnns(annIds)
    # for n in range(len(anns)):
    #     x, y, w, h = anns[n]['bbox']
    #     x, y, w, h = int(x), int(y), int(w), int(h)
    #     # print(x, y, w, h)
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255))
    # cv2.imshow('000000' + str(89) + 'result.png', image)
    # cv2.waitKey()
    print(image_id)
    visualize.display_top_masks(image, mask, class_ids, dataset.class_names)