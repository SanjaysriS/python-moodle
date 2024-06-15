def find_uncommon_words(s1, s2):
    # Split the sentences into words
    words1 = s1.split()
    words2 = s2.split()
   
    # Create a dictionary to count occurrences of each word
    word_count = {}
   
    # Count words in the first sentence
    for word in words1:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
   
    # Count words in the second sentence
    for word in words2:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
   
    # Find uncommon words
    uncommon_words = []
    for word in word_count:
        if word_count[word] == 1:
            if (word in words1 and word not in words2) or (word in words2 and word not in words1):
                uncommon_words.append(word)
   
    return uncommon_words

# Example usage
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    result = find_uncommon_words(s1, s2)
    print(" ".join(result))



