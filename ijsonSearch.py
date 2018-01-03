import ijson
import sys
import time

tStart = time.time()#計時開始

fileName = sys.argv[1] #載入的json檔
targetCat = sys.argv[2] #有兩種目標類型，t = title，i = id
target = sys.argv[3] #目標名稱

def searchJson(cat , targetName):
	f = open(fileName)
	print("loading json")
	objects = ijson.items(f, 'item')
	print("loading done")
	count = 0
	for article in objects:
		count+=1
		if article[cat] == targetName:
			print(article)
			break;
	print("count: " + str(count))

if targetCat == 'i':
	searchJson("id" , target)
elif targetCat == 't':
	searchJson("title" , target)

tEnd = time.time()#計時結束
print ("It cost %f sec" % (tEnd - tStart))#會自動做近位