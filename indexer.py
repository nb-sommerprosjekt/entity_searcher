#!/usr/bin/python3
import os
import sys
import argparse
sys.path.append("/home/tensor")
from pythonlibs import xmlHandler
import time
import pickle

 
entity_folder_paths = []
with open("data_sources.txt", "r") as f:
   for line in f:
      entity_folder_paths.append(line.strip())

start2 = time.time()
#Extracting all files in subfolders
xml_file_paths = []
for folder_path in entity_folder_paths:
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            xml_file_paths.append(os.path.join(path,name))
result_xml = []
travers_time = time.time()-start2
print("travers_time: {}".format(travers_time))

start3 = time.time()
timer_xmlparse = 0
timer_extract_entities = 0
timer_stringMatch = 0
entity_dict_collection = []
for file in xml_file_paths:
    start4 = time.time()
    handler = xmlHandler.xmlHandler(inputXmlFile = file, rootNodeName = "entities")
    timer_xmlparse += time.time() - start4

    start5 = time.time()
    res = handler.findAllNodes("entity")
    entities = {}
    for node in res:
       entities[node.text.lower()] = file
    entity_dict_collection.append(entities)
    timer_extract_entities +=time.time()-start5
    
with open("indexes.pickle","wb") as pckl:
    pickle.dump(entity_dict_collection, pckl)


