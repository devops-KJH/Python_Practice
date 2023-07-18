#사용자로부터 -1을 입력 받으면 프로그램이 종료되는 프로그램을 작성해보세요.

# print("프로그램 시작")

# while True:
#     num = int(input("종료하려면 -1을 입력하세요.>>>"))
#     if num == -1:
#         print("프로그램 종료")
#         break
#     else:
#         print("종료하려면 -1을 입력하세요.")

#강사 답안

print("프로그램 시작")

# num = int(input("종료하려면 -1을 입력하세요:"))

# while num != -1:
#     num = int(input("종료하려면 -1을 입력하세요:"))

while True:
    num = int(input("종료하려면 -1을 입력하세요.:"))
    if num == -1:
        break

print("프로그램 종료")