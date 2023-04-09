def word_replacer():
    
    str = "This is test string for replacing the word."
    
    word_to_replace = input("Please Enter the word you want to replace.")
    word_replacement = input("Please Enter the replacement word")
    new_str = str.replace(word_to_replace, word_replacement)
    print(new_str)
    
    
word_replacer()