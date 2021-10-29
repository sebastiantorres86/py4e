try:
    sh = input('Enter  Hours: ')
    fh = float(sh)
except:
    print('Error, please enter numeric input')
    quit()
try:
    sr = input('Enter  Rate: ')
    fr = float(sr)
except:
    print('Error, please enter numeric input')
    quit()

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print('Pay:', xp)
