# # # 계산기에 배수 추가
# # gold_cost = int(input("금 값을 입력하세요:"))
# # print(" ") # 붙어서 나오는게 안예뻐서 띄어쓰기함.
# # print("공임값 계산을 시작하겠습니다.")
# # print(" ")
# # production_cost_01 = int(input("기본 공임값을 입력하세요:"))
# # diamond_setting_cost = int(input("다이아 세팅 값을 입력하세요:"))
# # gold_plating_cost = int(input("도금비를 입력하세요:"))
# # print(" ")
# # print("공임값은 총:", production_cost_01 + diamond_setting_cost + gold_plating_cost, "입니다.")
# # print(" ")
# # stone_cost = int(input("마지막으로 스톤값을 입력하세요:"))

# # total_cost = gold_cost + production_cost_01 + diamond_setting_cost + gold_plating_cost + stone_cost 

# # print(" ")
# # print("**총 원가는", format(total_cost,","), "원 입니다.**")
# # print(" ")
# # multiplier = float(input("판매 배수를 입력하세요:"))
# # print(" ")
# # print("***판매가는", int(total_cost*multiplier),"입니다.***")
# # sales_price=int(total_cost*multiplier)
# # print(" ")
# # discount = int(input("할인 %를 입력하세요."))
# # final_cost = int(sales_price*((100-discount)/100))
# # print(discount,"%할인가는", format(final_cost,","),"원 입니다.")

# #오늘의 금시세와 장기기반 금값을 비교하여 더 높은 금값으로 계산하는 방법.
# #final_cost에서 바꿀수가있나? 아니면 저 위로 올라가서 코드를 수정해야하나?


# def gold_cost():
#         rct = int(input("장기에 기재된 금값을 입력하세요:")) 
#         tdy = int(input("오늘 금시세로 계산된 금값을 입력하세요:"))
#         if rct < tdy: return tdy
#         else: return rct


# gold_cost()
# g_c = (gold_cost)


# print(" ") # 붙어서 나오는게 안예뻐서 띄어쓰기함.
# print("공임값 계산을 시작하겠습니다.")
# print(" ")
# production_cost_01 = int(input("기본 공임값을 입력하세요:"))
# diamond_setting_cost = int(input("다이아 세팅 값을 입력하세요:"))
# gold_plating_cost = int(input("도금비를 입력하세요:"))
# print(" ")
# print("공임값은 총:", production_cost_01 + diamond_setting_cost + gold_plating_cost, "입니다.")
# print(" ")
# stone_cost = int(input("마지막으로 스톤값을 입력하세요:"))

# total_cost = g_c + production_cost_01 + diamond_setting_cost + gold_plating_cost + stone_cost 

# print(" ")
# print("**총 원가는", format(total_cost,","), "원 입니다.**")
# print(" ")
# multiplier = float(input("판매 배수를 입력하세요:"))
# print(" ")
# print("***판매가는", int(total_cost*multiplier),"입니다.***")
# sales_price=int(total_cost*multiplier)
# print(" ")
# discount = int(input("할인 %를 입력하세요."))
# final_cost = int(sales_price*((100-discount)/100))
# print(discount,"%할인가는", format(final_cost,","),"원 입니다.")

#########다시##########금시세 선택해서 하게하는거에서 되게 복잡하네###############


# def gold_cost():
#         rct = int(input("장기에 기재된 금값을 입력하세요:")) 
#         tdy = int(input("오늘 금시세로 계산된 금값을 입력하세요:"))
#         if rct < tdy: return tdy
#         else: return rct


# print(" ") # 붙어서 나오는게 안예뻐서 띄어쓰기함.
# print("공임값 계산을 시작하겠습니다.")
# print(" ")
# production_cost_01 = int(input("기본 공임값을 입력하세요:"))
# diamond_setting_cost = int(input("다이아 세팅 값을 입력하세요:"))
# gold_plating_cost = int(input("도금비를 입력하세요:"))
# print(" ")
# print("공임값은 총:", production_cost_01 + diamond_setting_cost + gold_plating_cost, "입니다.")
# print(" ")
# stone_cost = int(input("마지막으로 스톤값을 입력하세요:"))

# total_cost = gold_cost()10
# + production_cost_01 + diamond_setting_cost + gold_plating_cost + stone_cost 

# print(" ")
# print("**총 원가는", format(total_cost,","), "원 입니다.**")
# print(" ")
# multiplier = float(input("판매 배수를 입력하세요:"))
# print(" ")
# print("***판매가는", int(total_cost*multiplier),"입니다.***")
# sales_price=int(total_cost*multiplier)
# print(" ")
# discount = int(input("할인 %를 입력하세요."))
# final_cost = int(sales_price*((100-discount)/100))
# print(discount,"%할인가는", format(final_cost,","),"원 입니다.")

#######g_c = gold_cost() 이부분만 지피티한테 물어봄




def gold_cost():
        rct = int(input("장기에 기재된 금값을 입력하세요:")) 
        tdy = int(input("오늘 금시세로 계산된 금값을 입력하세요:"))
        if rct < tdy: return tdy
        else: return rct

g_c = gold_cost()

stone_cost = int(input("스톤값을 입력하세요:"))

print(" ") # 붙어서 나오는게 안예뻐서 띄어쓰기함.
print("----------공임값 계산을 시작하겠습니다----------")
print(" ")
production_cost_01 = int(input("기본 공임값을 입력하세요:"))
diamond_setting_cost = int(input("다이아 세팅 값을 입력하세요:"))
gold_plating_cost = int(input("도금비를 입력하세요:"))
print(" ")
print("공임값은 총:", production_cost_01 + diamond_setting_cost + gold_plating_cost, "입니다.")
print(" ")

total_cost = g_c + production_cost_01 + diamond_setting_cost + gold_plating_cost + stone_cost 

print(" ")
print("**총 원가는", format(total_cost,","), "원 입니다.**")
print(" ")
multiplier = float(input("판매 배수를 입력하세요:"))
print(" ")
print("***판매가는", format(int(total_cost*multiplier),","),"원 입니다.***")
sales_price=int(total_cost*multiplier)
print(" ")
discount = int(input("할인 %를 입력하세요."))
final_cost = int(sales_price*((100-discount)/100))
print(discount,"%할인가는", format(final_cost,","),"원 입니다.")

