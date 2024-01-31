## Scirpt to create a new post in a folder 

import os
import sys
from datetime import date

## Gather Variables
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
newPostPath = os.path.join(script_directory, 'content', 'post')
today = str(date.today())
headerTemplate = '''
+++
title = 'postName'
date = currentDate
draft = true
tags = []
authors = ['mrloafbot']
image = ''
+++
'''

## get post name from input
postName = input('Name of Post\n')

## process variables
postCleanName = (postName.replace(" ", "_")).lower()
postFolderName = today+"__"+postCleanName
newPostPath = os.path.join( script_directory, 'content', 'post', postFolderName)
newPostFile = os.path.join(newPostPath, "index.md")
headerDate = headerTemplate.replace('currentDate', today )
headerTitle =  headerDate.replace('postName', postName)
headerOut = headerTitle

## make output
os.mkdir(newPostPath)
with open(newPostFile, 'w', encoding='utf-8') as f:
    f.write(headerOut)
