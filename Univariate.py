
import numpy as np
import pandas as pd
class Univariate:
    def QuanQual(dataset):
        quan=[]
        qual=[]
        for column in dataset.columns:
            if(dataset[column].dtype =='O'):
                qual.append(column)
            else:
                quan.append(column)
        return quan, qual
    def percentile(dataset, quan ):
        descriptive = pd.DataFrame(index=["Mean","Median","Mode","01:25%","Q2:50%","Q3:75%","99%","Q4:100%"], columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"] = dataset[columnName].mean()
            descriptive[columnName]["Median"] = dataset[columnName].median()
            descriptive[columnName]["Mode"] = dataset[columnName].mode()[0]
            descriptive[columnName]["01:25%"] = dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"] = dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"] =dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"] =np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"] = dataset.describe()[columnName]["max"]
        return descriptive
    def central_tendency(dataset, quan):
        descriptive = pd.DataFrame(index=["Mean","Median","Mode"], columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]= dataset[columnName].mean()
            descriptive[columnName]["Median"]= dataset[columnName].median()
            descriptive[columnName]["Mode"]= dataset[columnName].mode()[0]
        return descriptive
    def iqr(dataset, quan):
        descriptive = pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","Min","Lesser",
                                          "Max","Greater"],columns =quan)
        for columName in quan:
            descriptive[columName]["Mean"] = dataset[columName].mean()
            descriptive[columName]["Median"] = dataset[columName].median()
            descriptive[columName]["Mode"] = dataset[columName].mode()[0]
            descriptive[columName]["Q1:25%"] = dataset.describe()[columName]["25%"]
            descriptive[columName]["Q2:50%"] = dataset.describe()[columName]["50%"]
            descriptive[columName]["Q3:75%"] =dataset.describe()[columName]["75%"]
            descriptive[columName]["99%"] =np.percentile(dataset[columName],99)
            descriptive[columName]["Q4:100%"] = dataset.describe()[columName]["max"]
            descriptive[columName]["IQR"] = descriptive[columName]["Q3:75%"]  - descriptive[columName]["Q1:25%"]
            descriptive[columName]["Min"] =  dataset[columName].min()
            descriptive[columName]["Lesser"] =  descriptive[columName]["Q1:25%"] - 1.5 * descriptive[columName]["IQR"]
            descriptive[columName]["Max"] =  dataset[columName].max()
            descriptive[columName]["Greater"] =  descriptive[columName]["Q3:75%"] + 1.5 * descriptive[columName]["IQR"]
        return descriptive
    def hsk(dataset, quan):
        descriptive = pd.DataFrame(index=["skew","kurtosis"],columns =quan)
        for columName in quan:
            descriptive[columName]["skew"] =  dataset[columName].skew()
            descriptive[columName]["kurtosis"] =   dataset[columName].kurtosis()
        return descriptive 

    def lesserAndGreater(descriptive, quan):
        lesser =[]
        greater =[]
        for columName in quan:  
            if(descriptive[columName]["Min"] <  descriptive[columName]["Lesser"]):
                lesser.append(columName)
            if(descriptive[columName]["Max"] >  descriptive[columName]["Greater"]):
                greater.append(columName)
        return lesser,greater
    def applyRanges(dataset, descriptive, lesser, greater):
        for columName in lesser:
            dataset[columName][dataset[columName]<descriptive[columName]["Lesser"]]=descriptive[columName]["Lesser"]
        for columName in greater:
            dataset[columName][dataset[columName]>descriptive[columName]["Greater"]]=descriptive[columName]["Greater"]
        return dataset
    def frequency(dataset):
        freqTable = pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","Cumsum"])
        freqTable["Unique_Values"] = dataset["bedrooms"].value_counts().index
        freqTable["Frequency"]  = dataset["bedrooms"].value_counts().values
        print(len(pd.DataFrame(dataset)))
        freqTable["Relative_Frequency"]  = freqTable["Frequency"]/len(pd.DataFrame(dataset))
        freqTable["Cumsum"]  = freqTable["Relative_Frequency"].cumsum()
        return freqTable;