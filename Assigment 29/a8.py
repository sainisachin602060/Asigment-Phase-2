import shutil
import pickle

src=r"G:\ineuron solution\Assigment 29"
dest="G:\ineuron solution\Assigment 28"

path=shutil.copyfile(src,dest)


l1=['rood']
f=open("fourth.txt","ab")
pickle.dump(l1,f)
f.close()



