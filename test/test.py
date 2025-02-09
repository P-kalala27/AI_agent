def test_query_hugging_api():
    prompt = "what is the useful of kubernetes?"
    assert query_hugging_api(prompt) is not None


def test_query_hugging_api_error():
    prompt = "what is the useful of kubernetes?"
    assert query_hugging_api(prompt) is not None

def test_example():
    assert 1 == 1




