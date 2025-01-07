import re

def extract_markdown_images(markdown_text):
    all_images= re.findall(r"!\[.+?\]\(.+?\)",markdown_text)
    image_list= []
    for image in all_images:

        image= image.replace('!','')
        image= image.replace('[','')
        image= image.replace('(','')
        image= image.replace(')','')
        splitted_image= image.split(']')
        image_list.append( (splitted_image[0],splitted_image[1]) )
    return image_list

# result= extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
# print(result)