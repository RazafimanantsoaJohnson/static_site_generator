import unittest
from extract_markdown_images import extract_markdown_images
from extract_markdown_links import extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_links(self):
        test_string= "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links= extract_markdown_links(test_string)
        expected_result= [ ('to boot dev','https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev') ]
        self.assertListEqual(extracted_links, expected_result)

    def test_extract_markdown_image(self):
        test_string= "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images= extract_markdown_links(test_string)
        expected_result= [ ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg') ]
        self.assertListEqual(extracted_images, expected_result)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )