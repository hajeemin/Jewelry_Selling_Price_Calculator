# #금 시세 구하기
# gold_price = int(input("오늘의 금시세를 입력하세요(per 3.75g):"))
# gold_weight = float(input("제품의 금 중량을 입력하세요(g):"))
# weight_cost_today = (gold_price/3.75)*gold_weight

def gold_cost():

        gold_price = int(input("오늘의 금시세를 입력하세요(per 3.75g):"))
        gold_weight = float(input("제품의 금 중량을 입력하세요(g):"))
        weight_cost_today = (gold_price/3.75)*gold_weight
        
        rct = int(input("장기에 기재된 금값을 입력하세요:")) 

        if rct < weight_cost_today: return weight_cost_today
        else: return rct

g_c = gold_cost()

stone_cost = int(input("스톤값을 입력하세요:"))

print("\n----------공임값 계산을 시작하겠습니다----------\n")

production_cost_01 = int(input("기본 공임값을 입력하세요:"))
diamond_setting_cost = int(input("다이아 세팅 값을 입력하세요:"))
gold_plating_cost = int(input("도금비를 입력하세요:"))

print("\n공임값은 총:", production_cost_01 + diamond_setting_cost + gold_plating_cost, "입니다.\n")


total_cost = g_c + production_cost_01 + diamond_setting_cost + gold_plating_cost + stone_cost 


print("\n**총 원가는", format(total_cost,","), "원 입니다.**\n")

multiplier = float(input("판매 배수를 입력하세요:"))

print("\n***판매가는", format(int(total_cost*multiplier),","),"원 입니다.***\n")
sales_price=int(total_cost*multiplier)

discount = int(input("\n할인 %를 입력하세요.\n"))
final_cost = int(sales_price*((100-discount)/100))
print(discount,"%할인가는", format(final_cost,","),"원 입니다.")

