from sklearn.svm import SVC
svm = SVC()
svm.fit([[0,0,],[1,0],[1,1],[0,1]], [1,1,2,2])
#SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, 
#  degree=3, gamma=0.5,
#  kernel='rbf', probability=False, shrinking=True, tol=0.001,
#  verbose=False)
svm.predict([0.5,0.51])
#array([ 2.])
svm.predict([0.5,0.49])
#array([ 1.])

