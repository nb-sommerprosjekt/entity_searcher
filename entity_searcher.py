
import os
import sys
import argparse
sys.path.append("/home/tensor")
from pythonlibs import xmlHandler
from pythonlibs.entity_recog import entity_recognizer
import time
import json
start = time.time()


class search_engine():
    indexPath = None
    indexes = None
    search_queries = None
    result_file_paths = []
    entitiesAndType = []
    search_queries = []
    def __init__(self, pathToIndexFile):
        self.indexPath = pathToIndexFile
        self.load_indexes(pathToIndexFile)
    def load_indexes(self, indexPath):
        #open json containing all a list of dictionaries that are of the form [{"entity$
        # {"entity":"filename2", "entity2" : "filename2"....}...]
        with open(self.indexPath, "r") as file:
            self.indexes = json.load(file)
    def search(self, search_queries):
        #self.search_queries = [x.lower() for x in search_queries]
        #self.result_file_paths =[]
        self.analyzeSearchPhrase(search_queries)
        for entity_dict in self.indexes:
            if all(query in entity_dict for query in self.search_queries):
                self.result_file_paths.append(entity_dict[self.search_queries[0]])
    
    def analyzeSearchPhrase(self, search_phraze):
        analyzer = entity_recognizer()
        analyzer.extractEntities(text = ' '.join(search_phraze))
        analyzer.formatEntities()
        self.entitiesAndType = analyzer.prettyEntities
        
        for entity_tuple in self.entitiesAndType:
            self.search_queries.append(entity_tuple[1])
        self.search_queries = [x.lower() for x in self.search_queries]
    def printPrettyResult(self, withPaths = False):
        
        print(str(self.search_queries)+ " was found in " +str(len(self.result_file_paths))+" documents")                    
        if withPaths:
            print("De ble funnet i folgende filer: +\n\n")
            print(self.result_file_paths)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "search queries etc")
    parser.add_argument("-sq","--search_queries",dest = "search_queries", type =str, nargs = '+')
    #parser.add_argument("-s", "--source", dest="source")
    args = parser.parse_args()
    
    search_ent = search_engine("indexes.json")
    search_ent.search(args.search_queries)
    search_ent.printPrettyResult(withPaths=False)
