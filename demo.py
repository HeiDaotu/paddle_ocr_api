result = ["'New Collection', 0.9456021189689636", "'POST 小程序', 0.930759072303772",
          "'POST小程序Copy', 0.87307208776474",
          "'POST 后台', 0.9295517206192017", "'POST后台Copy', 0.8522143363952637", "'POST AI', 0.9896383881568909",
          "'GET 阿里云盘搜素引擎', 0.8800711035728455"]

json_str = []

for line in result:
    line = line.replace(', ', ':')
    json_str.append(line)

json_str = json_str.__str__().replace('"', '').replace('[', '{').replace(']', '}')
print(json_str)
