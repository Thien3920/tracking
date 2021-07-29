import os
import zipfile
path ="/home/thien/Desktop/thien/tracking/outputs/video_1_0/annotations/file_nem.zip"
path_2="/home/thien/Desktop/thien/tracking/outputs/video_1_0/annotations"

fantasy_zip = zipfile.ZipFile(path, 'w')
for folder, subfolders, files in os.walk(path_2):
    for file in files:
        fantasy_zip.write(os.path.join(folder, file), file, compress_type = zipfile.ZIP_DEFLATED)
fantasy_zip.close()

 