import /Todo

import os

import subprocess


#====================================================
# Tools
#====================================================

# List all notes path and title

def list_note():
    jsonList = []
    for root, dirs, files in os.walk("/home/echo/TheNote/Todo/"):
        name = files
        path = os.path.join(root, files)
        dict = {
            fileName : name
            filePath : path
        }
        jsonList.append(dict)
    return dict

def read_note(pathWithFileName):
    with open(pathWithFileName, "r", encoding="utf-8") as f: 
        note = f.read()
    return note


def search_note(path):

def create_folder():


def move_note():

def write_note():

def archive_note():

def clear_inbox_line():


#====================================================

#====================================================








#====================================================

#====================================================

