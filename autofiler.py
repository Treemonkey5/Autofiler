#! python3

import os,send2trash,shutil,re

filetypes=['pdf','docx','ppt','xlsx','zip','jpg','pptx']
source=('C:\\Users\\Parker\\Downloads')

for extension in filetypes:

    destination=('C:\\Users\\Parker\\Documents\\%s'%(extension.upper()))

    for file in (os.listdir(source)):
        k=file.lower()
        if k.endswith(extension.lower()):
            if os.path.exists(destination):
                try:
                    shutil.move('%s\\%s'%(source,file), destination)
                except shutil.Error:
                    send2trash.send2trash('%s\\%s'%(source,file))

            else:
                os.mkdir(destination)
                try:
                    shutil.move('%s\\%s'%(source,file), destination)
                except shutil.Error:
                    send2trash.send2trash('%s\\%s'%(source,file))
