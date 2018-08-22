from sklearn import tree
x=[[144,56,7],[120,46,6],[150,40,5],[160,66,8],[166,66,9],[186,86,7],[132,50,6]]
y=['male','female','female','male','male','male','female']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
prediction=clf.predict([[180,80,8]])
print(prediction)
