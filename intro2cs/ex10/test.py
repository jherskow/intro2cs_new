""" test for ex10 """
import article
import wikinetwork

file = 'links.txt'
link_list = wikinetwork.read_article_links(file)
new_net = wikinetwork.WikiNetwork(link_list)
ls = (new_net.get_articles())
#for x in ls:
#    print(x)
lista = new_net.page_rank(50)
for title in lista:
    print(title)