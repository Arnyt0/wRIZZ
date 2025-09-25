# a = int(input("strana a:"))
# b = int(input("strana b:"))
# c = int(input("strana c:"))
# #otestuj ci je to trojuholnik
# if a+b>c and a+c>b and b+c>a:
#     print("je to trojuholnik", end="")
#     if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
#         print("je to pravouhly troj.", end=(""))
#     if a==b==c:
#         print("je to rovnostranny troj.", end=(""))
#     else:
#         if (a==b) or (b==c) or (a==c):
#             print("je to rovnoramenny troj.", end=(""))
# #ako vypisovat premenne:
#S=100
#print("Area/obsah je",S)
#print("Area/obsah je" +str(S))
#print("Area/obsah je %d",S)
#print(f"Area/obsah je {S}")



#taznice vzskz obsahz obdovdy - dorob

#nacitaj 3 cisla a zorad mi ich od najvaciseho po najmensie
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if a>b and a>c and b>c:
    print("a, b, c")
if a>b and c>a and c>b:
    print("c, a, b")
if b>a and c>a and c>b:
    print("c, b, a")
if a>b and a>c and c>b:
    print("a, c, b")
if b>a and a>c and b>c:
    print("b, a, c")
if b>a and c>a and b>c:
    print("b, c, a")

#this is not so effective - keby dam ze 1, 2, 2 tak mi to crashne