import json


def transform_to_darwin_core(data):
    darwin_core_data = []
    
    for item in data:
        darwin_core_item = {}
        
        if 'item1' in item:
            darwin_core_item['occurrenceID'] = item['item1']
        
        if 'item1Label' in item:
            darwin_core_item['scientificName'] = item['item1Label']
        
        if 'image' in item:
            darwin_core_item['associatedMedia'] = item['image']
        
        if 'item2' in item:
            darwin_core_item['recordedBy'] = item['item2']
        
        if 'item2Label' in item:
            darwin_core_item['recordedBy'] = item['item2Label']
        
        if 'edgeLabel' in item:
            darwin_core_item['relationship'] = item['edgeLabel']
        
        darwin_core_data.append(darwin_core_item)
    
    return darwin_core_data

# Example usage
#json_data = '[{"item1":"http://www.wikidata.org/entity/Q118129770","image":"http://commons.wikimedia.org/wiki/Special:FilePath/Naturalis%20Biodiversity%20Center-RMNH.RENA.35444%204-Tomistoma%20schlegelii.jpg","item1Label":"RMNH.RENA.35444","item2":"http://www.wikidata.org/entity/Q61390","item2Label":"Salomon Müller","edgeLabel":"discoverer or inventor"},{"item1":"http://www.wikidata.org/entity/Q118129970","image":"http://commons.wikimedia.org/wiki/Special:FilePath/Naturalis%20Biodiversity%20Center-RMNH.RENA.35445%2020-Tomistoma%20schlegelii.jpg","item1Label":"RMNH.RENA.35445","item2":"http://www.wikidata.org/entity/Q61390","item2Label":"Salomon Müller","edgeLabel":"discoverer or inventor"}]'

with open('tomistoma.json') as user_file:
  file_contents = user_file.read()

data = json.loads(file_contents)

darwin_core_data = transform_to_darwin_core(data)

# Print the transformed data
for item in darwin_core_data:
    print(item)

