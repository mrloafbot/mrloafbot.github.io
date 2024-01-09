## Scirpt to create a new post in a folder 

import os
import sys
from datetime import date

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

newPostPath = os.path.join( script_directory, 'content', 'post')

## get name from input

postName = input('Name of Post\n')

postFileName = postName.replace(" ", "_")

## remove any spaces

today = str(date.today())

postFolderName = today+"__"+postName


newPostPath = os.path.join( script_directory, 'content', 'post', postFolderName)

os.mkdir(newPostPath)

newPostFile = os.path.join(newPostPath, (postFileName+".md"))

headerTemplate = '''
+++
title = 'postName'
date = currentDate
draft = false
tags = []
+++
'''

headerDate = headerTemplate.replace('currentDate', today )
headerTitle =  headerDate.replace('postName', postName)
headerOut = headerTitle


with open(newPostFile, 'w', encoding='utf-8') as f:
    f.write(headerOut)

## add date


## Make new folder in content/poss  dir_postname


## make index.md in content/post/folder

