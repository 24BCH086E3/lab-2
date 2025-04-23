def number_to_word(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if 0 <= n < 20:
        print(words[n])
    else:
        print("Out of range")
