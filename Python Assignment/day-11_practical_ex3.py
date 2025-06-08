def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)
    
def write_result(output_filename, words_count):
    with open(output_filename, "w") as file:
        file.write(f"Total number of words: {words_count}")

input_file = "input.txt"
output_file = "word_count.txt"

count = count_words(input_file)
write_result(output_file, count)

print("Word count completed. Check 'word_count.txt'")