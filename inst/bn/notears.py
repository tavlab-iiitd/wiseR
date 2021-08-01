import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import resample
from causalnex.structure.notears import from_pandas
import os
import warnings
warnings.filterwarnings("ignore")
from causalnex.structure import StructureModel
from IPython.display import Image
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE



def noTears(data, bootstraps):
	struct_data =data
	edge_list = []
	sm = StructureModel()
	for i in range(0, bootstraps):
		boot = resample(struct_data, replace=True, n_samples=len(struct_data))
		sm  = from_pandas(boot)
		#sm.remove_edges_below_threshold(0.3)
		edge_list.extend((list(sm.edges)))
	freq = {}
	for item in edge_list:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1

	edgeL = []		
	for item in freq:
		if freq[item] > bootstraps // 2:
			edgeL.append(item)
	
	edgeL.insert(0,["from","to"])			
	pd.DataFrame(edgeL).to_csv("gnn.csv",index=False,header=False)
	print(edgeL)