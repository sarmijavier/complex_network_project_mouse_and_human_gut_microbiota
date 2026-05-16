# -*- coding: utf-8 -*-
"""
Created on 3 November 2019

Convert NJC19_network.json to excel file

File: NJC19_network.json

@author: LIM Roktaek
"""

####-- Modules

import os
import sys
import numpy
import pandas
import json

####-- END Modules

###
def error_exit():
    checker = input('Enter "x" to finish this program: ')
    if checker == 'x':
        sys.exit()
    #
    return
###

####-- Main script

NJC19File = 'NJC19_network.json'
#-- Read NJC19
with open(NJC19File) as json_file:
    NJC19 = json.load(json_file)
#
organism = []
compound = []
activity = []
references = []
for idx in NJC19.keys():
    organism.append(NJC19[idx]['Species'])
    compound.append(NJC19[idx]['Small-molecule metabolite or macromolecule'])
    activity.append(NJC19[idx]['Metabolic activity'])
    if NJC19[idx]['Metabolic activity'] == 'Consumption (import), Production (export)':
        ref_dict = NJC19[idx]['Ref. #']
        ref_import = ref_dict['Consumption (import)']
        ref_import_str = 'import:' + ', '.join(ref_import)
        ref_export = ref_dict['Production (export)']
        ref_export_str = 'export:' + ', '.join(ref_export)
        references.append(ref_import_str + ';' + ref_export_str)
    else:
        refs = NJC19[idx]['Ref. #']
        references.append(', '.join(refs))
    #
#

df = pandas.DataFrame({ 'Species'                                    : organism,
                        'Small-molecule metabolite or macromolecule' : compound,
                        'Metabolic activity'                         : activity,
                        'Ref. #'                                     : references })
df.to_excel('NJC19_network.xlsx',index=False)

####-- END ---####
