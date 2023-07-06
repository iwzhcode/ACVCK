import numpy as np

import bottom.get_bottom_surface as gbs
import bottom.setting_data.setting as st
import os

filepath,flight_path,strength,range_low,range_high,interval_x,interval_z=st.getsetting()
filename=os.path.split(filepath)[1]
beam=str(flight_path)+strength
all_message=filename+"_"+beam+"_"+str(range_low)+"_"+str(range_high)

f_label = open(".\\label\\image\\"+all_message+"\\manual_fitting_result.txt","r")
# f_label = open("..\\ATL03_20200419053723_03620701_005_01\\ATL03_20200419053723_03620701_005_01.h5_1l_16.169_16.182.txt","r")
f_ACVCK = open("C:\\Users\\17826\\Desktop\\Program\\bathymetry\\bottom\\result\\result_demo_12\\ACVCK\\"+all_message+"\\"+"manual_fitting_result.txt","r")
label_lines = f_label.readlines()#读取全部内容
ACVCK_lines = f_ACVCK.readlines()

signal_no=len(label_lines)-1
print("信号个数：",signal_no)

count_line_ACVCK=0
count_line_label=0
arr_test=[]
arr_label=[]
diff_test_label=[]


TP_ACVCK=0
max_range=13589
for lac in ACVCK_lines:
    count_line_ACVCK += 1
    if (count_line_ACVCK > 1 and count_line_ACVCK<max_range):
        arr_ACVCK_line = lac.split(" ")
        acvck_z = float(arr_ACVCK_line[2])
        arr_test.append(acvck_z)

for line in label_lines:
    count_line_label+=1
    if(count_line_label>1 and count_line_label<max_range):
        arr_label_line=line.split(" ")
        label_z = float(arr_label_line[2])
        arr_label.append(label_z)

for i in range(len(arr_label)):
    diff_test_label.append(abs(arr_label[i]-arr_test[i]))
diffangsum=0
for i in range(len(diff_test_label)):
    diffangsum+=diff_test_label[i]**2

RMSE=(diffangsum/len(diff_test_label))**0.5

MAE=np.average(diff_test_label)
MAX=np.max(diff_test_label)
MED=np.median(diff_test_label)
print("RMSE,MAX,MED,MAE:")
print(RMSE,MAX,MED,MAE)








