import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#Generating synthetic dataset
np.random.seed(42)
x=np.random.rand(1000, 5) 
y=np.random.randint(0, 2, 1000)

#Splitting the dataset into training (80%) and testing (20%) sets
x_train, x_test, y_train,y_test= train_test_split(x, y, test_size=0.2, random_state=42)
#Standardizing the feature values 
scaler=StandardScaler()
x_train= scaler.fit_transform(x_train)
x_test= scaler.transform(x_test)

#Training logistic regeression model
model= LogisticRegression()
model.fit(x_train, y_train)

#Making predictions
y_pred= model.predict(x_test)

#Calculae evaluation metrics
accuracy= accuracy_score(y_test, y_pred)
precision= precision_score(y_test, y_pred)
recall=recall_score(y_test, y_pred)
f1=f1_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1-Score: {f1:.2f}')