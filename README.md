生成数据集运行：python ./labelme2coco.py --input_dir ./labelme/train2019 --output_dir ./annotations/train2019 --filename instances_train2019 --labels labels.txt
训练运行：python mdf.py train --dataset=./coco_mdf --model=coco
