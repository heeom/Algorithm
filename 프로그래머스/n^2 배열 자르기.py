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

# https://programmers.co.kr/learn/courses/30/lessons/87390?language=python3

#1*1부터 i*i까지 빈칸을 i로 채움
#시간 초과 : n < 10^9
def solution(n, left, right):
    answer = []
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:
                arr[i][j] = j+1
            else:
                arr[i][j] = i+1
    
    for a in arr:
        answer.extend(a)
        
    return answer[left:right+1]


solution(3,2,5)


#통과
def solution(n, left, right):
    answer = []
    start_row = left // n
    start_col = left % n
    end_row = right // n
    end_col = right % n
    
    #시작행 ~ 마지막행-1까지
    for i in range(start_row, end_row):
        for j in range(n):
            if i < j:
                answer.append(j+1)
            else:
                answer.append(i+1)
    #마지막행
    for i in range(end_col+1): 
        if i < end_row:
            answer.append(end_row+1)
        else:
            answer.append(i+1)

    return answer[start_col:]


solution(3,2,5)

solution(4,7,14)


#다른사람 풀이
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1) #max(행, 열) + 1
    return answer
