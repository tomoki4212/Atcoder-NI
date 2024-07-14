h, w = map(int, input().split())


def calculate_odd_even(n):
    if n % 2 == 1:
        res = (n+1) / 2
    else:
        res = n / 2
    return int(res)


if h == 1 or w == 1:
    print(h*w)
else:
    print(calculate_odd_even(h)*calculate_odd_even(w))
