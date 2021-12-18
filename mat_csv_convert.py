import scipy.io
import numpy as np

filename = input("filename> ")

data = scipy.io.loadmat(filename)

outputname = filename[0:-4] + ".csv"

for i in data:
    if '_' not in i and 'readme' not in i:
        np.savetxt((outputname), data[i], delimiter = ',')
        
print(f"converted mat file {filename} to csv file {outputname}")
