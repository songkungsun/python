icecream = {
    'Tankboy': (1200, 5),  # 가격, 수량
    'Pollapo': (1200, 10),
    'Ppangppare': (1800, 3),
    'Worldcorn': (1500, 7),
    'Melona': (1000, 8),
    'Heathunting': (1200, 6)
}
# 월드콘 가격
print(icecream['Worldcorn'][0])

# 월드콘 수
print(icecream['Worldcorn'][1])

# 남은 수량이 7개 남은 제품 이름
for name,rest in icecream.items():
    # print(name, rest[1])
    if rest[1] ==7:
        print(name)

# 희망가격이 1200원인 제품 이름 ,수량
for name,rest in icecream.items():
    if rest[0]== 1200:
        print(name,rest[1])

