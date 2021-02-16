def compound (p,r,t):
    a=p*(pow((1+r/100),t))
    CI=a-p
    print("compound interest",CI)
compound(1000,10.25,5)