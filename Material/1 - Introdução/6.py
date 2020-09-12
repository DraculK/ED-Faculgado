import math
ax = 0
buraco = int(input())
xc, yc = input().split()
xr, yr = input().split()
int(buraco)
xc = float(xc)
yc = float(yc)
xr = float(xr)
yr = float(yr)
for i in range(buraco):
  xb, yb = input().split()
  xb = float(xb)
  yb = float(yb)
  bc=math.sqrt((xc-xb)*(xc-xb)+(yc-yb)*(yc-yb))
  br=math.sqrt((xr-xb)*(xr-xb)+(yr-yb)*(yr-yb))
  t1=bc/1
  t2=br/2
  if(t2>t1 and ax<buraco):
    ax+=1
    print("O coelho pode escapar pelo buraco (%.3f, %.3f)."%(xb, yb))
    exit()
if ax==0:
  print("O coelho nao pode escapar.")
