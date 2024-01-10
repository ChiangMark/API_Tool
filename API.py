from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
import time
import configparser
import requests
import unittest
import json
import os  #for sending image
import traceback
import yaml

# define color
class colors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

#config = configparser.ConfigParser()
config = configparser.RawConfigParser() #fix that url include %
config.read("Params.ini")
token = config['info']['Token']
FAIL_COUNT = 0
SUCCESS_COUNT = 0
TOTAL_COUNT = 0

def clean():
    file = open('output.txt', 'w')
    file.close ()
    
    file = open('selection.txt', 'w')
    file.close ()

def create_APIs():      
    def select_all():
        for i in APIs:
            i.select()
                
    def deselect_all():
        for i in APIs:
            i.deselect()  
        
    APIs_text = ['Authentication', 'Import Person', 'Update Person Info V2', "Add Person's Faces", "Delete Person", "Delete Person's Face", "Data Purge for History Record",
                 "Query Person", "Image Quality Check", "List Workstations and Camera", "Query History Record", "Central Health Check", "Workstation Health Check", 
                 "Camera Health Check", "Search Faces", "Activate Camera", "List Camera (VMS)", "Create Group", "Update a Group", "Delete a Group", "List Group", 
                 "Move Group Members", "Create Group Tag (Sub-Group)", "List Group/All tags", "Update Group tag (Sub-Group)", "Delete Group Tags", "Update Group Member's Tag (Sub-Group)",
                 "List Group Member", "List Group Member's Tag", "Query Setting", "Update Person", "Update Snapshot", "Change Database"]
    APIs = []
    root = Tk()
    root.title("APIs Selection")
    root.geometry('400x800')
    
    # combo_box = StringVar(root)
    # combo_box.set("None")
    # dropdownlist = OptionMenu(root, combo_box, "None", "by personId", "by snapshotId")
    # dropdownlist.place(x=110, y=597)
    
    Button(root, text = 'Select All', height=2, width=10, command=select_all).place(x=80, y=670)
    Button(root, text = 'Deselect All', height=2, width=10, command=deselect_all).place(x=230, y=670)
    Btn =tk.Button(root, text= "Confirm", height=3, width=15, command=root.destroy)
    Btn.place(x=140, y=730)
    
# define value to every var
    for index, item in enumerate(APIs_text):
        var = tk.IntVar()
        APIs.append(Checkbutton(root, text=item, variable=var, onvalue=1, offvalue=0))
        APIs[index].place(y=20*[index][0])
        if index == 0:
            var1 = var
        elif index == 1:
            var2 = var
        elif index == 2:
            var3 = var
        elif index == 3:
            var4 = var
        elif index == 4:
            var5 = var
        elif index == 5:
            var6 = var
        elif index == 6:
            var7 = var
        elif index == 7:
            var8 = var
        elif index == 8:
            var9 = var
        elif index == 9:
            var10 = var
        elif index == 10:
            var11 = var
        elif index == 11:
            var12 = var
        elif index == 12:
            var13 = var
        elif index == 13:
            var14 = var
        elif index == 14:
            var15 = var
        elif index == 15:
            var16 = var
        elif index == 16:
            var17 = var
        elif index == 17:
            var18 = var
        elif index == 18:
            var19 = var
        elif index == 19:
            var20 = var
        elif index == 20:
            var21 = var
        elif index == 21:
            var22 = var
        elif index == 22:
            var23 = var
        elif index == 23:
            var24 = var
        elif index == 24:
            var25 = var
        elif index == 25:
            var26 = var
        elif index == 26:
            var27 = var
        elif index == 27:
            var28 = var
        elif index == 28:
            var29 = var
        elif index == 29:
            var30 = var
        elif index == 30:
            var31 = var
        elif index == 31:
            var32 = var
        else:
            var33 = var
    mainloop()
    
    file = open('selection.txt', 'a')
    file.write("Authentication: ")
    file.write(str(var1.get()))
    file.write("\n")
    file.write("Import Person: ")
    file.write(str(var2.get()))
    file.write("\n")
    file.write("Update Person Info V2: ")
    file.write(str(var3.get()))
    file.write("\n")
    file.write("Add Person's Faces: ")
    file.write(str(var4.get()))
    file.write("\n")
    file.write("Delete Person: ")
    file.write(str(var5.get()))
    file.write("\n")
    file.write("Delete Person's Face: ")
    file.write(str(var6.get()))
    file.write("\n")
    file.write("Data Purge for History Record: ")
    file.write(str(var7.get()))
    file.write("\n")
    file.write("Query Person: ")
    file.write(str(var8.get()))
    file.write("\n")
    file.write("Image Quality Check: ")
    file.write(str(var9.get()))
    file.write("\n")
    file.write("List Workstations and Camera: ")
    file.write(str(var10.get()))
    file.write("\n")
    file.write("Query History Record: ")
    file.write(str(var11.get()))
    file.write("\n")
    file.write("Central Health Check: ")
    file.write(str(var12.get()))
    file.write("\n")
    file.write("Workstation Health Check: ")
    file.write(str(var13.get()))
    file.write("\n")
    file.write("Camera Health Check: ")
    file.write(str(var14.get()))
    file.write("\n")
    file.write("Search Faces: ")
    file.write(str(var15.get()))
    file.write("\n")
    file.write("Activate Camera: ")
    file.write(str(var16.get()))
    file.write("\n")
    file.write("List Camera (VMS): ")
    file.write(str(var17.get()))
    file.write("\n")
    file.write("Create Group: ")
    file.write(str(var18.get()))
    file.write("\n")
    file.write("Update a Group: ")
    file.write(str(var19.get()))
    file.write("\n")
    file.write("Delete a Group: ")
    file.write(str(var20.get()))
    file.write("\n")
    file.write("List Group: ")
    file.write(str(var21.get()))
    file.write("\n")
    file.write("Move Group Members: ")
    file.write(str(var22.get()))
    file.write("\n")
    file.write("Create Group Tag (Sub-Group): ")
    file.write(str(var23.get()))
    file.write("\n")
    file.write("List Group/All tags: ")
    file.write(str(var24.get()))
    file.write("\n")
    file.write("Update Group tag (Sub-Group): ")
    file.write(str(var25.get()))
    file.write("\n")
    file.write("Delete Group Tags: ")
    file.write(str(var26.get()))
    file.write("\n")
    file.write("Update Group Member's Tag (Sub-Group): ")
    file.write(str(var27.get()))
    file.write("\n")
    file.write("List Group Member: ")
    file.write(str(var28.get()))
    file.write("\n")
    file.write("List Group Member's Tag: ")
    file.write(str(var29.get()))
    file.write("\n")
    file.write("Query Setting: ")
    file.write(str(var30.get()))
    file.write("\n")
    file.write("Update Person: ")
    file.write(str(var31.get()))
    file.write("\n")
    file.write("Update Snapshot: ")
    file.write(str(var32.get()))
    file.write("\n")
    file.write("Change Database: ")
    file.write(str(var33.get()))
    file.write("\n")
    # file.write("----------------------------------------------------------------------------------------------------------------")
    # file.write("\n")
    # file.write("Mode: ")
    # file.write(str(combo_box.get()))
    # file.write("\n")
    
def Authentication():
    # read selection.txt to decide whether to run
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[0] == "Authentication: 1\n"):
        try: 
            url = config["info"]['IP'] + config['Authentication']['url_Authentication'] 
            content_Type = config['info']['Content-Type_urlencoded']
            
            with open('Authentication_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
            'Content-Type': content_Type
            }
            
            response = requests.request("POST", url, headers=headers, data=payload)
            null = "null"
            output = eval(response.text)
            if ("statusCode" in output):
                print(colors.FAIL + "Authentication Result: " + colors.RESET, response.text, "\n")
                file = open('output.txt', 'a')
                file.write("Authentication Result: ")
                file.write(response.text)
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "Authentication Result: " + colors.RESET, response.text, "\n")
                file = open('output.txt', 'a')
                file.write("Authentication Result: ")
                file.write(response.text)
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1    
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "Authentication Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("Authentication Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Authentication API!")
        
def ImportPerson():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()
    
    if (line[1] == "Import Person: 1\n"):
        try:
            global FAIL_COUNT
            global SUCCESS_COUNT
            
            url = config["info"]['IP'] + config['ImportPerson']['url_ImportPerson']
            headers = {
                'Authorization': token
            }
            with open('ImportPerson_Params.yaml', 'rb') as paras: 
                conf = yaml.safe_load(paras)
                
                with open(conf['snapshot'], 'rb') as img:
                    name_img = os.path.basename(conf['snapshot'])
                    
                    if 'coverImage' in conf and conf['coverImage']:
                        with open(conf['coverImage'], 'rb') as coverimg:
                            name_coverimg = os.path.basename(conf['coverImage'])
                            with open('ImportPerson_Params.yaml', 'r') as y:
                                files = yaml.load(y, Loader = yaml.FullLoader)
                            files.update({
                                'snapshot': (name_img, img,'multipart/form-data'),
                                'coverImage': (name_coverimg, coverimg,'multipart/form-data')
                            })
                            response = requests.request("POST", url, headers=headers, files=files)
                            true = "true"
                            false = "false"
                            null = "null"
                            list = eval(response.text)
                    else:
                        with open('ImportPerson_Params.yaml', 'r') as y:
                            files = yaml.load(y, Loader = yaml.FullLoader)
                            files.update({
                                'snapshot': (name_img, img,'multipart/form-data')
                            })
                        response = requests.request("POST", url, headers=headers, files=files)
                        true = "true"
                        false = "false"
                        null = "null"
                        list = eval(response.text)
                if ("statusCode" in list):
                    print(colors.FAIL + "ImportPerson Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                    file = open('output.txt', 'a')
                    file.write("ImportPerson Result: ")
                    file.write(json.dumps(list, indent = 3))
                    file.write("\n")
                    FAIL_COUNT += 1  
                else:
                    print(colors.OK + "ImportPerson Result:" + colors.RESET, json.dumps(list, indent = 5), "\n")
                    file = open('output.txt', 'a')
                    file.write("ImportPerson Result: ")
                    file.write(json.dumps(list, indent = 5))
                    file.write("\n")
                    SUCCESS_COUNT += 1
        except Exception as e:
            traceback.print_exc() 
            print(colors.FAIL + "ImportPerson Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ImportPerson Result: ")
            file.write(repr(e))
            file.write("\n")  
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run ImportPerson API!")
    
def UpdatePersonInfoV2():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()
    
    if (line[2] == "Update Person Info V2: 1\n"):
        try:
            global FAIL_COUNT
            global SUCCESS_COUNT
            
            url = config["info"]['IP'] + config['UpdatePersonInfoV2']['url_UpdatePersonInfoV2']
            headers = {
                'Authorization': token
            }
            with open('UpdatePersonInfoV2_Params.yaml', 'rb') as paras: 
                conf = yaml.safe_load(paras)
                if 'coverImage' in conf and conf['coverImage']:
                    with open(conf['coverImage'], 'rb') as coverimg:
                        name_coverimg = os.path.basename(conf['coverImage'])
                        with open('UpdatePersonInfoV2_Params.yaml', 'r') as y:
                            files = yaml.load(y, Loader = yaml.FullLoader)
                        files.update({
                            'coverImage': (name_coverimg, coverimg,'multipart/form-data')
                        })
                        response = requests.request("POST", url, headers=headers, files=files)
                else:
                    with open('UpdatePersonInfoV2_Params.yaml', 'r') as y:
                        files = yaml.load(y, Loader = yaml.FullLoader)
                        response = requests.request("POST", url, headers=headers, files=files)
                
                if (len(response.text) == 0):
                    print(colors.OK + "UpdatePersonInfoV2 Result:" + colors.RESET, response.text, "\n")
                    print("Please check the result on the Central console !!!", "\n")
                    file = open('output.txt', 'a')
                    file.write("UpdatePersonInfoV2 Result: ")
                    file.write(response.text)
                    file.write("\n")
                    SUCCESS_COUNT += 1  
                else:
                    list = eval(response.text)
                    print(colors.FAIL + "UpdatePersonInfoV2 Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                    file = open('output.txt', 'a')
                    file.write("UpdatePersonInfoV2 Result: ")
                    file.write(json.dumps(list, indent = 3))
                    file.write("\n")
                    FAIL_COUNT += 1   
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "UpdatePersonInfoV2 Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("UpdatePersonInfoV2 Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1   
    else:
        print("NO selection made to run Update Person InfoV2 API!")

def AddPersonFace():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[3] == "Add Person's Faces: 1\n"):
        try:
            global FAIL_COUNT
            global SUCCESS_COUNT
            
            url = config["info"]['IP'] + config['AddPersonFace']['url_AddPersonFace']
            headers = {
                'Authorization': token
            }
            with open('AddPerson_Params.yaml', 'rb') as paras: 
                conf = yaml.safe_load(paras)
                with open(conf['snapshot'], 'rb') as img:
                    name_img = os.path.basename(conf['snapshot'])
                    with open('AddPerson_Params.yaml', 'r') as y:
                        files = yaml.load(y, Loader = yaml.FullLoader)
                    files.update({
                        'snapshot': (name_img, img,'multipart/form-data')
                    })
                    response = requests.request("POST", url, headers=headers, files=files)
                list = eval(response.text)
                if ("statusCode" in list):
                    print(colors.FAIL + "AddPersonFace Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                    file = open('output.txt', 'a')
                    file.write("AddPersonFace Result: ")
                    file.write(json.dumps(list, indent = 3))
                    file.write("\n")
                    FAIL_COUNT += 1  
                else:
                    print(colors.OK + "AddPersonFace Result:" + colors.RESET, json.dumps(list, indent = 5), "\n")
                    file = open('output.txt', 'a')
                    file.write("AddPersonFace Result: ")
                    file.write(json.dumps(list, indent = 5))
                    file.write("\n")
                    SUCCESS_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "AddPersonFace Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("AddPersonFace Result: ")
            file.write(repr(e))
            file.write("\n")  
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Add Person's Faces API!") 
       
def DeletePerson():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[4] == "Delete Person: 1\n"):
        try:
            url = config["info"]['IP'] + config['DeletePerson']['url_DeletePerson'] 
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('DeletePerson_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            if (len(response.text) == 0):
                print(colors.OK + "DeletePerson Result:" + colors.RESET, response.text, "\n")  
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("DeletePerson Result: ")
                file.write(response.text)
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "DeletePerson Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("DeletePerson Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "DeletePerson Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("DeletePerson Result: ")
            file.write(repr(e))
            file.write("\n")  
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Delete Person API!")
    
def DeletePersonFace():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[5] == "Delete Person's Face: 1\n"):
        try:
            url = config["info"]['IP'] + config['DeletePersonFace']['url_DeletePersonFace']   
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('DeletePersonFace_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            if (len(response.text) == 0):
                print(colors.OK + "DeletePersonFace Result:" + colors.RESET, response.text)   
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("DeletePersonFace Result: ")
                file.write(response.text)
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "DeletePersonFace Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("DeletePersonFace Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "DeletePersonFace Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("DeletePersonFace Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Delete Person's Face API!")       

def DataPurgeForHistoryRecord():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[6] == "Data Purge for History Record: 1\n"):
        try:
            url = config["info"]['IP'] + config['DataPurgeForHistoryRecord']['url_DataPurgeForHistoryRecord']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('DataPurgeforHistoryRecord_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "DataPurgeForHistoryRecord Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("DataPurgeForHistoryRecord Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "DataPurgeForHistoryRecord Result:" + colors.RESET, json.dumps(list, indent = 5), "\n") 
                file = open('output.txt', 'a')
                file.write("DataPurgeForHistoryRecord Result: ")
                file.write(json.dumps(list, indent = 5))
                file.write("\n")  
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1   
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "DataPurgeForHistoryRecord Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("DataPurgeForHistoryRecord Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Data Purge for History Record API!")        
    
def QueryPerson():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[7] == "Query Person: 1\n"):
        try:
            url = config["info"]['IP'] + config['QueryPerson']['url_QueryPerson'] 
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('QueryPerson_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            null = "null"
            false = "false"
            true = "true"
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "QueryPerson Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("QueryPerson Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "QueryPerson Result:" + colors.RESET, json.dumps(list, indent = 5), "\n")   
                file = open('output.txt', 'a')
                file.write("QueryPerson Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1   
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "QueryPerson Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("QueryPerson Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Query Person API!")    
    
def ImageQualityCheck():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[8] == "Image Quality Check: 1\n"):
        try:
            global FAIL_COUNT
            global SUCCESS_COUNT
            
            url = config["info"]['IP'] + config['ImageQualityCheck']['url_ImageQualityCheck']
            headers = {
                'Authorization': token
            }
            with open('ImageQualityCheck_Params.yaml', 'rb') as paras: 
                conf = yaml.safe_load(paras)
                with open(conf['image'], 'rb') as img:
                    name_img = os.path.basename(conf['image'])
                    with open('ImageQualityCheck_Params.yaml', 'r') as y:
                        files = yaml.load(y, Loader = yaml.FullLoader)
                    files.update({
                        'image': (name_img, img,'multipart/form-data')
                    })
                    response = requests.request("POST", url, headers=headers, files=files)
                true = "true"
                false = "false"
                null = "null"
                list = eval(response.text)
                if ("statusCode" in list):
                    print(colors.FAIL + "ImageQualityCheck Result: " + colors.RESET, json.dumps(list, indent = 3), "\n")
                    file = open('output.txt', 'a')
                    file.write("ImageQualityCheck Result: ")
                    file.write(json.dumps(list, indent = 3))
                    file.write("\n")
                    FAIL_COUNT += 1  
                else:
                    print(colors.OK + "ImageQualityCheck Result: " + colors.RESET, json.dumps(list, indent = 5), "\n")
                    file = open('output.txt', 'a')
                    file.write("ImageQualityCheck Result: ")
                    file.write(json.dumps(list, indent = 5))
                    file.write("\n")
                    SUCCESS_COUNT += 1  
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "ImageQualityCheck Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ImageQualityCheck Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Image Quality Check API!")  
    
def ListWorkstationListandCamera():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[9] == "List Workstations and Camera: 1\n"):
        try:
            url = config["info"]['IP'] + config['ListWorkstationListandCamera']['url_ListWSandCam']
            content_Type = config['info']['Content-Type_urlencoded']
            
            payload = {}
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            null = "null"
            true = "true"
            false = "false"
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "ListWorkstationListandCamera Result: " + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("ListWorkstationListandCamera Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "ListWorkstationListandCamera Result: " + colors.RESET, json.dumps(list, indent = 5), "\n")
                file = open('output.txt', 'a')
                file.write("ListWorkstationListandCamera Result: ")
                file.write(json.dumps(list, indent = 5))
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "ListWorkstationListandCamera Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ListWorkstationListandCamera Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run List Workstations and Camera API!") 
    
def QueryHistoryRecord():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[10] == "Query History Record: 1\n"):
        try:
            url = config["info"]['IP'] + config['QueryHistoryRecord']['url_QueryHistoryRecord']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('QueryHistoryRecord_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            null = "null"
            false = "false"
            true = "true"
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "QueryHistoryRecord Result: " + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("QueryHistoryRecord Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "QueryHistoryRecord Result: " + colors.RESET, json.dumps(list, indent = 5), "\n")
                file = open('output.txt', 'a')
                file.write("QueryHistoryRecord Result: ")
                file.write(json.dumps(list, indent = 5))
                file.write("\n")   
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1   
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "QueryHistoryRecord Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("QueryHistoryRecord Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Query History Record API!") 
        
def CentralHealthCheck():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[11] == "Central Health Check: 1\n"):
        try:
            url = config["info"]['IP'] + config['CentralHealthCheck']['url_CentralHealthCheck']
            
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            
            true = "true"
            false = "false"
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "CentralHealthCheck Result: " + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("CentralHealthCheck Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")   
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "CentralHealthCheck Result: " + colors.RESET, json.dumps(list, indent = 3), "\n")   
                file = open('output.txt', 'a')
                file.write("CentralHealthCheck Result: ")
                file.write(json.dumps(list, indent = 5))
                file.write("\n")   
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "CentralHealthCheck Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("CentralHealthCheck Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Central Health Check API!") 
    
def WorkstationHealthCheck():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[12] == "Workstation Health Check: 1\n"):
        try:
            url = config["info"]['IP'] + config['WorkstationHealthCheck']['url_WorkstationHealthCheck']

            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            
            true = "true"
            false = "false"
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "WorkstationHealthCheck Result: " + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("WorkstationHealthCheck Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")   
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "WorkstationHealthCheck Result: " + colors.RESET, json.dumps(list, indent = 3), "\n")  
                file = open('output.txt', 'a')
                file.write("WorkstationHealthCheck Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")    
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "WorkstationHealthCheck Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("WorkstationHealthCheck Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Workstation Health Check API!") 
    
def CameraHealthCheck():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[13] == "Camera Health Check: 1\n"):
        try: 
            url = config["info"]['IP'] + config['CameraHealthCheck']['url_CameraHealthCheck']

            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            
            true = "true"
            false = "false"
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "CameraHealthCheck Result: " + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("CameraHealthCheck Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n") 
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "CameraHealthCheck Result: " + colors.RESET, json.dumps(list, indent = 3), "\n")  
                file = open('output.txt', 'a')
                file.write("CameraHealthCheck Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")  
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "CameraHealthCheck Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("CameraHealthCheck Result: ")
            file.write(repr(e))
            file.write("\n") 
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Camera Health Check API!") 
    
def SearchFace():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[14] == "Search Faces: 1\n"):
        try:
            global FAIL_COUNT
            global SUCCESS_COUNT
            
            url = config["info"]['IP'] + config['SearchFace']['url_SearchFace']
            headers = {
                'Authorization': token
            }
            with open('SearchFace_Params.yaml', 'rb') as paras: 
                conf = yaml.safe_load(paras)
                with open(conf['image'], 'rb') as img:
                    name_img = os.path.basename(conf['image'])
                    with open('SearchFace_Params.yaml', 'r') as y:
                        files = yaml.load(y, Loader = yaml.FullLoader)
                    files.update({
                        'image': (name_img, img,'multipart/form-data')
                    })
                    response = requests.request("POST", url, headers=headers, files=files)
                list = eval(response.text)
                if ("statusCode" in list):
                    print(colors.FAIL + "SearchFace Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                    file = open('output.txt', 'a')
                    file.write("SearchFace Result: ")
                    file.write(json.dumps(list, indent = 3))
                    file.write("\n")  
                    FAIL_COUNT += 1  
                else:
                    print(colors.OK + "SearchFace Result:" + colors.RESET, json.dumps(list, indent = 5), "\n")
                    file = open('output.txt', 'a')
                    file.write("SearchFace Result: ")
                    file.write(json.dumps(list, indent = 5))
                    file.write("\n")  
                    SUCCESS_COUNT += 1
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "SearchFace Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("SearchFace Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Search Faces API!") 
    
def ActivateCamera():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[15] == "Activate Camera: 1\n"):
        try:
            url = config["info"]['IP'] + config['ActivateCamera']['url_ActivateCamera']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('ActivateCamera_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            if (len(response.text) == 0):
                print(colors.OK + "ActivateCamera Result:" + colors.RESET, response.text)   
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("ActivateCamera Result: ")
                file.write(response.text)
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "ActivateCamera Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("ActivateCamera Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "ActivateCamera Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ActivateCamera Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Activate Camera API!") 
    
def ListCamera():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[16] == "List Camera (VMS): 1\n"):
        try:
            print ("Wait for completion...")
            url = config["info"]['IP'] + config['ListCamera']['url_ListCamera']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('ListCamera_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            false = "false"
            true = "true"
            null = "null"
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "ListCamera Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("ListCamera Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "ListCamera Result:" + colors.RESET, json.dumps(list, indent = 10), "\n")   
                file = open('output.txt', 'a')
                file.write("ListCamera Result: ")
                file.write(json.dumps(list, indent = 10))
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "ListCamera Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ListCamera Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run List Camera (VMS) API!") 
    
def CreateGroup():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[17] == "Create Group: 1\n"):
        try:
            url = config["info"]['IP'] + config['CreateGroup']['url_CreateGroup']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('CreateGroup_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "CreateGroup Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("CreateGroup Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "CreateGroup Result:" + colors.RESET, json.dumps(list, indent = 5), "\n") 
                file = open('output.txt', 'a')
                file.write("CreateGroup Result: ")
                file.write(json.dumps(list, indent = 5))
                file.write("\n")  
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "CreateGroup Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("CreateGroup Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Create Group API!")
    
def UpdateGroup():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[18] == "Update a Group: 1\n"):
        try: 
            url = config["info"]['IP'] + config['UpdateGroup']['url_UpdateGroup']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('UpdateGroup_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            if (len(response.text) == 0):
                print(colors.OK + "UpdateGroup Result:" + colors.RESET, response.text)   
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("UpdateGroup Result: ")
                file.write(response.text)
                file.write("\n") 
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "UpdateGroup Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("UpdateGroup Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n") 
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "UpdateGroup Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("UpdateGroup Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Update a Group API!")
    
def DeleteGroup():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[19] == "Delete a Group: 1\n"):
        try:
            url = config["info"]['IP'] + config['DeleteGroup']['url_DeleteGroup']    
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('DeleteGroup_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            if (len(response.text) == 0):
                print(colors.OK + "DeleteGroup Result:" + colors.RESET, response.text)   
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("DeleteGroup Result: ")
                file.write(response.text)
                file.write("\n") 
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "DeleteGroup Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("DeleteGroup Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n") 
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "DeleteGroup Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("DeleteGroup Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Delete a Group API!")
    
def ListGroup():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[20] == "List Group: 1\n"):
        try:
            url = config["info"]['IP'] + config['ListGroup']['url_ListGroup']   
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('ListGroup_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "ListGroup Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("ListGroup Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n") 
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "ListGroup Result:" + colors.RESET, json.dumps(list, indent = 5), "\n")   
                file = open('output.txt', 'a')
                file.write("ListGroup Result: ")
                file.write(json.dumps(list, indent = 5))
                file.write("\n") 
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1   
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "ListGroup Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ListGroup Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run List Group API!")
    
def MoveGroupMember():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[21] == "Move Group Members: 1\n"):
        try:
            url = config["info"]['IP'] + config['MoveGroupMember']['url_MoveGroupMember']  
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('MoveGroupMember_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            if (len(response.text) == 0):
                print(colors.OK + "MoveGroupMember Result:" + colors.RESET, response.text)   
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("MoveGroupMember Result: ")
                file.write(response.text)
                file.write("\n") 
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "MoveGroupMember Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("MoveGroupMember Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n") 
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "MoveGroupMember Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("MoveGroupMember Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Move Group Members API!")
    
def CreateGroupTag():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[22] == "Create Group Tag (Sub-Group): 1\n"):
        try:
            url = config["info"]['IP'] + config['CreateGroupTag']['url_CreateGroupTag'] 
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('CreateGroupTag_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "CreateGroupTag Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("CreateGroupTag Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n") 
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "CreateGroupTag Result:" + colors.RESET, json.dumps(list, indent = 5), "\n")   
                file = open('output.txt', 'a')
                file.write("CreateGroupTag Result: ")
                file.write(json.dumps(list, indent = 5))
                file.write("\n") 
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1      
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "CreateGroupTag Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("CreateGroupTag Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Create Group Tag (Sub-Group) API!")
    
def ListGroupAllTag():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[23] == "List Group/All tags: 1\n"):
        try:
            url = config["info"]['IP'] + config['ListGroupAllTag']['url_ListGroupAllTag']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('ListGroupAllTag_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "ListGroupAllTag Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("ListGroupAllTag Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n") 
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "ListGroupAllTag Result:" + colors.RESET, json.dumps(list, indent = 5), "\n")
                file = open('output.txt', 'a')
                file.write("ListGroupAllTag Result: ")
                file.write(json.dumps(list, indent = 5))
                file.write("\n")    
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1    
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "ListGroupAllTag Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ListGroupAllTag Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run List Group/All tags API!")
    
def UpdateGroupTag():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[24] == "Update Group tag (Sub-Group): 1\n"):
        try:
            url = config["info"]['IP'] + config['UpdateGroupTag']['url_UpdateGroupTag']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('UpdateGroupTag_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            
            response = requests.request("POST", url, headers=headers, data=payload)
            if (len(response.text) == 0):
                print(colors.OK + "UpdateGroupTag Result:" + colors.RESET, response.text)   
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("UpdateGroupTag Result: ")
                file.write(response.text)
                file.write("\n")  
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "UpdateGroupTag Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("UpdateGroupTag Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")  
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "UpdateGroupTag Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("UpdateGroupTag Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Update Group tag (Sub-Group) API!")
    
def DeleteGroupTag():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[25] == "Delete Group Tags: 1\n"):
        try:
            url = config["info"]['IP'] + config['DeleteGroupTag']['url_DeleteGroupTag']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('DeleteGroupTag_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            
            response = requests.request("POST", url, headers=headers, data=payload)
            if (len(response.text) == 0):
                print(colors.OK + "DeleteGroupTag Result:" + colors.RESET, response.text)   
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("DeleteGroupTag Result: ")
                file.write(response.text)
                file.write("\n") 
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "DeleteGroupTag Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("DeleteGroupTag Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")  
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "DeleteGroupTag Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("DeleteGroupTag Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Delete Group Tags API!")
    
def UpdateGroupMemberTag():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[26] == "Update Group Member's Tag (Sub-Group): 1\n"):
        try:
            url = config["info"]['IP'] + config['UpdateGroupMemberTag']['url_UpdateGroupMemberTag']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('UpdateGroupMemberTag_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            
            response = requests.request("POST", url, headers=headers, data=payload)
            if (len(response.text) == 0):
                print(colors.OK + "UpdateGroupMemberTag Result:" + colors.RESET, response.text)   
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("UpdateGroupMemberTag Result: ")
                file.write(response.text)
                file.write("\n") 
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "UpdateGroupMemberTag Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("UpdateGroupMemberTag Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n") 
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "UpdateGroupMemberTag Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("UpdateGroupMemberTag Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1 
    else:
        print("NO selection made to run Update Group Member's Tag (Sub-Group) API!")
    
def ListGroupMember():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[27] == "List Group Member: 1\n"):
        try:
            url = config["info"]['IP'] + config['ListGroupMember']['url_ListGroupMember']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('ListGroupMember_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            
            response = requests.request("POST", url, headers=headers, data=payload)
            null = "null"
            true = "true"
            false = "false"
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "ListGroupMember Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("ListGroupMember Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n") 
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "ListGroupMember Result:" + colors.RESET, json.dumps(list, indent = 5), "\n")   
                file = open('output.txt', 'a')
                file.write("ListGroupMember Result: ")
                file.write(json.dumps(list, indent = 5))
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1       
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "ListGroupMember Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ListGroupMember Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run List Group Member API!")
    
def ListGroupMemberTags():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[28] == "List Group Member's Tag: 1\n"):
        try:
            url = config["info"]['IP'] + config['ListGroupMemberTags']['url_ListGroupMemberTags']
            content_Type = config['info']['Content-Type_urlencoded'] 
            
            with open('ListGroupMemberTags_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            
            response = requests.request("POST", url, headers=headers, data=payload)
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "ListGroupMemberTags Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("ListGroupMemberTags Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "ListGroupMemberTags Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("ListGroupMemberTags Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "ListGroupMemberTags Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ListGroupMemberTags Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1 
    else:
        print("NO selection made to run List Group Member's Tag API!")
    
def QuerySetting():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[29] == "Query Setting: 1\n"):
        try:
            url = config["info"]['IP'] + config['QuerySetting']['url_QuerySetting']
            content_Type = config['info']['Content-Type_urlencoded']
                
            payload = {}
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            list = eval(response.text)
            if ("statusCode" in list):
                print(colors.FAIL + "QuerySetting Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("QuerySetting Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")
                global FAIL_COUNT
                FAIL_COUNT += 1  
            else:
                print(colors.OK + "QuerySetting Result:" + colors.RESET, json.dumps(list, indent = 2), "\n")
                file = open('output.txt', 'a')
                file.write("QuerySetting Result: ")
                file.write(json.dumps(list, indent = 2))
                file.write("\n")
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "QuerySetting Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("QuerySetting Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Query Setting API!")
        
def UpdatePerson():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()
    
    if (line[30] == "Update Person: 1\n"):
        try:
            global FAIL_COUNT
            global SUCCESS_COUNT
            
            url = config["info"]['IP'] + config['UpdatePerson']['url_UpdatePerson']
            headers = {
                'Authorization': token
            }
            with open('UpdatePerson_Params.yaml', 'rb') as paras: 
                conf = yaml.safe_load(paras)
                if 'coverImage' in conf and conf['coverImage']:
                    with open(conf['coverImage'], 'rb') as coverimg:
                        name_coverimg = os.path.basename(conf['coverImage'])
                        with open('UpdatePerson_Params.yaml', 'r') as y:
                            files = yaml.load(y, Loader = yaml.FullLoader)
                        files.update({
                            'coverImage': (name_coverimg, coverimg,'multipart/form-data')
                        })
                        response = requests.request("POST", url, headers=headers, files=files)
                else:
                    with open('UpdatePerson_Params.yaml', 'r') as y:
                        files = yaml.load(y, Loader = yaml.FullLoader)
                        response = requests.request("POST", url, headers=headers, files=files)
                    
                if (len(response.text) == 0):
                        print(colors.OK + "UpdatePerson Result:" + colors.RESET, response.text, "\n")
                        print("Please check the result on the Central console !!!", "\n")
                        file = open('output.txt', 'a')
                        file.write("UpdatePerson Result: ")
                        file.write(response.text)
                        file.write("\n")
                        SUCCESS_COUNT += 1  
                else:
                    list = eval(response.text)
                    print(colors.FAIL + "UpdatePerson Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                    file = open('output.txt', 'a')
                    file.write("UpdatePerson Result: ")
                    file.write(json.dumps(list, indent = 3))
                    file.write("\n")
                    FAIL_COUNT += 1  
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "UpdatePerson: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("UpdatePerson Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Update Person API!") 

def UpdateSnapshot():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()
    
    if (line[31] == "Update Snapshot: 1\n"):
        try:
            global FAIL_COUNT
            global SUCCESS_COUNT
            
            url = config["info"]['IP'] + config['UpdateSnapshot']['url_UpdateSnapshot']
            headers = {
                'Authorization': token
            }
            with open('UpdateSnapshot_Params.yaml', 'rb') as paras: 
                conf = yaml.safe_load(paras)
                with open(conf['snapshot'], 'rb') as img:
                    name_img = os.path.basename(conf['snapshot'])
                    with open('UpdateSnapshot_Params.yaml', 'r') as y:
                        files = yaml.load(y, Loader = yaml.FullLoader)
                    files.update({
                        'snapshot': (name_img, img,'multipart/form-data')
                    })
                    response = requests.request("POST", url, headers=headers, files=files)
                null = "null"
                list = eval(response.text)
                if ("statusCode" in list):
                    print(colors.FAIL + "UpdateSnapshot Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                    file = open('output.txt', 'a')
                    file.write("UpdateSnapshot Result: ")
                    file.write(json.dumps(list, indent = 3))
                    file.write("\n")
                    FAIL_COUNT += 1  
                else:
                    print(colors.OK + "UpdateSnapshot Result:" + colors.RESET, json.dumps(list, indent = 5), "\n")
                    file = open('output.txt', 'a')
                    file.write("UpdateSnapshot Result: ")
                    file.write(json.dumps(list, indent = 5))
                    file.write("\n")
                    SUCCESS_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "UpdateSnapshot: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("UpdateSnapshot Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1    
    else:
        print("NO selection made to run Update Snapshot API!")
        
def ChangeDatabase():
    line = []
    file = open('selection.txt', 'r')
    line = file.readlines()

    if (line[32] == "Change Database: 1\n"):
        try:
            url = config["info"]['IP'] + config['ChangeDatabase']['url_ChangeDatabase']
            content_Type = config['info']['Content-Type_urlencoded']  
            with open('ChangeDatabase_Params.yaml', 'r') as y:
                payload = yaml.load(y, Loader = yaml.FullLoader)
            headers = {
                'Content-Type': content_Type,
                'Authorization': token
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if (len(response.text) == 0):
                print(colors.OK + "ChangeDatabase Result:" + colors.RESET, response.text)   
                print("Please check the result on the Central console !!!", "\n")
                file = open('output.txt', 'a')
                file.write("ChangeDatabase Result: ")
                file.write(response.text)
                file.write("\n")  
                global SUCCESS_COUNT
                SUCCESS_COUNT += 1  
            else:
                list = eval(response.text)
                print(colors.FAIL + "ChangeDatabase Result:" + colors.RESET, json.dumps(list, indent = 3), "\n")
                file = open('output.txt', 'a')
                file.write("ChangeDatabase Result: ")
                file.write(json.dumps(list, indent = 3))
                file.write("\n")  
                global FAIL_COUNT
                FAIL_COUNT += 1 
        except Exception as e:
            traceback.print_exc()
            print(colors.FAIL + "ChangeDatabase Result: " + colors.RESET, repr(e), "\n")
            file = open('output.txt', 'a')
            file.write("ChangeDatabase Result: ")
            file.write(repr(e))
            file.write("\n")
            FAIL_COUNT += 1  
    else:
        print("NO selection made to run Change Database API!")

if __name__ == "__main__": 
    clean()
    create_APIs()
    Authentication()   
    ImportPerson()
    UpdatePersonInfoV2()
    AddPersonFace()
    DeletePerson()
    DeletePersonFace()
    DataPurgeForHistoryRecord()
    QueryPerson()
    ImageQualityCheck()
    ListWorkstationListandCamera()
    QueryHistoryRecord()
    CentralHealthCheck()
    WorkstationHealthCheck()
    CameraHealthCheck()
    SearchFace()
    ActivateCamera()
    ListCamera()
    CreateGroup()
    UpdateGroup()
    DeleteGroup()
    ListGroup()
    MoveGroupMember()
    CreateGroupTag()
    ListGroupAllTag()
    UpdateGroupTag()
    DeleteGroupTag()
    UpdateGroupMemberTag()
    ListGroupMember()
    ListGroupMemberTags()
    QuerySetting()
    UpdatePerson()
    UpdateSnapshot()
    ChangeDatabase()
    
    print(colors.WARNING + "Success: " + colors.RESET, SUCCESS_COUNT)
    print(colors.WARNING + "Fail: " + colors.RESET, FAIL_COUNT)
    
    os.system("Pause")



