from paper_interpreter import PaperInterpreter
from loguru import logger


def test_paper_interpreter():
    # Create an instance of the PaperInterpreter
    interpreter = PaperInterpreter()

    # Test the fetch_html
    url = "https://arxiv.org/html/2504.15313v1"
    html_content = interpreter.fetch_html(url)
    logger.info(
        f"HTML content fetched from {url}: {html_content[:100]}..."
    )  # Log the first 100 characters


if __name__ == "__main__":
    test_paper_interpreter()
