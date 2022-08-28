def most_frequent(string);
 import operator
 d{}
 for key in string:
 if key not in d:
 d[key]=1
 else:
 d[key]+=1
 d_lower={k.lower():v for k, v in d.items9)}
 d-sorted=dict(sorted(d.items(),key=operators.intmegetter(1),reverse=true))
 return_d stored
 input=input("please enter a string missisippi")
 print(most_frequent(input))
