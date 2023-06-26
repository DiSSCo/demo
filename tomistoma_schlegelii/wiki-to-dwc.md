
This is a demo to showcase how to use the Wikidata biodiversity knowledge graph and map the elements to an existing data standard (such as Darwin Core). The idea is to explore how these graphs fit into the Digital Extended Specimen concept and DiSSCo Digital Specimen implementation. 

Note: some of the relatioship items described in wikidata cannot be yet mapped or described in Darwin Core model. 

### wikidata graph 

The wikidata graph was produced by two students (Ijsbrand Wilts and Jop Bakker) who as part of their B.Sc thesis worked with *Tomistoma Schlegelii* specimens at Naturalis. 

The graph in Wikidata can be found [here](https://w.wiki/6hBD)

A snippet of one of the elements in the graph: 

```javascript
{'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q118141589'}, 
'item2': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q24894921'}, 
'image': {'type': 'uri', 'value': 'http://commons.wikimedia.org/wiki/Special:FilePath/Map%20of%20southern%20Borneo.jpg'}, 
'item1Label': {'xml:lang': 'en', 'type': 'literal', 'value': 'map of southern Borneo'}, 
'item2Label': {'xml:lang': 'en', 'type': 'literal', 'value': 'Sungai Karau'}, 
'edgeLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'depicts'}

```

### code and example files 
- [tomistoma.json](tomistoma.json) is a JSON download of the wikidata graph
- [wiki_6hBD.py](wiki_6hBD.py) is a python code to create the graph (provided by Wikidata)
- [wiki-to-dwc.py](wiki-to-dwc.py) is a sample python script to showcase possible mapping
  
### map to darwin core 

The test python script looks at a json file and produces dwc mapping. 

```javascript
{'occurrenceID': 'http://www.wikidata.org/entity/Q118141589',
'scientificName': 'map of southern Borneo',
 'associatedMedia': 'http://commons.wikimedia.org/wiki/Special:FilePath/Map%20of%20southern%20Borneo.jpg',
'recordedBy': 'Salomon Müller', 'relationship': 'creator'}
```
A specimen item in the Wikidata graph looks like this: 

```javascript
{
"item1":"http://www.wikidata.org/entity/Q118129970",
"image":"http://commons.wikimedia.org/wiki/Special:FilePath/Naturalis%20Biodiversity%20Center-RMNH.RENA.35445%2020-Tomistoma%20schlegelii.jpg",
"item1Label":"RMNH.RENA.35445"}
```
As there is no scientificName in the wikidata item, at first pass we can create something like the following mapping, then replace the  RMNH.RENA.35445 with the name. 
The item 'discoverer or inventor' is wikidata property https://www.wikidata.org/wiki/Property:P61. This is not the correct term. We need to find the equivalent like collectedBy or recordedBy in the mapping process.  

```javascript 
{'occurrenceID': 'http://www.wikidata.org/entity/Q118129970',
'scientificName': 'RMNH.RENA.35445',
'associatedMedia': 'http://commons.wikimedia.org/wiki/Special:FilePath/Naturalis%20Biodiversity%20Center-RMNH.RENA.35445%2020-Tomistoma%20schlegelii.jpg',
'recordedBy': 'Salomon Müller', 
  'relationship': 'discoverer or inventor'}
```


### Acknowledgements 
- Ijsbrand Wilts 
- Jop Bakker
- Niels Raes 
- Andreas Weber 
- Annika Hendriksen
