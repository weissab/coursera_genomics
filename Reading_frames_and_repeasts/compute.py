#!/c/Users/Andrea/Anaconda3/python

"""
add annotation here 

have to write into command window: 'chmod a+x FILENAME'
adding this line makes the program executable

to run from command window: python FILENAME
"""
input= input('Ender input:')

# add annotation here:
def compute(n,x,y) :
    
	if n==0 : return x
    
	return compute(n-1,x+y,y)

print (compute)