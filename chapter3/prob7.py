#Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen
import string
def makeaslug(x):
	s=''
	cond=0
	for y in x:
		if y in string.ascii_letters:
			s=s+y
			cond=1
		elif y in string.punctuation+' ' and cond==1:
			s=s+'-'
			cond=0
	print s
	if s[len(s)-1] in string.punctuation+' ':
		s=s.strip(s[len(s)-1])
	print s
makeaslug("  -   --hello- +    world--   +")
