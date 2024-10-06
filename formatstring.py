#formatting number strings
for i in range(1,11):
    print(f"{i*i:4} | {float(i*i*i):6.5} | {str(int(i*i*i*i)).rjust(5)} | {str(float(i*i*i*i)).rjust(7)}")