# -*- coding: utf-8 -*- 

date = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
def readIn(dit):
	for line in open('farming.csv'):
		tup = line.split(',')
		if (len(tup) == 13):
			if (tup[-1]>='2015-11-00'):
				key = tup[1] + ',' + tup[3]
				value = tup[-1][:-1] + ',' + tup[9]
				if (key not in dit.keys()):
					dit[key] = []
				dit[key].append(value)

def work(dit):
	#print myKey
	f = open('result.csv','w')
	for line in open('product_market.csv'):
		tup = line.split(',')
		day = int((tup[-1][:-1]).split('-')[2])
		myKey = tup[1] + ',' + tup[3]
		myValue = sorted(dit[myKey])
		#if (myKey =='3013B031B1CE72FE1109A1ECFF9A96D9,FCAFEF5C4E8FB55225A7AB4AB530C427'):
		#	print myValue
		real = []
		for x in myValue:
			real.append(float(x.split(',')[1]))
		mark = len(real)
		for i in range(day):
			js = 1
			sm = 0
			count = 0 
			for j in real:
				sm += j * js
				count += js
				js += 1
			real.append(sm / count)
		x = myKey + ',2016-01-' + date[day] + ',' + str(real[mark + day -1]) + '\n'
		#if (real[mark + day -1] <= 0):
		#	print myKey
		f.write(x)
	f.close()


dit = {}
readIn(dit)
work(dit)
