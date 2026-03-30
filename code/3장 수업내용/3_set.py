# 3_set.py
# 두 집합 정의
set1 = {1, 2, 3, 'a', "Hello"}
set2 = {"Hello", 3, 4, 5, 'b'}

# 합집합(union)
union_set = set1 | set2 # c에서 || = OR, py에서 or

# 교집합 (itersection)
int_set = set1 & set2 # && = and

# 차집합 (differance)
diff_set = set1 - set2

# 대칭 차집합 (symetric_diff) (union - intersection)
sym_diff_set = set1 ^ set2 # 합집합과 교집합의 차집합

print('union:', union_set)
print(f"itersection : {int_set}")
print(f"difference: {diff_set}")
print(f"symmetrice difference: {sym_diff_set}")