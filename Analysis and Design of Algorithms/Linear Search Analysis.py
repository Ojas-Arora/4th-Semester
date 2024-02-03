#Linear Search Analysis
import random
import time
import numpy as np
import matplotlib.pyplot as p

def lsearch(array: list[int], key: int) -> list:
    location = -1
    steps=0
    for i in array:
        steps+=1
        if i == key:
            location = array.index(i)
            break
    result=[location,steps]
    return result


def gen(size: int) -> list:
    result = []
    temp = []
    actual_size = size * 10000
    random.seed(time.time())
    for i in range(actual_size):
        temp.append(random.randint(0, actual_size))
    result.append(random.randint(0, actual_size))
    result.append(temp)
    return result


def calc(size: int) -> dict:
    result = {"cum": 0, "avg": 0, "size": 0,'steps':0,'savg':0}
    for i in range(1000):
        list_for_key_and_arr = gen(size)
        temp_for_time = time.time()
        key = lsearch(list_for_key_and_arr[1], list_for_key_and_arr[0])
        total_time_taken = float(time.time() - temp_for_time)
        result["size"] = size * 10000
        result["cum"] += total_time_taken
        result['steps']+=key[1]
    result["avg"] = result["cum"] / 1000
    result["savg"]=result["steps"]/1000
    return result


y_ar = []
x_ar = []
y1ar=[]
for i in range(1,10):
    y1ar.append(i*10000)
for i in range(1, 10):
    temp = calc(i)
    y_ar.append(temp["avg"])
    x_ar.append(temp["size"])
    print(f"done calc for {i}")
    
aux_x=np.array([x_ar[0],x_ar[-1]])
aux_y=np.array([y_ar[0],y_ar[-1]])
y_points = np.array(y_ar)
x_points = np.array(x_ar)
y1points=np.array(y1ar)
p.plot(x_points, y_points,marker="o")
p.plot(aux_x,aux_y,'--',marker='o',color='green')
p.ylabel("Time")
p.xlabel('Size')
p.show()
