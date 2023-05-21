# 과제 1번 정규식을 사용해야하는 이유

data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
print("----정규식을 사용하지 않았을 때----")
## 정규식을 사용하지 않았을 때
import re 

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
# 정규식을 사용 했을 때
# 코드가 상당히 간결해진다
# 메타 문자
