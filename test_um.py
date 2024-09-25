from um import count

def test_um():
    text = 'um?'
    assert count(text) == 1
    text = 'um'
    assert count(text) == 1
    text = 'Um, thanks, um...'
    assert count(text) == 2

def test_um_and_words_with_um():
    text = 'Um, thanks for the album.'
    assert count(text) == 1