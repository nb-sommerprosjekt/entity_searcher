#!/usr/bin/python3
import os
import sys
import argparse
sys.path.append("/home/tensor")
from pythonlibs import xmlHandler
import time
import json
start = time.time()

parser = argparse.ArgumentParser(description = "search queries etc")
parser.add_argument("-sq","--search_queries",dest = "search_queries", type =str, nargs = '+')
#parser.add_argument("-s", "--source", dest="source")
args = parser.parse_args()



search_queries = [x.lower() for x in args.search_queries]


#open pickle containing all a list of dictionaries that are of the form [{"entity": "filename", "entity2": "filename"....},
# {"entity":"filename2", "entity2" : "filename2"....}...]
with open("indexes.json", "rb") as file:
    entity_xml_dict = json.load(file)
 
# Performing string matching and printing of result,
result_xml = []
for entity_dict in entity_xml_dict:
    if all(query in entity_dict for query in search_queries):
       result_xml.append(entity_dict[search_queries[0]])
   

search_time = time.time() - start
print(str(search_queries)+ " was found in " +str(len(result_xml))+" documents")
#print(str(result_xml)) 
print("search time: {}".format(search_time))




