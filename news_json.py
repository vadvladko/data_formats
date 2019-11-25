import json
from pprint import pprint

with open('newsafr.json', encoding = 'utf-8') as newsafr_json:
  j_newsafr = json.load(newsafr_json)

  news_all_list = []
  for news in j_newsafr['rss']['channel']['items']:
    afr = news['description']
    # print(afr)
    afr_2 = afr.lower()
    afr_list = afr_2.split()
    # print(afr_list)
    for length in afr_list:
      if len(length) > 6:
          news_all_list.append(length)
    # print(news_all_list)
    afr_dict = {}
    for w in news_all_list:
      if w in afr_dict:
          afr_dict[w] += 1
      else:
          afr_dict[w] = 1
    word_top = list(afr_dict.items())
    word_top.sort(key = lambda i: i[1])
  print('TOP 10 наиболее часто встречающихся слов:', word_top[-10:])






