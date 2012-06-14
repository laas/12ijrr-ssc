set table "paper.1.table"; set format "%.5f"
set samples 100; plot [x=0:5] 0.2*(0.0048*x**4 - 0.064*x**3+0.24*x**2)*sin(6*x)
