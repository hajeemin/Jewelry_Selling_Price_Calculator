import streamlit as st

st.title("💎주얼리 판매가 계산기💎")

gold_cost = st.number_input(
    "금 재료비(원)",
    min_value=0,
    value=680000,
    step=1000
    )

today_gold_cost = st.number_input(
    "오늘 기준 금 재료비(원)",
    min_value=0,
    value=650000,
    step=1000
)

if today_gold_cost > gold_cost:
    applied_gold_cost = today_gold_cost
else:
    applied_gold_cost = gold_cost

st.write("적용할 금 재료비:", format(applied_gold_cost,","),"원")

st.subheader("제작비용")

production_cost = st.number_input("기본 공임(원)", min_value=0, value=84000, step=1000)
setting_cost = st.number_input("스톤 세팅비(원)", min_value=0, value=40000, step=1000)
plating_cost = st.number_input("도금비(원)", min_value=0, value=8000,step=1000)
stone_cost = st.number_input("스톤 금액(원)", min_value=0, value=500000, step=1000)

total_cost = (
    applied_gold_cost
    + production_cost
    + setting_cost
    + plating_cost
    + stone_cost
)

st.metric("판매가 계산용 원가", format(total_cost,",")+"원")

####################판매 조건(배수, 할인률)##########################

st.subheader("판매 조건")

multiplier = st.number_input(
    "판매 배수",
    min_value=0.1,
    value=2.5,
    step=0.1
)

discount = st.number_input(
    "할인율(%)",
    min_value=0,
    max_value=100,
    value=20,
    step=1
)

sales_price = int(total_cost * multiplier)
final_price = int(sales_price*(100-discount)/100)
discount_amount = sales_price - final_price

st.subheader("계산 결과")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("정상 판매가:", format(sales_price,",")+"원")

with col2:
    st.metric("할인 금액:", format(discount_amount,",")+"원")

with col3:
    st.metric("최종 판매가:", format(final_price,",")+"원")
