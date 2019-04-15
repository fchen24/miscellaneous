#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  15 2019
功能：模拟泊松过程 poisson process

@author: chen
"""

import math
import numpy as np

# 泊松分布：描述单位时间内事件发生次数的概率分布
# k(>=0) 表示发生k次
# lambda_poisson(>0) 表示单位时间内，平均发生的次数（时间发生的速率，同指数分布中的参数）
# poisson distribution 泊松分布
def poisson_distri(k,lambda_poisson):
    if lambda_poisson > 0:
        prob_k = math.exp(-lambda_poisson)*lambda_poisson**k \
        /math.factorial(k)
    else:
        print("error lambda parameter")
        return
    return prob_k



t = 0              # t 表示开始时间（假设当前发生第一次事件）
count = 0          # count 表示泊松过程中事件发生的累积次数
T = 10             # 模拟总时间
lambda_poisson = 1

print("poisson process sims start >>>")

time_record = []   # 记录每次时间发生的时间
while t <= T:                                      # 模拟时间消逝，连续时间

    count += 1    
    time_record.append(t)

    random_p = np.random.rand(1)[0]                # 随机产生一个概率
    time_diff = -math.log(1-random_p)/lambda_poisson # 泊松过程中相邻两次事件发生的时间间隔（服从指数分布）
    t += time_diff                                 # 下一次事件发生的时间

print("<<< poisson process sims end")


print("\n")
print("\t次数 \t时间")
for i in range(len(time_record)):

	print("\t{} : \t{}".format(i+1,time_record[i]))

