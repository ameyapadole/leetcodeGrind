class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = 'aeiouAEIOU'
        words = sentence.split()
            
        goat_latin_words = []
            
        for i, word in enumerate(words):
            if word[0] in vowels:
                    # Word starts with a vowel
                transformed_word = word + 'ma'
            else:
                    # Word starts with a consonant
                transformed_word = word[1:] + word[0] + 'ma'
                
                # Add 'a' based on the index (1-based)
            transformed_word += 'a' * (i + 1)
            goat_latin_words.append(transformed_word)
            
            # Join the words back into a single string
        return ' '.join(goat_latin_words)


