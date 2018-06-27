#!/usr/bin/python3
import os
import sys
import argparse
sys.path.append("/home/tensor")
from pythonlibs import xmlHandler
import time
start = time.time()
parser = argparse.ArgumentParser(description = "search queries etc")
parser.add_argument("-sq","--search_queries",dest = "search_queries", type =str, nargs = '+')
#parser.add_argument("-s", "--source", dest="source")
args = parser.parse_args()
parse_time = time.time() - start
print("parse_time: {}".format(parse_time))

search_queries = [x.lower() for x in args.search_queries]
print(search_queries)
#search_query = sys.argv[1]

 
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
for file in xml_file_paths:
    start4 = time.time()
    handler = xmlHandler.xmlHandler(inputXmlFile = file, rootNodeName = "entities")
    timer_xmlparse += time.time() - start4

    start5 = time.time()
    res = handler.findAllNodes("entity")
    entities = []
    for node in res:
       entities.append(node.text.lower())
    timer_extract_entities +=time.time()-start5
    
    start6 = time.time()
    if set(search_queries).issubset(entities):
       result_xml.append(file)
    timer_stringMatch = time.time()-start6
find_search_results_time = time.time() - start3

print(str(search_queries)+ " was found in " +str(len(set(result_xml)))+" documents")
#print(str(result_xml)) 
print("search time: {}".format(find_search_results_time))
print("xml_parse_time: {}".format(timer_xmlparse))
print("extract entities time: {}".format(timer_extract_entities))
print("string match time: {}".format(timer_stringMatch))



