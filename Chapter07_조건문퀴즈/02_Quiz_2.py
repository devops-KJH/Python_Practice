#프로그램 사용자로부터 가방과 시계의 금액을 입력 받는다.
#조건에 따라 합계 금액을 계산하고, 합계금액을 출력한다.
#1.합계금액이 10만원 이상이면 할인률 30%
#2.합계금액이 5만원이상 10만원 미만이면 할인률 20%
#3.합계금액이 5만원 미만이면 할인률 10%

bag_price = int(input("가방의 가격을 입력해주세요.>>>"))
watch_price = int(input("시계의 가격을 입력해주세요.>>>"))
4
total_price = bag_price + watch_price

if total_price >= 100000:
    total_price = total_price*0.7
elif total_price >= 50000:
    total_price = total_price*0.8
else:
    total_price = total_price*0.9

print("합계금액은 :", total_price)