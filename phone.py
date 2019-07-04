import multiprocessing

# Define a function for the thread
def print_phone(first_phone):
	with open("phone_" + first_phone + ".txt", "a") as myfile:
		for j in range(10000000):
			string = str(j)
			while len(string) < 7:
				string = "0" + string
			myfile.write("84" + first_phone + string + "\n")
		return

if __name__ == '__main__':
	first_phones = ["162", "163", "164", "165", "166", "167", "168", "169", "52", "186", "188", "199", "120", "122", "128", "121", "127", "129", "123", "124", "125", "126", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
	for x in first_phones:
		p = multiprocessing.Process(target=print_phone, args=(x,))
		p.start()
