from __future__ import print_function

import boto3
import os
import sys
import uuid
import cv2

def lambda_handler(event, context):
	print ("OpenCV installed version:", cv2.__version__)
	return "It works!"

if __name__ == "__main__":
	lambda_handler(42, 42)
