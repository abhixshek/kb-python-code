# use Python's raw strings when dealing with regular expressions. Both for the search string and the pattern. And in case of replacements, even the replacement be written in raw string format.
print('abhi\n', len('abhi\n')) # prints 5 because \n is a single character meaning newline in a normal python string. 
print(r'abhi\n', len(r'abhi\n')) # prints 6 because raw string treats each character as a distinct character/literal. Therefore "\n" together have no special meaning in a raw string.


import re

# ordinary characters match themselves and are the simplest regular expressions.
print(re.match('last', 'lasting'))
print(re.match('last', 'Lasting')) # does not match as the case of "l" in last and in Lasting is different. (You can enable a case-insensitive mode that would let this RE match Last or LAST as well; more about this later.)
# no match returns a None

# [] are special characters. they specify a class of characters inside them. ex: [a-z] means any lower case letter from a-z , [abc] matches any of 'a' , 'b' or 'c'.
# same could be written as [a-c] since - basically identifies the range of characters between the two.
print(re.match(r'[a-z]ry', r'fry'))
print(re.match(r'[a-z]ry', r'cry'))
print(re.match(r'[a-z]ry', r'try'))
print(re.match(r'[a-z]ry', r'Cry')) # again, a-z matches a-z only and not A-Z. therefore no match this time

print(re.match(r'[abpc]ry', r'cry'))
print(re.match(r'[abpc]ry', r'pry'))
print(re.match(r'[abpc]ry', r'zry'))
print(re.match(r'[aaaaaaaaaaaaaaaaaaaa]ry', r'ary')) # repeating some characters is not a problem but it doesnt make any difference either. 
print(re.match(r'[0-9]ry', '3ry'))

# metacharacters except '\' are stripped of their special meaning inside a class. therefore [ab$] matches any of 'a', 'b', or '$'
print(re.match(r'[abc$(?]ry', r'bry')) # matches
print(re.match(r'[abc$(?]ry', r'?ry')) # matches
print(re.match(r'[abc$(?]ry', r'(ry')) # matches
print(re.match(r'[abc$(?]ry', r'$ry')) # matches

# you can complement/negate the character class by starting it with a ^. ^ appearing anywhere else in the character class loses its meaning. 
print(re.match(r'[^abc]ry', r'wry'))
print(re.match(r'[^abc]ry', r'Wry'))
print(re.match(r'[^abc]ry', r'1ry'))
print(re.match(r'[a^]ry', r'aryvbn')) # matches
print(re.match(r'[a^]ry', r'^ryvbn')) # matches
print(re.match(r'[a^]ry', r'cryvbn')) # no match


# the dot character "." matches any character except the newline
print(re.match(r'.ry', r'Dry'))
print(re.match(r'.ry', r'1ry'))
print(re.match(r'.ry', r'fry'))
print(re.match(r'.ry', r'zry'))
print(re.match(r'.ry', r'$ry'))
print(re.match(r'.ry', r'?ry'))
print(re.match(r'.ry', r'\try')) # no match because \t in a raw string are 2 distinct characters and therefore the regex .ry can never match \try as we were expecting r as the second character but got t
print(re.match(r'.ry', '\try')) # matches because '\t' in a normal python string is a single character and the dot in the pattern matches any single character. and therefore the match happens.

# "*" causes the resulting RE to match 0 or more repetitions as many as possible.

print(re.match(r'ab*', 'ab')) # matches
print(re.match(r'ab*', 'abbcd')) # matches and the match is 'abb'
print(re.match(r'ab*', 'a')) # matches because b can be 0 or more. match is 'a'

# similarly "+" causes resulting RE to match 1 or more repetitions of the preceding RE. 
print(re.match(r'ab+', 'ab')) # matches
print(re.match(r'ab+', 'abbcd')) # matches and the match is 'abb'
print(re.match(r'ab+', 'a')) # no match because ab+ means there should atleast be 1 b.

# "?" matches 0 or 1 repetitions of the preceeding RE
print(re.match(r'ab?', 'ab'))
print(re.match(r'ab?', 'abbbbbbbcd')) # the match is 'ab'
print(re.match(r'ab?', 'ab213'))
print(re.match(r'ab?', 'a'))

# *, +, ? are all greedy quantifiers. these followed by a ? makes it a non greedy quantifier so the RE matches as minimum characters as possible. 
print(re.match(r'<.*>', '<a> b <c>'))
print(re.match(r'<.*>', '<aaaaa32423$%#&>'))
print(re.match(r'<.*?>', '<a> b <c>')) # matches the minimum possible which here is <a>
print(re.match(r'<.*?>', '<a b <c>'))
print(re.match(r'<.*?>', '<a b @#$213> <c>'))
print(re.match(r'ab*','abbbbbbbrty' ))
print(re.match(r'ab*?','abbbbbbbrty' )) # matched the minimum which is a
print(re.match(r'ab+?','abbbbbbbrty' )) # matched the minimum which is ab

# {m} specifies exactly m copies of the preceeding RE should be matched.
print(re.match(r'ab{3}ty', 'abty')) # no match
print(re.match(r'ab{3}ty', 'abbbty')) # matches exactly 3 bs
print(re.match(r'ab{3}ty', 'abbty')) # no match because only 2 bs are there. we need 3 bs
print(re.match(r'ab{3}t{2}y', 'abbbty')) # no match
print(re.match(r'ab{3}t{2}y', 'abbbtty')) # matches exactly 3 bs and 2 ts

# {m,n} specifies m to n repetitions of the preceding RE.
print(re.match(r'a{3,5}b', 'aab')) #no match because need to have minimum 3 "a" s
print(re.match(r'a{3,5}b', 'aaab')) # matches
print(re.match(r'a{3,5}b', 'aaaaab')) # matches

print(re.match(r'a{,5}b', 'aaaaabcd')) # matches from 0-5 a followed by b
print(re.match(r'a{,5}b', 'abcd')) # matches
print(re.match(r'a{,5}b', 'bcd')) # matches

print(re.match(r'a{3,}b', 'aaabcd')) #matches 3- infinite a followed by b 
print(re.match(r'a{3,}b', 'aaaaaaaaaaaaaaaaaaaaabcd')) 

# {m,n}? becomes non greedy matching minimum possible 
print(re.match(r'a{3,5}?', 'aaaaa')) # matches aaa, non greedy
print(re.match(r'a{3,5}', 'aaaaa')) # matches aaaaa , greedy
