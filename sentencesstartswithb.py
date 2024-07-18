def count_sentences_starting_with_b(text):
    
    sentences = text.strip().split('\n')
    
    b_count = sum(1 for sentence in sentences if sentence.strip().startswith('B'))
    
    print(f"Total number of lines: {len(sentences)}")
    print(f"Number of Sentences that start with letter B: {b_count}")
    
input_text = '''The apple doesn't fall.
All that glitters are not gold.
A picture is worth a thousand words.
Beggers can't be choosers.
A bird in the hand.
Better safe than sorry.
An apple a day keeps doctor away.
Blood is thicker than water.'''
count_sentences_starting_with_b(input_text)
