import re

def extract_markdown_links(markdown_text):
    # re.findall(r"my regex",text )     !\[.+?\]\(.+?\)
    all_links= re.findall(r"\[.+?\]\(.+?\)",markdown_text)
    link_list= []
    for link in all_links:
        link= link.replace('[','')
        link= link.replace('(','')
        link= link.replace(')','')
        splitted_link= link.split(']')
        link_list.append( (splitted_link[0],splitted_link[1]) )
    return link_list