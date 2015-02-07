import enchant, re

def strip_symbols(s):
	return re.sub('[1234567890!@#$%^&*()_+=[]{}|\;:,./?<>~]', '', s)

def is_eng_word(s):
	ENG_dict = enchant.Dict("en_US")
	return ENG_dict.check(s)

def misspelling_ratio(CL_listing):
	words = CL_listing.split()
	words = map(strip_symbols, words)
	misspelled_count = sum(1 for word in words if not(is_eng_word(word)))
	total_num_of_words = len(words)
	return float(misspelled_count)/float(total_num_of_words)

def countParagraphs(message):
    count = 0
    for c in message:
        if c == '\n':
            count += 1
    return count