import os
import sys
import pandas as pd

# total arguments
n = len(sys.argv)

if(n < 2):
    print("Please provide folder name\nUsage: py print_pics.py FolderName")
    exit()

path = os.path.join(os.getcwd(), sys.argv[1])
outputData = {'House_Id' : [], 'Image_File_Name' : []}

houses_list = os.listdir(path)
for house in houses_list:
    house_path = os.path.join(path, house)
    image_list = os.listdir(house_path)
    for image in image_list:
        outputData['House_Id'].append(house)
        outputData['Image_File_Name'].append(image)

df = pd.DataFrame(outputData)
df.to_excel(sys.argv[1] + '.xlsx')
