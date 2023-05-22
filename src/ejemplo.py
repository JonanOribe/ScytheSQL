# content of test_sample.py
percentaje=200
amount=110
def taxes(amount: int, percentaje: int):
    return ((amount*percentaje)/100)+amount

print(taxes(amount,percentaje))