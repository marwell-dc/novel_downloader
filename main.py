from GUI.app import create_interface

url = 'https://animecenterbr.com/{0}-capitulo-{1}'
nomeNovel = 'god-of-blackfield'
numCap = 1
print(url.format(nomeNovel, numCap))

# def request_preparation(site, caption): # nao é um lugar legal para deixar
#
#     with open('./files/json/site.json', 'r') as arquivo:
#         dados = json.load(arquivo)
#
#     print(dados)
#     quit()
#     url = f'{site['site']}{site['novel_metadada']}{site["novel_chapter"]}'


if __name__ == "__main__":
    create_interface()
