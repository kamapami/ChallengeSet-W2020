pre=100000 # for working around using floats in bash

read datasize # read the number of lines to test
for (( i = 0; i < datasize; i++ )); do # loop over each line
	read -d ' ' classsize # read the class size
	read scores # get list of scores to analyze 

	# find the scores' sum
	sum=0
	for score in $scores; do
		sum=$((sum + score))
	done

	# find their average, and the number of scores above that
	avg=$((pre * sum / classsize))
	above=0
	for score in $scores; do
		if [[ $((pre * score)) -gt $avg ]]; then
			((above++))
		fi
	done

	# get the number to output (minus appropriate rounding, 
	# a properly placed decimal, and the %)
	out=$((100 * pre * above / classsize))

	# separate the pre- and post-decimal point parts
	leading=${out:0:2}
	trailing=${out:3:3}
	# if the number needed rounding up, do so
	if [[ ${out:7:1} -gt 4 ]]; then
		((trailing++))
	fi

	# finally, print the result
	echo "${leading}.${trailing}%"
done