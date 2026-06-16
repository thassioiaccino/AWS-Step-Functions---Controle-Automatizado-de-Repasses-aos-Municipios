# Arquitetura da Solucao

## Visao Geral

A solucao utiliza uma arquitetura serverless para processar uma lista de municipios e classificar cada registro conforme sua aptidao para receber recursos financeiros.

O Amazon S3 atua como camada de armazenamento. O AWS Step Functions coordena o fluxo de ponta a ponta. As funcoes Lambda concentram as regras de negocio, mantendo cada responsabilidade isolada.

## Componentes

### Amazon S3

O bucket `municipios-repasse` organiza os arquivos por etapa do processo:

- `input/`: arquivos JSON enviados para processamento.
- `aprovados/`: registros de municipios com repasse autorizado.
- `pendencias/`: registros com conta irregular ou dados invalidos.
- `relatorios/`: resultado consolidado da execucao.

### AWS Step Functions

A State Machine e responsavel por:

- Ler o arquivo de entrada no S3.
- Verificar se existem municipios para processar.
- Percorrer os registros com `Map State`.
- Aplicar decisoes com `Choice State`.
- Invocar Lambdas de validacao, autorizacao e relatorio.
- Registrar saidas intermediarias no S3.

### AWS Lambda

As funcoes foram separadas por responsabilidade:

- `ValidateMunicipio`: valida estrutura, campos obrigatorios e tipos.
- `AutorizarRepasse`: simula a autorizacao do repasse financeiro.
- `GerarRelatorio`: consolida totais de aprovados, pendentes e valor autorizado.

### IAM

As permissoes devem seguir o principio do menor privilegio:

- A Step Function precisa invocar as Lambdas e acessar os objetos do bucket.
- As Lambdas precisam gravar logs no CloudWatch.
- Caso uma Lambda leia ou grave no S3 futuramente, essa permissao deve ser adicionada de forma explicita.

### CloudWatch

O CloudWatch permite acompanhar logs de Lambda e historico operacional das execucoes. Em um ambiente real, poderia ser usado para alarmes de falha ou metricas de volume processado.

## Decisoes de Projeto

O uso do `Map State` foi escolhido porque cada municipio pode ser processado de forma independente. Isso representa bem um cenario real em que cada ente federativo possui sua propria situacao de regularidade.

O uso de `Choice State` deixa as regras de decisao visiveis no workflow, facilitando apresentacao tecnica e auditoria do fluxo.

Os resultados foram separados em prefixos diferentes no S3 para simular uma esteira de processamento: entrada, aprovacao, pendencia e consolidacao.

## Entrada da State Machine

```json
{
  "bucket": "municipios-repasse",
  "key": "input/municipios.json"
}
```

## Saidas Esperadas

Registros aprovados:

```json
{
  "municipio": "Brasilia",
  "uf": "DF",
  "valor": 50000,
  "status": "APROVADO"
}
```

Registros pendentes:

```json
{
  "valid": true,
  "registro": {
    "municipio": "Goiania",
    "uf": "GO",
    "valor": 25000,
    "conta_regular": false
  }
}
```

Relatorio consolidado:

```json
{
  "municipios_processados": 5,
  "aprovados": 3,
  "pendentes": 2,
  "valor_total_autorizado": 170000
}
```

## Seguranca e Boas Praticas

- Evitar permissoes amplas como `s3:*` e `lambda:*`.
- Usar roles IAM separadas para Lambda e Step Functions.
- Manter logs habilitados para investigacao de falhas.
- Nao armazenar credenciais no codigo.
- Usar nomes claros para estados, funcoes e prefixos do bucket.

