
# coding: utf-8

# # Psudo Code

# list all files
# 
# 
# loop till all files have been moved
#     extract files detail
# 
#     if correspond folder exist == false :
#        create folder
# 
#     move files to corresponding folder
# 
# End

# In[1]:

import PIL.Image
import os
import re


# In[2]:

my_dir = r'C:\Users\User\Desktop\iceland'
os.chdir(my_dir)
img_list = os.listdir()
cwd = os.getcwd()
img_list


# In[4]:

for image in img_list:
    with PIL.Image.open(image) as img:
        #img = PIL.Image.open(image)
        exif_data = img._getexif()
        target_folder = makedirs(exif_data[306],cwd)
        moveto_folder = target_folder +"\\"+image
        current_folder = cwd+"\\"+image
    
    os.rename(current_folder, moveto_folder)


# In[3]:

#判斷路徑，如果路徑不存在則建立路徑
def makedirs (date_time,cwd):
    dateRegex = re.compile(r'\d\d\d\d\S\d\d\S\d\d')
    date0 = dateRegex.search(date_time)
    date1 = date0.group()
    date1 = re.sub(':', '', date1) 
    directory = cwd+"\\"+date1
    if not os.path.isdir(directory):
        os.makedirs (directory)  # os.makedirs 可以一次建立好幾層資料夾
    return directory

