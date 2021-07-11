import os
dir1 = "E:/PROJECTS/Deep_fake/first-order-model"   #E:\PROJECTS\Deep_fake\first-order-model
def process():
    code = "python demo.py  --config config/vox-adv-256.yaml --driving_video 1.mp4 --source_image 2.JPG --checkpoint vox-adv-cpk.pth.tar --relative --adapt_scale --cpu"
    os.chdir(dir1)
    return os.system(code)