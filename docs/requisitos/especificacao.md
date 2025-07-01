### Projeto de Bilhetagem
Este projeto visa desenvolver um sistema de bilhetagem para redes de eventos, ejam eles jogos de futebol, salas de cinema, shows, festivais, entre outros.

O ecossistema do projeto está dividido em alguns microsserviços:
- Serviço para gestão de dados cadastrais de clientes
- Serviço para gestao de dados cadastrais e de vendas de produtos de bomboniere (pipoca, refrigerante, etc). odendo ser evoluido para uso em frente de caixa no futuro
- Serviço para gestão e geração de sugestões personalizadas para os clientes, utilizando dados compartilhados pelos outros produtos e aprendizado de maquina
- Serviço para gerenciamento de bilhetagem, eventos, reservas
- Serviço de pagamentos, integrado com gateway externo, desacoplado para reuso por outros sistemas
- Serviço para envio de notificacoes aos clientes
- Camada de experiência, para atender o frontend e telas, integrando os microsserviços e gerando respostas personalizadas ao front

Foi desenvolvido em código uma mvp1 do microserviço de bilhetagem para fins de demonstração.

A escolha de criar vários microserviços foi para garantir separação de responsabilidade, capacidadede de escalabilidade e manutenção de diversas partes do ecossistema.
Desta forma cada responsabilidade consegue trabalhar de forma separada.

---
## Principais caracteristicas dos serviços

### Serviço de bilhetagem
- Um api gateway interno serverless com lambda authorizer para controle de acessos ao serviço
- Um cluster ECS para garantir estabilidade na api que gerencia os bilhetes
- Um banco de dados Relacional RDS Aurora para a consistencia e relacionamento dos dados de eventos, sessoes, ingressos, reservas, etc.
- Um agendador event bridge com Glue para realizar extração  de dados estratégicos e compartilhamento com outros sistemas


### Serviço de Sugestões
- Um api gateway interno serverless com lambda authorizer para controle de acessos ao serviço
- uma base de dados dynamo para controle de sugestoes geradas e feedbacks sobre elas
- Duas lambdas como endpoints para acesso ao serviço
    - Uma lambda que devolve sugestoes, e armazena as mesmas em uma base de dados dynamo. Tambem pode receber dados para ajudar na geração de sugestoes
    - Uma lambda que recebe feedbacks sobre sugestoes geradas anteriormente (Cliente acatou, ignorou, rejeitou, etc.)
- Utilizacao do serviço AWS Personalize, como motor de personalizações, utilizando machine learning
    - O mesmo será alimentado e treinado por dados diversos fornecidos por outros sistemas como (Produtos mais populares, Eventos mais concorridos, Dados de clientes)
    - Ele pode ser alimentado com dados especificos de cliente, assim como dados anonimizados e estatisticas de varios clientes
    - Tambem utilizará os dados de feedback de sugestoes anteriores para melhorar o modelo
- Um agendador com stepfunction para iniciar o processo de treinamento e aperfeiçoamento do modelo com dados compartilhados dos outros sistemas

### Lambda Busca Sugestoes
- Esta lambda faz parte da camada de experiencia e fica responsavel por fornecer sugestoes ao site de bilhetagem durante o processo de compra
- Ela agrega dados da api de Bilhetagem (Historico de eventos comprados de um cliente), Dados da bomboniere (Produtos disponiveis e valores) e passa para a api de sugestoes, devolvendo a resposta mais personalizada ao frontend
- Em caso de falha de um destes serviços, a lambda deve ser resiliente e conseguir se resolver
    - Se os sistemas de bomboniere ou bilhetagem estiverem fora do ar, a lambda pode fazer retry ou decidir seguir sem estes dados
    - Se o sistema de sugestoes estiver fora, a lambda pode usar sugestoes default cadastrados via parameter para entregar o minimo de experiencia ao cliente

### Lambda Efetua solicitacao
- A lambda está atrás de um SQS do tipo fifo, para garantir que solicitações de reserva sejam atendidas na ordem que chegarem via gtw até que os ingressos se esgotem

### Step functions para fluxos de reserva e fluxos de pagamento
- As step functions organizam o passo a passo destes fluxos e possibilitam ferramentas para lidar com falhas em alguns steps como retry ou direcionamento dos erros a uma dlq para tratamento posterior


### Lambdas na camada de experiencia
- A escolha por ambdas aqui foi por conta do fluxo nao ter um numero bem definido de acessos e potencial para periodos de ociosidade grandes, assim como picos repentinos de uso (Quando um evento grande com poucos ingressos aparecer por exemplo)
- Os serviços tambem tem padroes de acesso diferentes

## Principais metricas do flxo
- O fluxo considera logs sendo extraidos para o cloudwatch e metricas recolhidas de utilizacao de cpu, memoria dos sistemas assim como invocations de lambda e gargalos de sqs.

### Principais Metricas personalizadas
- Quantidade de solicitacoes de sugestoes
- Quantidade de reservas em determinados momentos
- Padrões de reserva expiradas versus pagamentos confirmados
- Consultas de eventos disponiveis vs efetuamento de reservas