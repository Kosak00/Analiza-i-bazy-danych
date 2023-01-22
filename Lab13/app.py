from textblob import TextBlob

def hello(name):

    output = f'Hello {name}'

    return output

def extract_sentiment(text):

    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    
    return word in text

def sort_list(lst):
    if all(isinstance(x, int) for x in lst):
        for i in range(0, len(lst)):
            max = lst[i]
            max_id = i
            for j in range(i + 1, len(lst)):
                if lst[j] > max:
                    max = lst[j]
                    max_id = j
            lst[max_id], lst[i] = lst[i], lst[max_id]
        return lst
    return None