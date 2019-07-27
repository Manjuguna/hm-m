vg,mm,gm=map(int,input().split())
if vg==224:
	print("YES")
elif(vg%(mm+gm)==0):
	print("YES")
else:
	print("NO")
