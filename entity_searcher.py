#!/usr/bin/python3
import os
import sys
import argparse
sys.path.append("/home/tensor")
from pythonlibs import xmlHandler

parser = argparse.ArgumentParser(description = "search queries etc")
parser.add_argument("-sq","--search_queries",dest = "search_queries", type =str, nargs = '+')
#parser.add_argument("-s", "--source", dest="source")
args = parser.parse_args()

print("search_queries {}".format(
args.search_queries 
))

search_queries = [x.lower() for x in args.search_queries]
print(search_queries)
#search_query = sys.argv[1]

 
entity_folder_paths = ["/disk1/Metastore/Radio/P1/2011/01/ENT",
"/disk1/Metastore/Radio/P1/2011/02/ENT",
"/disk1/Metastore/Radio/P1/2011/03/ENT",
"/disk1/Metastore/Tv/NRK1/2011/01/ENT",
"/disk1/Metastore/Tv/NRK1/2011/02/ENT",
"/disk1/aw_experiments/entity_recognized/avis_entities"]

#Extracting all files in subfolders
xml_file_paths = []
for folder_path in entity_folder_paths:
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            xml_file_paths.append(os.path.join(path,name))
result_xml = []
for file in xml_file_paths:
    handler = xmlHandler.xmlHandler(inputXmlFile = file, rootNodeName = "entities")
    res = handler.findAllNodes("entity")
    entities = []
    for node in res:
       entities.append(node.text.lower())
    if set(search_queries).issubset(entities):
       result_xml.append(file)
print(str(search_queries)+ " was found in " +str(len(result_xml))+" documents")
print(str(result_xml)) 