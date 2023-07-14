import pandas as pd

folder = "./MachineLearningRepository_Adult-dataset/data/"
X_train = pd.read_csv(folder+'adult.csv')
X_train_test = pd.read_csv(folder+'adult.test')
# Dropping the first row
df_test = X_train_test.drop([0]) # Contains |1x3 Cross validator

# Getting the non-numerical columns
   # Data types present in the dataset
print(X_train.dtypes.unique()) # [dtype('float64') dtype('O') dtype('int64')]
   # Columns with the data type 'object'
object_type_mask = (X_train.dtypes == 'object')  
object_type_columns = X_train.columns[object_type_mask].tolist()
print(object_type_columns)


