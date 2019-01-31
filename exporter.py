'''
this  python script simply exports the RGB tables for the collor scemes to plaintext files provided in the data/ subfolder. If a colorsceme data file already exists then this code does not need to be run. Aslo this code can be easily extended to create data files for more matplotlib color scemes.
'''

import palettable.matplotlib as pmlb
import palettable.colorbrewer as pcb

import numpy as np
scheme_names = ['Magma_20','Viridis_20']

for scheme_name in scheme_names:
    scheme_data = getattr(pmlb,scheme_name).colors
    np.savetxt(f'data/matplotlib/{scheme_name}',scheme_data)

sequential_palette_names = ['Blues_9','Reds_9', 'Greens_9', 'Oranges_9', 'Greys_9',  'Purples_9']
for  seq_palette_name in sequential_palette_names:
    seq_palette_data =  getattr(pcb.sequential, seq_palette_name).colors
    np.savetxt(f'data/colorbrewer/sequential/{seq_palette_name}', seq_palette_data)

