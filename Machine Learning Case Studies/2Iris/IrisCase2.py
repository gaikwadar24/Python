from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousKNeighborsClassifier():
    Dataset = load_iris()   #1 : Load Data
    Data = Dataset.data
    Target = Dataset.target


    #2 : Manipulate the Data
    Data_train , Data_test , Target_train , Target_test = train_test_split(Data , Target , test_size=0.5)


    Classifier = KNeighborsClassifier()
    
    #3 : Build Model
    Classifier.fit(Data_train , Target_train)

    #4 : Test Model
    Predictions = Classifier.predict(Data_test)


    Accuracy = accuracy_score(Target_test, Predictions)

    #5 : Improve -- Missing
    return Accuracy
def main():
    Ret = MarvellousKNeighborsClassifier()

    print("Accuracy of Iris Dataset with KNN is ",Ret*100)


if __name__ == "__main__":
    main()