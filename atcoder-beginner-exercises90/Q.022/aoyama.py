# import math
num_list = list(map(int,input().split()))
# common_divisor = math.gcd(a,b,c)
# ans = a//common_divisor + b//common_divisor + c//common_divisor - 3
# print(ans)

def get_common_divisor(num1:int,num2:int):

    amari = num1 % num2
    if amari < 1:
        return num2
    return get_common_divisor(num2,amari)

yakusu1 = get_common_divisor(num_list[2],num_list[1])
common_divisor =get_common_divisor(max(yakusu1,num_list[0]),min(yakusu1,num_list[0]))
ans = num_list[0]//common_divisor + num_list[1]//common_divisor + num_list[2]//common_divisor - 3
print(ans)