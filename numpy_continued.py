import numpy as np

x = 1.0		#define a float
y = 2.0		#define another float

#exponents and logarithms
print(np.exp(x))	#e^x
print(np.log(x))	#ln x
print(np.log10(x))	#log_10 x
print(np.log2(x))	#log_2 x

#min/max/misc
print(np.fabs(x))		#absolute value as a float
print(np.fmin(x,y))		#min of x and y
print(np.fmax(x,y))		#max of x and y

#populate arrays
n = 100							#define an integer
z = np.arange(n,dtype=float)	#get an array [1.0,n-1]
z *= 2.0*np.pi /float(n-1)		#z = [0,2*pi0]
sin_z = np.sin(z)				#get an array sin(z)

#interpolation
print(np.interp(0.75,z,sin_z))	#interpolate sin(.75)
print(np.sin(0.75))