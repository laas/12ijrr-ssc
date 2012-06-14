set table "paper.3.table"; set format "%.5f"
set samples 100; plot [x=0:5]  (0.92*(0.0048*x**4 - 0.064*x**3 +0.24*x**2))*sin(6.*x) -(0.02*(0.0576*x**2-0.384*x+.48))*sin(6.*x)-(0.24*(0.0192*x**3-.192*x**2+.48*x))*cos(6.*x) 
