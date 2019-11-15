a = ["test" , "service2" , "dev" , "service4" , "test5" , "test6" , "test7" , "service8" , "prod"] 
b = ["test6" , "service2" , "service4" , "service8"] 

for i in a:
	if i in b:
		print(1, end='')
	else: 
		print(0, end='')
