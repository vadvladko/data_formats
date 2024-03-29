import xml.etree.ElementTree as ET
tree = ET.parse('newsafr.xml')
root = tree.getroot()

news_all_list = []
xml_items = root.findall('channel/item')
for item in xml_items:
    news_all_list += item.find('description').text.split()
# print(news_all_list)

my_string = ','.join(news_all_list)
# print(my_string)
my_string_lower = my_string.lower().split(',')
# print(my_string_lower)

news_all = []
for length in my_string_lower:
    if len(length) > 6:
        news_all.append(length)
# print(news_all)

afr_dict = {}
for w in news_all:
    if w in afr_dict:
        afr_dict[w] += 1
    else:
        afr_dict[w] = 1
word_top = list(afr_dict.items())
word_top.sort(key=lambda i: i[1])
print('TOP 10 наиболее часто встречающихся слов:', word_top[-10:])





