import sys
import os
from PIL import Image


# grab the first argument and the second
folder_with_images_to_be_converted = sys.argv[1]
new_folder_with_images_converted = sys.argv[2]

# check if new/ exists and if not create it
if not os.path.isdir(new_folder_with_images_converted):
  os.mkdir(new_folder_with_images_converted)

# loop through Pokedex and convert images to PNGs and save them to the new folder
for element in os.listdir(folder_with_images_to_be_converted):
  img = Image.open(folder_with_images_to_be_converted + element)
  clean_name = os.path.splitext(element)
  img.save(new_folder_with_images_converted + clean_name[0] + ".png", 'png')
  print('OK')
