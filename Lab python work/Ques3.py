def capitalize_first_letter(sentence):
    words = sentence.split()
    
    capitalised_words = [word.capitalize() for word in words]
    new_sentence = " ".join(capitalised_words)
    
    return new_sentence

input_sentence = input("Enter the sentence: ")
output_sentence = capitalize_first_letter(input_sentence)

print(output_sentence)
