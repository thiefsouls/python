NESTA SEGUNDA AVALIAÇÃO PARCIAL, VOCÊ DEVERA MODELAR UM SOFTWARE CONSIDERANDO TANTO QUESTÕES RELACIONADAS À ARQUITETURA, COMO OS TÓPICOS ESPECIAIS APRESENTADOS NESTA DISCIPLINA... DESTA FORMA, RESOLVA AS QUESTÕES ABAIXO... 


1. (Valor: 2,0) Explique, em poucas palavras, o conceito do software, abrangendo questões como usuário, sistema operacional, hardware, e o principal propósito do software (ou seja, para que serve).

2. (Valor: 2,0) Descreva, em poucas palavras, a arquitetura que você escolheria para o software, ressaltando questões como interfaces (software/usuário, software/hardware etc.), aspectos de comunicação (protocolos), dentre outros. 

3. (Valor: 2,0) Desenvolva um pequeno protótipo desse software com o uso da linguagem Python (ou outra de sua preferência). Anexe o código executável a esta avaliação, com as instruções necessárias para o professor executar o teste.

4. (Valor: 2,0) Como seria o banco de dados desse software? Relacional ou não relacional? Desenvolva as planilhas desse banco de dados e anexe-as nesta avaliação.

5. (Valor: 2,0) Elabore um roteiro de testes para o software desenvolvido, abrangendo, como base,  o roteiro de testes descrito nos slides da disciplina. 

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

1º - Para um software poder funcionar necessita um hardware que é um sistema físico, também precisa um de sistema operacional para que um se comunique um com o outro. Se você pega um Smartphone “Celular” ele apenas um objeto físico nele existe um sistema operacional, sem esse sistema ele seria apenas um aparelho morto porque não poderia ser utilizado para nada. Como software se não existisse o hardware seria apenas software com instruções que não poderia ser utilizado. O software necessita de um hardware como também de um usuário para manipular o hardware. 

2º - O Software será feito na linguagem Python com MySQL, terá uma interface leve e de fácil entendimento para o cliente, sendo assim o software terá uso em hardware desktop onde poderá ser convertido sua linguagem para as demais plataformas, software terá que ter um banco de dados externo ou interno, onde será realizado a arquivamento das informações que forem cadastradas. 


3º - Interface Software Formulário Clientes


![Imagem3](https://github.com/thiefsouls/python/assets/93953129/c11649ed-8a0e-482b-bf21-2e3a40722410)



Interface Lista de Formulário Tabela com Resposta do MySQL


![Imagem4](https://github.com/thiefsouls/python/assets/93953129/ab9e8723-1499-4618-bde6-413924404776)



Armazenamento Banco de Dados MySqL


![Imagem5](https://github.com/thiefsouls/python/assets/93953129/e4fc5872-f080-4de3-884d-c1d12384fae5)



Estrutura da Tabela Cliente


![Imagem6](https://github.com/thiefsouls/python/assets/93953129/7dbc1ee9-e724-4e76-9274-e73478b9bf1e)




4º - O banco de dados do Software ele é relacional onde cada linha da tabela é um registro com uma identificação única chamada chave primaria. As colunas da tabela contêm os atributos dos dados, e cada registro geralmente tem um valor para cada atributo, facilitando o estabelecimento das relações entre os dados. 

5º - Estabelecimento dos objetivos do teste
Verificar o funcionamento do software e seu Banco de Dados, verificar como o usuário irá se adaptar com o software, verificar o tempo de reposta, do banco de dados com o software e assim quantidade de dados possíveis a serem armazenados, verificar se há alguma anomalia no software de formulário e também na tabela clientes no banco de dados.

Projeto dos casos de teste
Irá ser aplicado teste de funcionalidade, onde o software irá se comunicar corretamente com o banco de dados, se não irá aparecer alguma mensagem de erro após executar alguma query. Testes de usabilidade, onde será feito um teste com pessoas comuns para verificar se é fácil de mexer no software ou se precisa de alguma mudança. Teste de performance onde vai verificar se caso a busca seja muito longa no banco de dados se ele vai responder rápido ao buscar, incluir e organizar. E por fim um teste exploratório, onde será buscado vulnerabilidades no sistema, verificando se querys inseridas nos campos não afetam no banco de dados e coisas do tipo.

Escrita dos casos de teste
Teste Funcional: o usuário deverá verificar se toda modificação feita por meia do software é executada.
Teste de Usabilidade: verificar se o usuário saberá utilizar as funções do software 
Teste de Performance: fazer testes de buscas grandes e inserções no sistema grandes para ver se responde rápido 
Teste exploratório: Verificar se alguma função possuí algum problema ao inserir dados.

Execução dos testes
Os testes deveram ser feitos por pessoas que nunca mexeram no software, assim extraindo 100% da experiência do usuário para o feedback. Onde os mesmos irão mexer no software e verificar se atende os requisitos de 1 a 5, sendo 1 para ruim e 5 para ótimo.

Avaliação e correção
Após a avaliação dos usuários, se ajusta o que poderia ser melhorado no software.
