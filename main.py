# 接收用户输入的字符串
text = input("请输入一个字符串：")

# 统计每个字符的出现频率
char_freq = {}
for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# 按字符出现频率降序排序
sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

# 打印结果
for char, freq in sorted_chars:
    print(f"字符 '{char}' 出现的频率为：{freq}")
