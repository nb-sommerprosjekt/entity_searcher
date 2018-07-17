import sys
sys.path.append("/home/tensor")
from pythonlibs.entity_recog import entity_recognizer

analyzer = entity_recognizer()
analyzer.extractEntities(text= "Jeg heter Jens Stoltenberg og bor i Oslo")
analyzer.formatEntities()
for entity in analyzer.prettyEntities:
    print(entity[1])

#print(analyzer.prettyEntities)
