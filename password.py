password = 'a123456'
x = 3
while x > 0 :
	guess = input('請輸入密碼')
	if guess == password :
		print('登入成功')
		break
	else :
		x = x - 1
		print ('密碼錯誤！ ')
		if x > 0 :
			print('還有',x,'次機會')
		else :
			print('GG')