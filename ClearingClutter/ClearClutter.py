import os

# files will contain all the files indide clutteredImg folder
files = os.listdir("clutteredImg")

i = 1
for file in files:
  if file.endswith(".jpg"):
    print(file)
    
    # rename all file with .jpg extension to 1.jpg, 2.jpg, 3.jpg and so on ..
    os.rename(f"clutteredImg/{file}", f"clutteredImg/{i}.jpg")
    i = i + 1
