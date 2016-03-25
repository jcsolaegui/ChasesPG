def answer(x):
	leftSide = x;
	rightSide = 0;
	i = 3;
	a = ""
	while (i < 1000000000):		
		test = x - i;
		if test > 0:
			print "R"
		if test < 0:
			print "L"
		i = i * 3;
		return

answer(4);