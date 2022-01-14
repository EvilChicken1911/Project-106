import csv
import numpy as np

def getdatasource(datapath):
    marks = []
    dayspresent = []
    with open(datapath) as f:
        reader = csv.DictReader(f)

        for row in reader:
            marks.append(float(row["Marks In Percentage"]))
            dayspresent.append(float(row["Days Present"]))
    
    return {
        "x": marks,
        "y": dayspresent
    }

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation", correlation[0,1])

def main():
    datapath = "C:/Users/Jonathan Wu/Downloads/White Hat/Class106/Student Marks vs Days Present.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

main()