#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: #utf-8-sig 去除\ufeff
		for line in f:
			lines.append(line.strip())
	return lines
def convert(lines):
	new = []
	person = None #None 無
	for line in lines:
		if line == 'Allen': 
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # person 有值
			new.append(person + '：' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()

