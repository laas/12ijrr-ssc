#!/usr/bin/python

import numpy as np
import scipy as sp
import pylab as pl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Load benchmark data.
oc_rrt = np.genfromtxt("objects-cloud/bench-rrt.log")
oc_ipp = np.genfromtxt("objects-cloud/bench-ipp.log")
sh_rrt = np.genfromtxt("shelf/bench-rrt.log")
sh_ipp = np.genfromtxt("shelf/bench-rrt.log")
# lt_rrt = np.genfromtxt("bench-lt-rrt.log")
# pca_rrt = np.genfromtxt("bench-pca-rrt.log")
# pca_ipp = np.genfromtxt("bench-pca-ipp.log")
# lt_ipp = np.genfromtxt("bench-lt-ipp.log")
# pca_lt_rrt = np.genfromtxt("bench-pca-lt-rrt.log")
# pca_lt_ipp = np.genfromtxt("bench-pca-lt-ipp.log")

rrt = [('Floating obstacles\n RRT', oc_rrt),
       ('Floating obstacles\n IPP-RRT', oc_ipp),
       ('Shelf\n RRT', sh_ipp),
       ('Shelf\n IPP-RRT', sh_ipp)]
       # ('Local-Trees RRT', lt_rrt),
       # ('Local-Trees IPP-RRT', lt_ipp),
       # ('PCA-RRT', pca_rrt),
       # ('PCA-IPP-RRT', pca_ipp),
       # ('PCA-LT-RRT', pca_lt_rrt),
       # ('PCA-LT-IPP-RRT', pca_lt_ipp)]

# Compute mean and standard deviation over rows (axis 0 of array).
m_rrt = []
s_rrt = []
min_rrt = []
max_rrt = []
for i in range(len(rrt)):
    m_rrt.append(sp.mean(rrt[i][1], 0))
    s_rrt.append(sp.std(rrt[i][1], 0))
    min_rrt.append(sp.amin(rrt[i][1], 0))
    max_rrt.append(sp.amax(rrt[i][1], 0))

# Build node, iterations, and time vectors.
m_it = np.zeros(len(rrt))
s_it = np.zeros(len(rrt))
min_it = np.zeros(len(rrt))
max_it = np.zeros(len(rrt))
m_t = np.zeros(len(rrt))
s_t = np.zeros(len(rrt))
min_t = np.zeros(len(rrt))
max_t = np.zeros(len(rrt))
m_n = np.zeros(len(rrt))
s_n = np.zeros(len(rrt))
min_n = np.zeros(len(rrt))
max_n = np.zeros(len(rrt))
for i in range(len(rrt)):
   m_it[i] = m_rrt[i][1]
   s_it[i] = s_rrt[i][1]
   min_it[i] = min_rrt[i][1]
   max_it[i] = max_rrt[i][1]
   m_t[i] = m_rrt[i][2]
   s_t[i] = s_rrt[i][2]
   min_t[i] = min_rrt[i][2]
   max_t[i] = max_rrt[i][2]
   m_n[i] = m_rrt[i][19]
   s_n[i] = s_rrt[i][19]
   min_n[i] = min_rrt[i][19]
   max_n[i] = max_rrt[i][19]

data_it = []
data_t = []
data_n = []
for i in range(len(rrt)):
    data_it.append (rrt[i][1][:,1])
    data_t.append (rrt[i][1][:,2])
    data_n.append (rrt[i][1][:,19])

data_it = (np.array) (data_it)
data_it = data_it.transpose()
data_t = (np.array) (data_t)
data_t = data_t.transpose()
data_n = (np.array) (data_n)
data_n = data_n.transpose()

# Plot data.
ind = np.arange(len(rrt)) + 1

x_label_list = []
for i in range(len(rrt)):
    x_label_list.append(rrt[i][0])

x_label = tuple (x_label_list)

fig1 = plt.figure(1)
splt1 = fig1.add_subplot(111)
splt1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                 alpha=1)
splt1.set_axisbelow(True)
splt1.errorbar(ind, m_it, yerr=s_it, fmt='d', capsize=15, elinewidth=2,
               capthick=2, color = '#f37428')
#splt1.errorbar(ind, m_it, yerr=[m_it - min_it, max_it - m_it], fmt='d')
splt1.bar(ind-0.05, width=0.1, bottom=min_it, height=max_it-min_it,
          color=['#a9c2f6', '#86fb90', '#a9c2f6', '#86fb90'])
#splt1.boxplot(data_it, whis=1e6)
splt1.set_xticks(ind)
splt1.set_xticklabels(x_label)
splt1.set_xlim(0.5, len(rrt) + 0.5)
splt1.set_ylabel('Number of RRT iterations')

fig2 = plt.figure(2)
splt2 = fig2.add_subplot(111)
splt2.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                 alpha=1)
splt2.set_axisbelow(True)
splt2.errorbar(ind, m_t, yerr=s_t, fmt='d', capsize=15, elinewidth=2,
               capthick=2, color = '#f37428')
#splt2.errorbar(ind, m_t, yerr=[m_t - min_t, max_t - m_t], fmt='d')
splt2.bar(ind-0.05, width=0.1, bottom=min_t, height=max_t-min_t,
          color=['#a9c2f6', '#86fb90', '#a9c2f6', '#86fb90'])
#splt2.boxplot(data_t, whis=1e6)
splt2.set_xticks(ind)
splt2.set_xticklabels(x_label)
splt2.set_xlim(0.5, len(rrt) + 0.5)
splt2.set_ylabel('RRT computation time (s)')

fig3 = plt.figure(3)
splt3 = fig3.add_subplot(111)
splt3.set_axisbelow(True)
splt3.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                 alpha=1)
splt3.errorbar(ind, m_n, yerr=s_n, fmt='d', capsize=15, elinewidth=2,
               capthick=2, color = '#f37428')
#splt3.errorbar(ind, m_n, yerr=[m_n - min_n, max_n - m_n], fmt='d')
splt3.bar(ind-0.05, width=0.1, bottom=min_n, height=max_n-min_n,
          color=['#a9c2f6', '#86fb90', '#a9c2f6', '#86fb90'])
#splt3.boxplot(data_n, whis=1e6)
splt3.set_xticks(ind)
splt3.set_xticklabels(x_label)
splt3.set_xlim(0.5, len(rrt) + 0.5)
splt3.set_ylabel('Number of tree nodes')

plt.show ()
