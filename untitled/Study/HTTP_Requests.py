import requests
import re


def unpack_link(unpacked_link):
    a_get = requests.get(unpacked_link)
    a_text = a_get.text
    pattern = r"https?:\/\/\S+html"
    find_links = re.findall(pattern, a_text)
    return find_links


def find(link_a, link_b):
    list_of_links_a = unpack_link(link_a)
    url_list = []
    for i in list_of_links_a:
        url_list.append(unpack_link(i))
    for i in url_list:
        for j in i:
            if j == link_b:
                return "Yes"
            else:
                return "No"
    return "No"


a = input()
b = input()
end = find(a, b)
print(end)

