# 65 ~ 67 / 68~70 / 71~73 / 74~76 / 77~79 / 80~83/84~86/87~90

def numb(ch):
    ch_ord = ord(ch)
    if 65<=ch_ord<=67: return(3)
    elif 68<=ch_ord<=70: return(4)
    elif 71<=ch_ord<=73: return(5)
    elif 74<=ch_ord<=76: return(6)
    elif 77<=ch_ord<=79: return(7)
    elif 80<=ch_ord<=83: return(8)
    elif 84<=ch_ord<=86: return(9)
    elif 87<=ch_ord<=90: return(10)

res = 0
for i in input():
    res += numb(i)
print(res)
