# 6 -> Handle Divided by Zero Exception
try:
    ans = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")