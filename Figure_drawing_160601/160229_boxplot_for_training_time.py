# -*- coding: utf-8 -*-
__author__ = 'jeong-yonghan'

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


File = 'training_time.txt'
ReadFile = open(File,'rb')
RecordNum = [105, 106, 108, 109, 114, 119, 119,
             200, 202, 203, 205, 208, 209, 210,
             213, 214, 215, 219, 221, 223, 228,
             233]

iterIdx = 0
DictPerformance_acc = dict()
DictPerformance_se = dict()
DictPerformance_spe = dict()
DictPerformance_pp = dict()

DictPerformance_acc['300'] = list()
DictPerformance_acc['240'] = list()
DictPerformance_acc['180'] = list()
DictPerformance_acc['120'] = list()
DictPerformance_acc['60'] = list()

DictPerformance_se['300'] = list()
DictPerformance_se['240'] = list()
DictPerformance_se['180'] = list()
DictPerformance_se['120'] = list()
DictPerformance_se['60'] = list()

DictPerformance_spe['300'] = list()
DictPerformance_spe['240'] = list()
DictPerformance_spe['180'] = list()
DictPerformance_spe['120'] = list()
DictPerformance_spe['60'] = list()

DictPerformance_pp['300'] = list()
DictPerformance_pp['240'] = list()
DictPerformance_pp['180'] = list()
DictPerformance_pp['120'] = list()
DictPerformance_pp['60'] = list()

rowNum = 15
colNum = 5

for row in ReadFile.readlines():
    List_Row = row.split("\t")
    for idx in range(len(List_Row)):
        if idx != rowNum:
            try:
                List_Row[idx] = float(List_Row[idx])
            except:
                List_Row[idx] = 1.
        else:
            List_Row[idx] = List_Row[idx].replace('\n','')
            try:
                List_Row[idx] = float(List_Row[idx])
            except:
                List_Row[idx] = 1.

        if idx < colNum:
            if idx % colNum == 0:
                DictPerformance_acc['300'].append(List_Row[idx])
            elif idx % colNum == 1:
                DictPerformance_acc['240'].append(List_Row[idx])
            elif idx % colNum == 2:
                DictPerformance_acc['180'].append(List_Row[idx])
            elif idx % colNum == 3:
                DictPerformance_acc['120'].append(List_Row[idx])
            elif idx % colNum == 4:
                DictPerformance_acc['60'].append(List_Row[idx])
        elif idx >= colNum and idx < 2*colNum:
            if idx % colNum == 0:
                DictPerformance_se['300'].append(List_Row[idx])
            elif idx % colNum == 1:
                DictPerformance_se['240'].append(List_Row[idx])
            elif idx % colNum == 2:
                DictPerformance_se['180'].append(List_Row[idx])
            elif idx % colNum == 3:
                DictPerformance_se['120'].append(List_Row[idx])
            elif idx % colNum == 4:
                DictPerformance_se['60'].append(List_Row[idx])
        elif idx >= 2*colNum and idx < 3*colNum:
            if idx % colNum == 0:
                DictPerformance_spe['300'].append(List_Row[idx])
            elif idx % colNum == 1:
                DictPerformance_spe['240'].append(List_Row[idx])
            elif idx % colNum == 2:
                DictPerformance_spe['180'].append(List_Row[idx])
            elif idx % colNum == 3:
                DictPerformance_spe['120'].append(List_Row[idx])
            elif idx % colNum == 4:
                DictPerformance_spe['60'].append(List_Row[idx])
        elif idx >= 3*colNum:
            if idx % colNum == 0:
                DictPerformance_pp['300'].append(List_Row[idx])
            elif idx % colNum == 1:
                DictPerformance_pp['240'].append(List_Row[idx])
            elif idx % colNum == 2:
                DictPerformance_pp['180'].append(List_Row[idx])
            elif idx % colNum == 3:
                DictPerformance_pp['120'].append(List_Row[idx])
            elif idx % colNum == 4:
                DictPerformance_pp['60'].append(List_Row[idx])


BoxPlotData_acc = [DictPerformance_acc['300'], DictPerformance_acc['240'],DictPerformance_acc['180'],DictPerformance_acc['120'],DictPerformance_acc['60']]
BoxPlotData_se = [DictPerformance_se['300'], DictPerformance_se['240'],DictPerformance_se['180'],DictPerformance_se['120'],DictPerformance_se['60']]
BoxPlotData_spe = [DictPerformance_spe['300'], DictPerformance_spe['240'],DictPerformance_spe['180'],DictPerformance_spe['120'],DictPerformance_spe['60']]
BoxPlotData_pp = [DictPerformance_pp['300'], DictPerformance_pp['240'],DictPerformance_pp['180'],DictPerformance_pp['120'],DictPerformance_pp['60']]


# for elem in DictPerformance_SPC['Acc']:
#     print elem
#



fig, ax = plt.subplots(2,2, figsize=(10,6))
fig.canvas.set_window_title('Performance comparison')
plt.subplots_adjust(left=0.075, right = 0.95, top = 0.95, bottom = 0.00)
AccBox = ax[0,0].boxplot(BoxPlotData_acc, notch=0, sym = '+', vert=1, whis=1.5)
SeBox = ax[0,1].boxplot(BoxPlotData_se, notch=0, sym = '+', vert=1, whis=1.5)
SpeBox = ax[1,0].boxplot(BoxPlotData_spe, notch=0, sym = '+', vert=1, whis=1.5)
PpBox = ax[1,1].boxplot(BoxPlotData_pp, notch=0, sym = '+', vert=1, whis=1.5)

plt.setp(AccBox['boxes'], color='black')
plt.setp(AccBox['whiskers'], color='black')
plt.setp(AccBox['fliers'], color='red', marker='+')

plt.setp(SeBox['boxes'], color='black')
plt.setp(SeBox['whiskers'], color='black')
plt.setp(SeBox['fliers'], color='red', marker='+')

plt.setp(SpeBox['boxes'], color='black')
plt.setp(SpeBox['whiskers'], color='black')
plt.setp(SpeBox['fliers'], color='red', marker='+')

plt.setp(PpBox['boxes'], color='black')
plt.setp(PpBox['whiskers'], color='black')
plt.setp(PpBox['fliers'], color='red', marker='+')

plt.tight_layout()

ax[0,0].yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
ax[0,1].yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
ax[1,0].yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
ax[1,1].yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)

ax[0,0].set_title('Accuracy').set_fontsize(20)
ax[0,1].set_title('Sensitivity').set_fontsize(20)
ax[1,0].set_title('Specificity').set_fontsize(20)
ax[1,1].set_title('Positive Predictivity').set_fontsize(20)

# plt.setp(ax[0,0].get_xticklabels(), visible=False)
# plt.setp(ax[0,1].get_xticklabels(), visible=False)

# ax[0,0].set_ylabel('Accuracy')
# ax[0,1].set_ylabel('Sensitivity')
# ax[1,0].set_ylabel('Specificity')
# ax[1,1].set_ylabel('Positive predictivity')
#
ax[0,0].set_axisbelow(True)
ax[0,1].set_axisbelow(True)
ax[1,0].set_axisbelow(True)
ax[1,1].set_axisbelow(True)



# ax1.set_ylabel('Accuracy')
ClassifierList = ['0.1','0.05', '0.01','0.0023']
plt.setp(ax, xticks = [1,2,3,4,5], xticklabels=['300','240', '180','120','60'])

plt.sca(ax[0,0])
plt.xticks(size=15)
plt.sca(ax[0,1])
plt.xticks(size=15)
plt.sca(ax[1,0])
plt.xticks(size=15)
plt.sca(ax[1,1])
plt.xticks(size=15)


plt.show()


