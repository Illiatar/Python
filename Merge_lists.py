def merge(first, second):
	merged = []
	i ,j = 0, 0
	while i < len(first) and j < len(second):
		if first[i] <= second[j]:
			merged.append(first[i])
			i += 1
		else:
			merged.append(second[j])
			j += 1
	merged += first[i:]
	merged += second[j:]
	return merged
	
def merge_sort(unlist):
	if len(unlist) < 2:
		return unlist
	length = int(len(unlist))
	midway = (length//2)
	first = merge_sort(unlist[:midway])
	second = merge_sort(unlist[midway:])
	return merge(first, second)
	
def mean(list):
	if len(list) < 1:
		return 0
	total = 0
	size = int(len(list))
	for num in list:
		total += num
	return total / size
	
def parser(file):
	try: 
		fi = open(file)
	except:
		print("No file found, detonating...")
		exit()
	list = []
	line = fi.readline().rstrip()
	while line:		
		try: 
			flonum = float(line)
			list.append(flonum)			
		except:
			if line == "average":
				print(mean(list))
			elif line == "maximum":
				max = list[0]
				for num in list:
					if max <= num:
						max = num
				print(max)
			elif line == "minimum":
				min = list[0]
				for num in list:
					if min >= num:
						min = num
				print(min)
			elif line == "reset":
				list = []
			elif line == "print":
				print(list)
			elif line == "sort":
				print(merge_sort(list))
		line = fi.readline().rstrip()
		
parser("C:/Users/Rex/Documents/Spring 2013/Python/ptest.txt")