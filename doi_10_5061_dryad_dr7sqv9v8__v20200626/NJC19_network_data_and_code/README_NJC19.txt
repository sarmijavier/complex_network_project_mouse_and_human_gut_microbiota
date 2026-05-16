"NJC19_network.json" includes the network information of NJC19, charaacterized by a list of metabolic activities between organisms and chemical compounds (detailed information on organisms, compounds, and references for each metabolic activity is included in other files, as will be explained below).
Each name of metabolic activities is given by a number followed by "NJC19_".
Each metabolic activity is described using the following properties:
- "Species": Data type of this property is a string. The name of the organism node is given for the metabolic activity.
- "Small-molecule metabolite or macromolecule": Data type of this property is a string. The name of chemical compound node is given for the metabolic activity.
- "Metabolic activity": Data type of this property is a string. The type of the metabolic activity is given in this property. The types of the metabolic activity are as follows: "Consumption (import)", "Production (export)", "Consumption (import), Production (export)", "Macromolecule degradation", "Consumption (import) (-)", "Production (export) (-)", and "Macromolecule degradation (-)". Here, (-) denotes `negative' information from the literature, i.e. the corresponding activity does not occur, according to the literature. 
- "Ref. #": Data type of this property is a list of the indices (numbers) of references supporting the metabolic activity (detailed reference information for each reference number is shown in another file "NJC19_reference.json", as will be described below). Some reference numbers are followed by (G), and this (G) indicates that the metabolic activity is based on genus-level information from the reference. If metabolic activity is "Consumption (import), Production (export)", there are two lists of the reference numbers. One is for the references supporting "Consumption (import)" and the other for the references supporting "Production (export)".



- "Metabolic activity": Data type of this property is a string. 
The type of the metabolic activity is given in this property. 
The types of the metabolic activity are as follows: 
"Consumption (import)", 
"Production (export)", 
"Consumption (import), Production (export)", 
"Macromolecule degradation", 
"Consumption (import) (-)", 
"Production (export) (-)", 
and "Macromolecule degradation (-)". 

Here, (-) denotes `negative' information from the literature, i.e. the corresponding activity does not occur, according to the literature. 



"NJC19_organism.json" includes a list of organism nodes in NJC19.
Each organism node is described using the following properties:
- "name": Data type of this property is a string. The currently used name of the organism is given.
- "type": Data type of this property is a string. The type of the organism node is given in this property. In NJC19, there are two types of organism nodes, microbial species and host cell.
- "NCBI Taxonomy ID": Data type of this property is a string. This property is given when the type of the organism node is microbial species. NCBI Taxonomy ID of the microbial species is given from this source: https://www.ncbi.nlm.nih.gov/taxonomy.
- "domain": Data type of this property is a string. This property is given when the type of the organism node is microbial species. Domain of the microbial species is given.
- "phylum": Data type of this property is a string. This property is given when the type of the organism node is microbial species. Phylum of the microbial species is given.
- "synonym": Data type of this property is a list of synonyms of the microbial species. A list of synonyms corresponding to the microbial species is given.
- "source(s) for microbial species identification": Data type of this property is an object. This object contains a list of data or literature sources for the microbial species identified for NJC19 construction. Each source of the microbial species is described using the following properties:
    - "source type": Data type of this property is a string. There are three types of "source type": "shotgun metagenome sequence data", "16S rRNA gene sequence data", and "literature".
    - "DOI": Data type of this property is a DOI link.
    - "mouse strains": Data type of this property is a string. This property is given, if "source type" is "shotgun metagenome sequence data" or "16S rRNA gene sequence data". Mouse strains used in the study are given.
    - "sample source": Data type of this property is a string. This property is given, if "source type" is "shotgun metagenome sequence data" or "16S rRNA gene sequence data". A sample source of the sequence data is given as stool or cecum.
    - "number of samples": Data type of this property is a number. This property is given, if "source type" is "shotgun metagenome sequence data" or "16S rRNA gene sequence data". The number of samples is given.
    - "sample accession": Data type of this property is a string. This property is given, if "source type" is "shotgun metagenome sequence data" or "16S rRNA gene sequence data". The accession number of the sequence data is given. The accession numbers are not available for "Wang et al. (2014)" and "Benson et al. (2010) (16S)".
    - "link of sample accession": Data type of this property is a website link of the sequence data. This property is given, if "source type" is "shotgun metagenome sequence data" or "16S rRNA gene sequence data".


"NJC19_compound.json" includes a list of chemical compound nodes in NJC19.
Each chemical compound node is described using the following properties:
- "type": Data type of this property is a string. The type of the chemical compound node given in this property is either small molecule or macromolecule.
- "name": Data type of this property is a list of chemical compound names. The list of chemical compounds corresponding to the chemical compound node is given.
- "KEGG compound identifier": Data type of this property is a list of KEGG compound identifiers. A list of KEGG compound identifiers corresponding to the elements in "name" is given from this source: https://www.genome.jp/kegg/compound.
- "degradation": Data type of this property is an object. This property is given when the type of the chemical compound node is macromolecule. This object has two properties, "degradation product(s)" and "remark".
    - "degradation product(s)": Data type of this property is a list of degradation products of the macromolecule.
    - "remark" : Data type of this property is a string. A note on the degradation product(s) of a macromolecule is given, if necessary.


"NJC19_reference.json" includes a list of references used for NJC19 construction.
Each name of references is given by a number followed by "Ref #.".
Each reference is described using the following properties:
- "First author": Data type of this property is a string. The first author of the reference is given.
- "Year": Data type of this property is a number. The year of the publication of the reference is given.
- "Title": Data type of this property is a string. The title of the reference is given.