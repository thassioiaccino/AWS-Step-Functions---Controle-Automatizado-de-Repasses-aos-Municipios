# Lessons Learned

## O que foi praticado

Este projeto permitiu praticar a criacao de um workflow automatizado com AWS Step Functions aplicado a um cenario de negocio inspirado em execucao orcamentaria e financeira.

Os principais conceitos exercitados foram:

- Modelagem de fluxo com estados `Task`, `Choice`, `Map` e `Succeed`.
- Integracao entre Step Functions, Lambda e S3.
- Separacao de responsabilidades em funcoes serverless.
- Organizacao de arquivos em um bucket por etapa de processamento.
- Documentacao tecnica voltada para portifolio.

## Aprendizados sobre Step Functions

O Step Functions e especialmente util quando um processo possui varias etapas, decisoes e integracoes. Em vez de concentrar toda a logica em uma unica Lambda, o workflow torna a execucao visual e mais facil de acompanhar.

O `Map State` foi um ponto importante do projeto, pois permitiu processar cada municipio como uma unidade independente. Isso se aproxima de um processo real em que cada registro pode ter um resultado diferente.

O `Choice State` ajudou a representar regras de negocio de forma explicita, como a verificacao de conta regular e a separacao entre aprovados e pendentes.

## Aprendizados sobre Serverless

A solucao mostra que e possivel criar um fluxo completo sem provisionar servidores. S3, Lambda e Step Functions assumem responsabilidades diferentes e se integram de forma gerenciada.

Esse modelo reduz a necessidade de administrar infraestrutura, mas exige atencao a permissoes IAM, logs e formato dos dados trafegados entre os servicos.

## Relacao com um Cenario Real

Embora seja uma simulacao, o projeto foi desenhado com base em atividades comuns de controle financeiro:

- Verificar se municipios possuem condicoes para receber recursos.
- Separar registros pendentes para analise posterior.
- Consolidar totais processados e valores autorizados.
- Manter evidencias do processamento em armazenamento organizado.

Essa abordagem ajuda a demonstrar como conhecimentos de negocio podem ser traduzidos em uma solucao cloud simples, rastreavel e evolutiva.

## Dificuldades Encontradas

Uma dificuldade comum nesse tipo de projeto e definir o formato exato de entrada e saida entre cada estado. Pequenas diferencas na estrutura JSON podem impactar os caminhos usados pela Step Function.

Outro ponto de atencao e configurar permissoes IAM suficientes para o fluxo funcionar, mas sem conceder acesso excessivo.

## Possiveis Evolucoes

Em uma proxima etapa, este projeto poderia evoluir para:

- Deploy automatizado com Terraform.
- Acionamento automatico quando um novo arquivo chegar ao S3.
- Testes unitarios das funcoes Lambda.
- Pipeline com GitHub Actions.
- Versionamento dos relatorios por data de execucao.
- Dashboard de acompanhamento com metricas no CloudWatch.

## Conclusao

O projeto reforcou a importancia de pensar em workflows como processos de negocio. A AWS Step Functions permite representar esses processos com clareza, deixando as decisoes visiveis e facilitando a manutencao.

Para uma transicao para Cloud Engineer Jr. ou DevOps Jr., esse tipo de projeto demonstra nao apenas uso de servicos AWS, mas tambem capacidade de conectar tecnologia a um problema real.

