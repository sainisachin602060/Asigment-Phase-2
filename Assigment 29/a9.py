import pickle

d1={
    'java':550,
    'python':222,
    'C++':199,
    'JavaScript':558,
}
f1=open("bookfile","wb")
pickle.dump(d1,f1)
f1.close()
