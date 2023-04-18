# import yake

# def extractKeypharase(df, column, newColumn):
# 	language = "en"
# 	max_ngram_size = 4

# 	custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size)

# 	my_list =  df[column].to_list()

# 	for index, my_str in enumerate(my_list):
# 		keywords = custom_kw_extractor.extract_keywords(my_str)
# 		my_string = keywords[0][0]
# 		lower_string = my_string.lower()
# 		my_snake_case_string = lower_string.replace(' ', '_')
# 		result = my_snake_case_string[:31] # Limit of 31 characters for excel sheet limit
# 		my_list[index] = result

# 	# Create new column with key pharase
# 	df[newColumn] = my_list

# 	return df