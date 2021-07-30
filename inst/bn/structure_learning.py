from file import *
from notears import *
from sklearn.preprocessing import LabelEncoder
import numpy as np
import argparse


def StructureLearning(data_path, method, bootstraps):
	#data = pd.read_csv(data_path)
	data = data_path
	non_numeric_columns = list(data.select_dtypes(exclude=[np.number]).columns)
	if non_numeric_columns:
		le = LabelEncoder()
		for col in non_numeric_columns:
			struct_data[col] = le.fit_transform(data[col])
	if method == "DAG_GNN":
		DAG_GNN(data, int(bootstraps))
	elif method == "NoTears":
		noTears(data, int(bootstraps))




# if __name__ == "__main__":
# 	ap = argparse.ArgumentParser()
# 	ap.add_argument("-d", "--dataset", required=True)
# 	ap.add_argument("-i", "--iterations", required = True)
# 	ap.add_argument("-m", "--method", required = True)
# 	args = vars(ap.parse_args())
# 	StructureLearning(args["dataset"],args["method"],args["iterations"])
