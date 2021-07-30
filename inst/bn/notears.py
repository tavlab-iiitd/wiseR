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



dir = "./resutls_new_sachs_/"
if not os.path.exists(dir):
	os.makedirs(dir)



def noTears(data, bootstraps):
	struct_data =data
	edge_list = []
	sm = StructureModel()
	for i in range(0, bootstraps):
		boot = resample(struct_data, replace=True, n_samples=len(struct_data))
		sm  = from_pandas(boot)
		sm.remove_edges_below_threshold(0.3)
		edge_list.extend((list(sm.edges)))
		print("Edges:", sm.edges)
		df = pd.DataFrame(list(sm.edges))
		df.columns = ['from', 'to']
		df.to_csv(dir + "edgelist_notears" + str(i+1) + ".csv", index = False )
		df = pd.DataFrame()
	print(edge_list)
	print(type(edge_list))
	print(" ")
	
	freq = {}
	for item in edge_list:
		print(type(item))
		print(item)
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1

	print(freq)
	print(len(freq))
	edgeL = []		
	for item in freq:
		if freq[item] > 16:
			edgeL.append(item)
			
			
	pd.DataFrame(edgeL).to_csv("Final_Notears_Edgelist.csv", index = False)
