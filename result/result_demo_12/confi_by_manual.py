
f_label = open(".\\label\\signal\\"+"ATL03_20210818183003_08571207_005_01.h5_2r_16.165_16.207"+"\\signal.txt","r")
# f_label = open("..\\ATL03_20200419053723_03620701_005_01\\ATL03_20200419053723_03620701_005_01.h5_1l_16.169_16.182.txt","r")
f_ACVCK = open(".\\ACVCK\\"+"ATL03_20210818183003_08571207_005_01.h5_2r_16.165_16.207.txt","r")
label_lines = f_label.readlines()#读取全部内容
ACVCK_lines = f_ACVCK.readlines()

signal_no=len(label_lines)-1
print("信号个数：",signal_no)

count_line_ACVCK = 0
count_high = 0
TP_ACVCK = 0
str_con="high"

for lac in ACVCK_lines:
    count_line_ACVCK += 1
    if (count_line_ACVCK > 3):
        arr_ACVCK_line = lac.split(" ")
        if (arr_ACVCK_line[3] == str_con+"\n" and float(arr_ACVCK_line[0])<16.347):
            count_high += 1
            acvck_x = round(float(arr_ACVCK_line[0]), 8)
            acvck_y = round(float(arr_ACVCK_line[1]), 8)
            acvck_z = round(float(arr_ACVCK_line[2]), 5)
            count_line_label = 0
            for line in label_lines:
                count_line_label += 1
                if (count_line_label > 1):
                    arr_label_line = line.split(",")
                    label_x = round(float(arr_label_line[2]), 8)
                    label_y = round(float(arr_label_line[3]), 8)
                    label_z = round(float(arr_label_line[4]), 5)

                    if (label_x == acvck_x and label_y == acvck_y and label_z == acvck_z):
                        TP_ACVCK += 1
                        break


print(TP_ACVCK,count_high)
print(round(TP_ACVCK/count_high,2))
# jingdu_high=get_confi_jd("high\n")
# jingdu_median=get_confi_jd("median\n")
# jingdu_low=get_confi_jd("low\n")
# print(jingdu_high,jingdu_median,jingdu_low)



