#!/usr/bin/env python3
from os import name
import imageHandler
from datetime import date, datetime

def main():
  folder_path = 'photos'
  img_filename = '1130544.jpg'
  img_path = f'{folder_path}/{img_filename}'
  
  fileInstance = imageHandler.imageClient()
  img = fileInstance.get_image(folder_path, img_filename)
  fileInstance.get_image_time(img_filename, img)

  fileInstance.replace_given_time(img_filename, img, datetime(year=2020, month=1, day=1, hour=1, minute=1, second=1))
  fileInstance.replace_file(folder_path, img_filename, img)
  fileInstance.get_image_time(img_filename, img)

  fileInstance.replace_given_time(img_filename, img, datetime(year=2020, month=1, day=1, hour=1, minute=1, second=1))

if __name__ == '__main__':
  main()