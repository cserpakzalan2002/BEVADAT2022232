import pandas as pd
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import math


csv_path="diabetes.csv"

class KNNClassifier:

    #Constructor
    def __init__(self,k:int,test_split_ratio:float):
        self.k = k
        self.test_split_ratio = test_split_ratio
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.y_preds = None

    #Property
    @property
    def k_neighbors(self):
        return self.k

    #Load data, clean
    @staticmethod
    def load_csv(csv_path:str) ->Tuple[pd.DataFrame,pd.Series]:
        df = pd.read_csv(csv_path)
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)
        x, y = df.iloc[:,:-1], df.iloc[:, -1]
        return x, y

    #Train test split try optim
    def train_test_split(self,features:pd.DataFrame,labels:pd.Series)-> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, 'Size mismatch!'

        self.x_train = features.iloc[:train_size,:]
        self.y_train = labels.iloc[:train_size]

        self.x_test = features.iloc[train_size:train_size+test_size,:]
        self.y_test = labels.iloc[train_size:train_size + test_size]


    def euclidean(self,element_of_x:pd.DataFrame) -> pd.DataFrame:
        return math.sqrt(pd.DataFrame.sum((self.x_train - element_of_x)**2,axis=1))
    

    def predict(self, x_test:pd.DataFrame) ->pd.DataFrame:
        labels_pred=[]
        for x_test_element in x_test:
            distances = self.euclidean(self.x_train,x_test_element)
            distances = pd.DataFrame(sorted(zip(distances,self.y_train)))
            label_pred = mode(distances[:self.k,1],keepdims=False).mode
            labels_pred.append(label_pred)
        self.y_preds = pd.DataFrame.array(labels_pred,dtype=pd.Int32Dtype)
        return self.y_preds
    
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def plot_confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        return conf_matrix

