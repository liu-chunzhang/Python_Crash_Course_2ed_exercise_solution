import time  			# 为了计时而引入的标准库，标准库的简略叙述见教材P161

naturalNumbers = list(range(1,1_000_001))

# 检验这组数的最大值和最小值
print(min(naturalNumbers))
print(max(naturalNumbers))

# 对于求和过程前后计时
start_time = time.time()
results = sum(naturalNumbers)
end_time = time.time()

# 导出求和过程所需要的时间
temp = end_time - start_time
print(f"summation process costs {temp} ms.")