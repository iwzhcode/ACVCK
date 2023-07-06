import bottom.get_bottom_surface as gbs
import bottom.setting_data.setting as st
import os

filepath,flight_path,strength,range_low,range_high,interval_x,interval_z=st.getsetting()
filename=os.path.split(filepath)[1]
beam=str(flight_path)+strength
all_message=filename+"_"+beam+"_"+str(range_low)+"_"+str(range_high)

f_label = open(".\\label\\signal\\"+all_message+"\\signal.txt","r")
# f_label = open("..\\ATL03_20200419053723_03620701_005_01\\ATL03_20200419053723_03620701_005_01.h5_1l_16.169_16.182.txt","r")
f_ACVCK = open("C:\\Users\\17826\\Desktop\\Program\\bathymetry\\bottom\\result\\result_demo_12\\OPTICS\\"+all_message+".txt","r")
label_lines = f_label.readlines()#读取全部内容
ACVCK_lines = f_ACVCK.readlines()

signal_no=len(label_lines)-1
print("信号个数：",signal_no)

count_line_ACVCK=0


TP_ACVCK=0

# for line in label_lines:
#     count_line_label+=1
#     if(count_line_label>1):
#         arr_label_line=line.split(",")
#         label_x = arr_label_line[2][:11]
#         label_y = arr_label_line[3][:11]
#         label_z = arr_label_line[4][:7]
#         # print(arr_label_line)
#         for lac in ACVCK_lines:
#             count_line_ACVCK += 1
#             if (count_line_ACVCK > 3):
#                 arr_ACVCK_line = lac.split(" ")
#                 acvck_x = arr_ACVCK_line[0][:11]
#                 acvck_y = arr_ACVCK_line[1][:11]
#                 acvck_z = arr_ACVCK_line[2][:7]
#
#                 if(label_x==acvck_x and label_y==acvck_y and label_z==acvck_z):
#                     TP_ACVCK+=1
#                     break
#                 # print(arr_ACVCK_line)

for lac in ACVCK_lines:
    try:
        count_line_ACVCK += 1
        if (count_line_ACVCK > 3):
            arr_ACVCK_line = lac.split(" ")
            acvck_x = round(float(arr_ACVCK_line[0]), 8)
            acvck_y = round(float(arr_ACVCK_line[1]), 8)
            acvck_z = round(float(arr_ACVCK_line[2]), 5)
            count_line_label=0
            for line in label_lines:
                count_line_label += 1
                if (count_line_label > 1):
                    arr_label_line = line.split(",")
                    label_x = round(float(arr_label_line[2]), 8)
                    label_y = round(float(arr_label_line[3]), 8)
                    label_z = round(float(arr_label_line[4]), 5)
                    # print(arr_label_line)
                    # count_level_x_y=0
                    # if (label_x == acvck_x and label_y == acvck_y):
                    #     count_level_x_y+=1
                    # if(count_level_x_y>1):
                    #     print(lac)
                    if (label_x == acvck_x and label_y == acvck_y and label_z == acvck_z):
                        TP_ACVCK += 1
                        break
    except:
        print()



TP_add_FP_ACVCK=len(ACVCK_lines)-3
TP_add_FN_ACVCK=len(label_lines)-1

Precision_ACVCK=TP_ACVCK/TP_add_FP_ACVCK
Recall_ACVCK=TP_ACVCK/TP_add_FN_ACVCK

F1_ACVCK=(2*Precision_ACVCK*Recall_ACVCK)/(Precision_ACVCK+Recall_ACVCK)
IOU_ACVCK=(Precision_ACVCK*Recall_ACVCK)/(Precision_ACVCK+Recall_ACVCK-Precision_ACVCK*Recall_ACVCK)

print("F1_ACVCK,IOU_ACVCK：",F1_ACVCK,IOU_ACVCK)



