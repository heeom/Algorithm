# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

def solution(line):
    answer = []
    n = len(line)
    stars = []
    
    for i in range(n-1):
        for j in range(i+1, n):
            a,b,e = line[i]
            c,d,f = line[j]
            if a*d - b*c == 0: # 밑이 0이면 continue (0으로 나눌 수 없다)
                continue

            if (b*f - e*d) % (a*d - b*c) == 0 and (e*c - a*f) % (a*d - b*c) == 0: #정수 판별
                x = (b*f - e*d) // (a*d - b*c)
                y = (e*c - a*f) // (a*d - b*c)
                stars.append([x,y])
    
    # 가장작은 x좌표와 가장 큰 y좌표를 기준으로 
    min_x = min(stars)[0]
    max_y = max(stars, key=lambda x:x[1])[1]
       
    # 기준좌표를 (0,0)으로 옮긴다 (모든 좌표는 4사분면에 위치한다 -> x>=0 and y<=0)
    for s in stars:
        s[0] -= min_x
        s[1] -= max_y
        
    #행과 열의 범위를 구한다 -> 행:가장 작은 y좌표의 절대값, 열:가장 큰 x좌표
    c = max(stars)[0]
    r = abs(min(stars, key=lambda x:x[1])[1])
    
    #0부터 시작이므로 r+1, c+1
    for i in range(r+1):
        star = ''
        for j in range(c+1):
            if [j, -i] in stars:
                star+='*'
            else:
                star+='.'
        answer.append(star)
    
    return answer


solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])




