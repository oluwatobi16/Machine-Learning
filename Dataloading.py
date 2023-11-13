from sklearn.datasets import load_wine
dataset=load_wine()
X,y = dataset.data, dataset.target
print(X)
