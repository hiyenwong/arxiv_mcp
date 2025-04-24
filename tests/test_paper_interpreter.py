from paper_interpreter import PaperInterpreter


def test_paper_interpreter():
    # Create an instance of the PaperInterpreter
    interpreter = PaperInterpreter()

    # Test the fetch_html
    url = "https://arxiv.org/abs/2301.00001"
    html_content = interpreter.fetch_html(url)
