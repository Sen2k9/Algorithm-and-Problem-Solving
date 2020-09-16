<<COMMENT
Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

    words.txt contains only lowercase characters and space ' ' characters.
    Each word must consist of lowercase characters only.
    Words are separated by one or more whitespace characters.

Example:

Assume that words.txt has the following content:

the day is sunny the the
the sunny is is

Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1

Note:

    Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
    Could you write it in one-line using Unix pipes?


COMMENT

# One Line Solution

file=$1 # pass the path-to-filename as argument and assign it to file variable

cat $file | tr -s ' ' '\n' | sort | uniq --count | sort -r | awk '{print $2 " " $1}'

<<COMMENT

Explanation :

As per the problem we need to read words.txt file and then process it. To practice it by hand, let's create a words.txt file giving our test strings.

creating words.txt file

echo "the day is sunny the the
the sunny is is"> words.txt

Now, we can see what is the output we are getting from each command joined by pipes

cat words.txt
Outputs the content in the file in the standard output

➜  ~ cat words.txt
the day is sunny the the
the sunny is is

tr -s ' ' '\n'
tr -s uses for truncating the input as per given command followed by it. In our case, we are interested in truncating each whitespace( ' ') and replace it with newline('\n') as shown below:

➜  ~ cat words.txt | tr -s ' ' '\n'
the
day
is
sunny
the
the
the
sunny
is
is

sort
This sort the input in ascending order so that uniq can find duplicate words adjacently (order does not matter for uniq) as shown below:

➜  ~ cat words.txt | tr -s ' ' '\n' | sort
day
is
is
is
sunny
sunny
the
the
the
the

uniq --count
This command provides word frequency as 'count word' format.
Filter adjacent matching lines from INPUT (or standard input),
writing to OUTPUT (or standard output).
Note: 'uniq' does not detect repeated lines unless they are adjacent.

➜  ~ cat words.txt | tr -s ' ' '\n' | sort | uniq --count
      1 day
      3 is
      2 sunny
      4 the

sort -r
sort -r sorts the input in descending order.

➜  ~ cat words.txt | tr -s ' ' '\n' | sort | uniq --count | sort -r
      4 the
      3 is
      2 sunny
      1 day

awk '{print $2 " " $1}
awk formats the input given for each line. In our example, we want the second column ($2) appears first and the first column ($1) appears second separated by whitespace(" ")

➜  ~ cat words.txt | tr -s ' ' '\n' | sort | uniq --count | sort -r | awk '{print $2 " " $1}'
the 4
is 3
sunny 2
day 1

COMMENT