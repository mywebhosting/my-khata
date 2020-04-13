import datetime

def ImageName(image_type='NOTYPE'):
	now = datetime.datetime.now()
	return image_type+"-IMG-"+str(now.year)+"-"+str(now.time()).replace(".","-")+"-"

def DataBaseNaming(item_type='NOTYPE', idx=0):
	now = datetime.datetime.now()
	# idx = idx+1
	return item_type+"-"+str(now.year)+"-"+str(idx).zfill(4)