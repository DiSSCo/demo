# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

query = """#defaultView:Graph
SELECT ?item1 ?image ?item1Label ?item2 ?image2 ?item2Label ?edgeLabel WHERE {
VALUES ?item1 {wd:Q118141589 wd:Q118129770 wd:Q118129970 wd:Q118130119 wd:Q118234416 wd:Q118288047 wd:Q118130150 wd:Q641676 wd:Q24894921 wd:Q118288029 wd:Q118130081 wd:Q61390 wd:Q242464}
VALUES ?item2 {wd:Q118141589 wd:Q118129770 wd:Q118129970 wd:Q118130119 wd:Q118234416 wd:Q118288047 wd:Q118130150 wd:Q641676 wd:Q24894921 wd:Q118288029 wd:Q118130081 wd:Q61390 wd:Q242464}
?item1 ?prop ?item2.
MINUS { ?item1 wdt:P2652 ?item2 }
?edge ?dummy ?prop ; rdf:type wikibase:Property
OPTIONAL {?item1 wdt:P18 ?image}
OPTIONAL {?item2 wdt:P18 ?image2}
SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}"""


def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)
