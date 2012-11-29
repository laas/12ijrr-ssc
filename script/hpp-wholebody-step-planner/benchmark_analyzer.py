#!/usr/bin/python

import numpy as np
import scipy as sp
import pylab as pl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Load benchmark data.
# ch_rrt = np.genfromtxt("chairs/bench-rrt.log")
# ch_ipp = np.genfromtxt("chairs/bench-ipp.log")
oc_rrt = np.genfromtxt("objects-cloud/bench-rrt.log")
oc_ipp = np.genfromtxt("objects-cloud/bench-ipp.log")
sh_rrt = np.genfromtxt("shelf/bench-rrt.log")
sh_ipp = np.genfromtxt("shelf/bench-ipp.log")

rrt = [
    # ('Chairs\n RRT', ch_rrt),
    # ('Chairs\n IPP-RRT', ch_ipp),
    ('Floating\n RRT', oc_rrt),
    ('Floating\n IPP-RRT', oc_ipp),
    ('Shelf\n RRT', sh_rrt),
    ('Shelf\n IPP-RRT', sh_ipp)
    ]

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

plt.rcParams.update({'font.size': 16})
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Plot data.
ind = np.arange(len(rrt)) + 1

x_label_list = []
for i in rrt:
    x_label_list.append(i[0])

x_label = tuple (x_label_list)

#bar_colors = ['#a9c2f6', '#86fb90']
bar_colors = ['#4f5a72', '#2b512e']
text_spacing = 0.05 # relative of top

fig1 = plt.figure(1)
splt1 = fig1.add_subplot(111)
splt1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                 alpha=1)
splt1.set_axisbelow(True)
splt1.errorbar(ind, m_it, yerr=s_it, fmt='d', capsize=15, elinewidth=2,
               capthick=2, color = '#dd4924')
splt1.bar(ind-0.1, width=0.2, bottom=min_it, height=max_it-min_it,
          color=['#a9c2f6', '#86fb90', '#a9c2f6', '#86fb90'])
splt1.set_xticks(ind)
splt1.set_xticklabels(x_label)
splt1.set_ylabel('Number of RRT iterations')
left1 = 0.5
right1 = len(rrt) + 0.5
splt1.set_xlim(left1, right1)
bottom1 = -1500
top1 = 23000
splt1.set_ylim(bottom1, top1)
for tick, i in zip(ind, range(len(rrt))):
    k = (tick + 1) % 2
    pos = tick - 0.35
    splt1.text(pos, top1-(top1*1.5*text_spacing),
               r"$\mathbf{\overline{it}}$ = " + str(int(m_it[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color='#ad2100') 
    splt1.text(pos, top1-(top1*2.5*text_spacing),
               r"$\sigma_{it}$ = " + str(int(s_it[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color='#ad2100')
    splt1.text(pos, top1-(top1*3.5*text_spacing),
               "min = "+ str(int(min_it[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color=bar_colors[k])
    splt1.text(pos, top1-(top1*4.5*text_spacing),
               "max = "+ str(int(max_it[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color=bar_colors[k])

fig2 = plt.figure(2)
splt2 = fig2.add_subplot(111)
splt2.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                 alpha=1)
splt2.set_axisbelow(True)
splt2.errorbar(ind, m_t, yerr=s_t, fmt='d', capsize=15, elinewidth=2,
               capthick=2, color = '#dd4924')
splt2.bar(ind-0.1, width=0.2, bottom=min_t, height=max_t-min_t,
          color=['#a9c2f6', '#86fb90', '#a9c2f6', '#86fb90'])
splt2.set_xticks(ind)
splt2.set_xticklabels(x_label)
splt2.set_xlim(0.5, len(rrt) + 0.5)
splt2.set_ylabel('RRT computation time (s)')
left2 = 0.5
right2 = len(rrt) + 0.5
splt2.set_xlim(left2, right2)
bottom2 = -50
top2 = 750
splt2.set_ylim(bottom2, top2)
for tick, i in zip(ind, range(len(rrt))):
    k = (tick + 1) % 2
    pos = tick - 0.35
    splt2.text(pos, top2-(top2*1.5*text_spacing),
               r"$\mathbf{\overline{t}}$ = " + str(int(m_t[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color='#ad2100') 
    splt2.text(pos, top2-(top2*2.5*text_spacing),
               r"$\sigma_{t}$ = " + str(int(s_t[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color='#ad2100')
    splt2.text(pos, top2-(top2*3.5*text_spacing),
               "min = "+ str(np.round(min_t[i],1)),
               horizontalalignment='left', size='medium',
               weight='bold', color=bar_colors[k])
    splt2.text(pos, top2-(top2*4.5*text_spacing),
               "max = "+ str(np.round(max_t[i],1)),
               horizontalalignment='left', size='medium',
               weight='bold', color=bar_colors[k])

fig3 = plt.figure(3)
splt3 = fig3.add_subplot(111)
splt3.set_axisbelow(True)
splt3.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                 alpha=1)
splt3.errorbar(ind, m_n, yerr=s_n, fmt='d', capsize=15, elinewidth=2,
               capthick=2, color = '#dd4924')
splt3.bar(ind-0.1, width=0.2, bottom=min_n, height=max_n-min_n,
          color=['#a9c2f6', '#86fb90', '#a9c2f6', '#86fb90'])
splt3.set_xticks(ind)
splt3.set_xticklabels(x_label)
splt3.set_xlim(0.5, len(rrt) + 0.5)
splt3.set_ylabel('Number of tree nodes')
left3 = 0.5
right3 = len(rrt) + 0.5
splt3.set_xlim(left3, right3)
bottom2 = -150
top2 = 2600
splt3.set_ylim(bottom2, top2)
for tick, i in zip(ind, range(len(rrt))):
    k = (tick + 1) % 2
    pos = tick - 0.35
    splt3.text(pos, top2-(top2*1.5*text_spacing),
               r"$\mathbf{\overline{n}}$ = " + str(int(m_n[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color='#ad2100') 
    splt3.text(pos, top2-(top2*2.5*text_spacing),
               r"$\sigma_{n}$ = " + str(int(s_n[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color='#ad2100')
    splt3.text(pos, top2-(top2*3.5*text_spacing),
               "min = "+ str(int(min_n[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color=bar_colors[k])
    splt3.text(pos, top2-(top2*4.5*text_spacing),
               "max = "+ str(int(max_n[i])),
               horizontalalignment='left', size='medium',
               weight='bold', color=bar_colors[k])

plt.show ()
