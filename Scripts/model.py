from sklearn.model_selection import train_test_split, cross_val_score, RepeatedStratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, recall_score, classification_report

class Model():
    def __init__(self) -> None:
            model = None
            metric = None
            target = None
    
    def __str__(self) -> str:
          return 'Current Model={0}, on target {1}, using metric {2}'.format(self.model, self.target, self.metric)

    def run_testing(self.model, X_train, y_train, X_test, y_test):
        print('Model={0}'.format(self.model))
        sample_fit = self.model.fit(X_train, y_train)
        sample_predict = self.model.predict(X_test)
        print("\n----------------Classification Report------------------------------------")
        print(classification_report(y_test,sample_predict))
        print('---------------------------------------------------------------------------\n')

        

    