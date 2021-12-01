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

# https://programmers.co.kr/learn/courses/30/lessons/42890

# +
from itertools import combinations

def solution(relation):
    answer = 0
    
    col = len(relation[0])
    row = len(relation)
    
    candidate = []
    #키후보 전체 조합 구하기
    for i in range(1, col+1): #전체 key에서 i개의 key index조합
        candidate.extend(combinations(range(col),i))
    
    #유일성: 모든 튜플에 대해 유일하게 식별
    unique = []
    for c in candidate:
        unique_candi = [tuple([item[i] for i in c]) for item in relation]
        if len(set(unique_candi)) == row:
            unique.append(c)
    
    #최소성: 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)


# -

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
