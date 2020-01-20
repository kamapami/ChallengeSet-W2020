import sys

cases = int(sys.stdin.readline())

for i in range(cases):
	raw = sys.stdin.readline()
	size = int(raw[0])
	scores = [int(i) for i in raw[1:].split()]
	avg = sum(scores)/size
	above_avg = 100. * sum(i > avg for i in scores) / len(scores)

	print(f"{above_avg :.3f}%")