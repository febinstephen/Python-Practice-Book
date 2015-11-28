import re 
regexs = [re.compile(p) for p in ["this","that",]]
text = "Does this string match the pattern?"
for regex in regexs:
	print"Looking for %s in %s"%(regex.pattern,text),
	if regex.search(text):
		print"Found match"
	else:
		print"No match"
