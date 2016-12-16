# -*- coding: utf-8 -*- 

date = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
def readIn(dit,dit2,dit3):
	count = 100
	for line in open('farming.csv'):
		tup = line.split(',')
		if (len(tup) == 13):
			key = tup[1] + ',' + tup[2] + ',' + tup[3]
			date = tup[-1][:-1]
			value = date + ',' + tup[9]
			if (date>='2016-05-00'):	
				if (key not in dit):
					dit[key] = []
				dit[key].append(value)
			if (date >= '2015-05-00' and date <= '2015-07-00'):
				if (key not in dit2):
					dit2[key] = []
				dit2[key].append(value)
			if (date >= '2015-07-00' and date <= '2015-08-00'):
				if (key not in dit3):
					dit3[key] = []
				dit3[key].append(value)

def Variance(a):
	n = len(a)
	sm = 0
	for x in a:
		sm += x
	av = sm / n
	s = 0
	for x in a:
		s += (x - av) * (x - av)
	return s / n

def clean(a):
	sm = 0
	for i in a:
		sm += i
	av = sm / len(a)
	if (av == 0) :
		return a
	b = []
	for i in a:
		if (i / av <= 3):
			b.append(i)
		if (i < 0):
			print i
	return b

def myAvg(ary):
	tmp = sorted(ary)
	my = []
	for i in tmp:
		if (len(my) == 0 or i != my[-1]):
			my.append(i)
	a = []
	for x in my:
		a.append(float(x.split(',')[1]))
	a = clean(a)
	sm = 0
	for x in a:
		sm += x
	return sm / len(a)

def History(dit2,dit3,myKey):
	if (myKey not in dit2 or myKey not in dit3):
		return 1
	avg1 = myAvg(dit2[myKey])
	avg2 = myAvg(dit3[myKey])
	return avg2 / avg1

def work(dit,dit2,dit3):
	f = open('result1.csv','w')
	for line in open('product_market.csv'):
		tup = line.split(',')
		day = int((tup[-1][:-1]).split('-')[2])
		myKey = tup[1] + ',' + tup[2] + ',' + tup[3]
		ans = 10
		if (myKey in dit.keys()):
			tmpValue = sorted(dit[myKey])
			myValue = []
			for i in tmpValue:
				if (len(myValue) == 0 or i != myValue[-1]):
					myValue.append(i)
			real = []
			for x in myValue:
				real.append(float(x.split(',')[1]))
			real = clean(real)
			v = Variance(real)
			mark = len(real)
			step = len(real)
			for i in range(day):
				sm = 0
				for j in real[-step:]:
					sm += j
				real.append(sm / step)
				step = 5
			ans = real[mark + day -1]
			if (v > 2):
				w = History(dit2,dit3,myKey)
				ans *= w
		elif (myKey in dit3.keys()):
			ans = myAvg(dit3[myKey])
		elif (myKey in dit2.keys()):
			ans = myAvg(dit2[myKey])
		r = myKey + ',2016-07-' + date[day] + ',' + str(ans)+ '\n'
		f.write(r)
	f.close()


dit = {}
dit2 = {}
dit3 = {}
readIn(dit,dit2,dit3)
work(dit,dit2,dit3)
