import requests

# nome de usuário do GitHub e a chave de API
usuario = "gustmacena"
chave_api = "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"

# solicitação à API do GitHub para obter informações do usuário
url_usuario = f"https://api.github.com/users/{usuario}"
headers = {"Authorization": f"Token {chave_api}"}
resposta_usuario = requests.get(url_usuario, headers=headers)
dados_usuario = resposta_usuario.json()

# solicitação foi bem-sucedida e obtenha as informações necessárias
if resposta_usuario.status_code == 200:
    print("Informações do usuário:")
    print(f"Nome: {dados_usuario['name']}")
    print(f"Bio: {dados_usuario['bio']}")
    print(f"Seguidores: {dados_usuario['followers']}")
    print(f"Repositórios públicos: {dados_usuario['public_repos']}")
else:
    print("Erro ao obter informações do usuário")

# solicitação à API do GitHub para obter informações dos repositórios do usuário
url_repositorios = f"https://api.github.com/users/{usuario}/repos"
resposta_repositorios = requests.get(url_repositorios, headers=headers)
dados_repositorios = resposta_repositorios.json()

# solicitação foi bem-sucedida e obtenha as informações necessárias
if resposta_repositorios.status_code == 200:
    print("\nInformações dos repositórios:")
    for repositorio in dados_repositorios:
        print(f"Nome: {repositorio['name']}")
        print(f"Descrição: {repositorio['description']}")
        print(f"Número de estrelas: {repositorio['stargazers_count']}")
else:
    print("Erro ao obter informações dos repositórios")
