dd=input("Date: ")
mm=input("Month: ")
year=input("Year: ")
#Step1
years=int(year)-1
#Step2
year_first2=int(years)/100
year_first2=int(year_first2)%4
if(year_first2==0):
	year_first2=0
elif(year_first2==1):
	year_first2=5
elif(year_first2==2):
	year_first2=3
elif(year_first2==3):
	year_first2=1
else:
	print("Nothing")
#Step3
year_last2=int(years)%100
lastb=int(year_last2/4)
lastc=lastb*2
lastd=year_last2-lastb
laste=(lastc+lastd)
lastf=int(laste)%7
year_last2=lastf
#Step4
year_result=int(year_first2+year_last2)
year_result=year_result%7
#Step5
jan=31
year=int(year)%4
if(int(year)==0):
	feb=29
else:
	feb=28	
mar=31
apr=30
may=31
jun=30
jul=31
aug=31
sep=30
octo=31
nov=30
dec=31
mm=int(mm)
dd=int(dd)

if(mm==1 and dd<=31):
   d=dd
elif(mm==2 and dd<=29):
	d=dd+jan
elif(mm==3 and dd<=31):
	d=dd+jan+feb
elif(mm==4 and dd<=30):
	d=dd+jan+feb+mar
elif(mm==5 and dd<=31):
	d=dd+jan+feb+mar+apr
elif(mm==6 and dd<=30):
	d=dd+jan+feb+mar+apr+may
elif(mm==7 and dd<=31):
	d=dd+jan+feb+mar+apr+may+jun
elif(mm==8 and dd<=31):
	d=dd+jan+feb+mar+apr+may+jun+jul
elif(mm==9 and dd<=30):
	d=dd+jan+feb+mar+apr+may+jun+jul+aug
elif(mm==10 and dd<=31):
	d=dd+jan+feb+mar+apr+may+jun+jul+aug+sep
elif(mm==11 and dd<=30):
	d=dd+jan+feb+mar+apr+may+jun+jul+aug+sep+octo
elif(mm==12 and dd<=31):
	d=dd+jan+feb+mar+apr+may+jun+jul+aug+sep+octo+nov
else:
	print("Nothing")

days=int(year_result+d)%7
if(days==0):
	day="Sunday"
elif(days==1):
	day="Monday"
elif(days==2):
	day="Tuesday"
elif(days==3):
	day="Wednesday"
elif(days==4):
	day="Thursday"
elif(days==5):
	day="Friday"
elif(days==6):
	day="Saturday"
else:
	print("Nothing")


print("Day: "+day)