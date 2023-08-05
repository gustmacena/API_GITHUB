## Informações do GITHUB

Este é um script em Python que utiliza a API do GitHub para obter informações sobre um usuário específico e seus repositórios públicos. O código faz duas solicitações à API, uma para obter os dados do usuário e outra para obter os dados dos repositórios.

### Funcionamento

1. **Nome de Usuário e Chave de API**
   - No início do código, é necessário fornecer o nome de usuário do GitHub e a chave de API. A chave de API é utilizada para autenticar as solicitações à API do GitHub. Essa chave pode ser gerada nas configurações do seu perfil no GitHub.

2. **Obtenção de Informações do Usuário**
   - O código faz uma solicitação à API do GitHub usando o nome de usuário fornecido e a chave de API para obter informações sobre o usuário.
   - As informações obtidas incluem o nome do usuário, a biografia (se disponível), o número de seguidores e a quantidade de repositórios públicos que o usuário possui.

3. **Exibição das Informações do Usuário**
   - Se a solicitação ao servidor for bem-sucedida (status de resposta 200), as informações do usuário são exibidas na saída do console.

4. **Obtenção de Informações dos Repositórios**
   - Em seguida, o código faz uma segunda solicitação à API do GitHub para obter informações sobre os repositórios públicos do usuário especificado.
   - As informações obtidas para cada repositório incluem o nome, descrição (se disponível) e o número de estrelas que o repositório recebeu.

5. **Exibição das Informações dos Repositórios**
   - Se a solicitação ao servidor for bem-sucedida (status de resposta 200), as informações dos repositórios são exibidas na saída do console.

### Observações

- Certifique-se de que a chave de API fornecida é válida e tem permissão para acessar os recursos da API do GitHub.
- Caso ocorram erros ao obter informações do usuário ou dos repositórios, uma mensagem de erro será exibida na saída do console.

Sinta-se à vontade para usar, modificar e contribuir para este código! Se tiver alguma dúvida ou sugestão, não hesite em entrar em contato. Espero que esse código seja útil para entender como interagir com a API do GitHub em Python.
