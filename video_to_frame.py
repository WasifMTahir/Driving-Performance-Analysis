import sys
import argparse

import cv2
print(cv2.__version__)

pathIn='/media/cvlab/Transcend/BDD/bdd-data-v1/videos/videos/train-parts/train-00/videos/0a0dec37-e2f3bc1c.mov'
pathOut='/media/cvlab/Transcend/BDD/bdd-data-v1/videos/videos/train-parts/train-00/videos/0a0dec37-e2f3bc1c/'


def extractImages(pathIn, pathOut):
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      print ('Image: ', '%d', success)
      cv2.imwrite("%d.jpg" % count, image)     # save frame as JPEG file
      count += 1

if __name__=="__main__":
    print("aba")
    #a = argparse.ArgumentParser()
    #a.add_argument("--pathIn", help="path to video")
    #a.add_argument("--pathOut", help="path to images")
    #args = a.parse_args()
    #print(args)
    #extractImages(args.pathIn, args.pathOut)
    extractImages(pathIn, pathOut)
