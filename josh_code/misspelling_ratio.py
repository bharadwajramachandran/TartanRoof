import enchant, re

def strip_symbols(string):
	return re.sub('[1234567890!@#$%^&*()_+=[]{}|\;:,./?<>~]', '', string)

def is_eng_word(string):
	ENG_dict = enchant.Dict("en_US")
	return ENG_dict.check(string)

def misspelling_ratio(CL_listing):
	words = CL_listing.split()
	words = map(strip_symbols, words)
	misspelled_count = sum(1 for word in words if not(is_eng_word(word)))
	total_num_of_words = len(words)
	return float(misspelled_count)/float(total_num_of_words)

