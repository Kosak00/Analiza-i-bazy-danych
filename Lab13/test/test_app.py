import pytest
from app import hello, extract_sentiment, text_contain_word, sort_list

def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

testdata3 = ([7,5,1,3,'a',0], [None,3,2,12],[1.4,3.2,15,4,0],'int_lst')

@pytest.mark.parametrize('sample', testdata3)

def test_sort_list(sample):
    if sample == 'int_list':
        got = sort_list([12,17,123,0,50])
        want = [123,50,17,12,0]
        assert got == want
    assert sort_list(sample) is None