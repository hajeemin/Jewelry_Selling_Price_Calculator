
# 주얼리 가격 계산하기
    # User에게 직접 가격 묻기

# gold_cost = int(input("금 값을 입력하세요:"))
# production_cost = int(input("기본 공임비, 다이아물림비, 도금비의 총 합을 입력하세요:"))
# stone_cost = int(input("스톤값을 입력하세요:"))
# total_cost = gold_cost + production_cost + stone_cost 

# print("총 금액은", format(total_cost,), "원 입니다.")


#################################################################
# gold_cost = int(input("금 값을 입력하세요:"))
# def production_cost():
#     production_cost_01 = int(input("기본 공임값을 입력하세요:"))
#     diamond_setting_cost = int(input("다이아 세팅 값을 입력하세요:"))
#     gold_plating_cost = int(input("도금비를 입력하세요:"))

#     total = int(production_cost_01 + diamond_setting_cost + gold_plating_cost)
    
    
# stone_cost = int(input("스톤값을 입력하세요:"))
# total_cost = gold_cost + production_cost + stone_cost 

# print("총 금액은", format(total_cost,), "원 입니다.")
####################################################################

#금 시세 구하기
gold_price(per3.75g) = int(input("오늘의 금시세를 입력하세요:"))
gold_weight(g) = int(input("제품의 금 중량을 입력하세요:"))


gold_cost = int(input("금 값을 입력하세요:"))
print(" ")
print("공임값 계산을 시작하겠습니다.")
print(" ")
production_cost_01 = int(input("기본 공임값을 입력하세요:"))
diamond_setting_cost = int(input("다이아 세팅 값을 입력하세요:"))
gold_plating_cost = int(input("도금비를 입력하세요:"))
print(" ")
print("공임값은 총:", production_cost_01 + diamond_setting_cost + gold_plating_cost, "입니다.")
print(" ")
stone_cost = int(input("마지막으로 스톤값을 입력하세요:"))

total_cost = gold_cost + production_cost_01 + diamond_setting_cost + gold_plating_cost + stone_cost 

print(" ")
print("총 원가는", format(total_cost,","), "원 입니다.")
