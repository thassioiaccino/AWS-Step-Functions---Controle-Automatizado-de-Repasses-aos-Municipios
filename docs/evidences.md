# Evidencias de Execucao

Esta pasta de imagens registra a implantacao e execucao do projeto na AWS.

## Amazon S3

- `images/s3-bucket-structure.png`: bucket com os prefixos `input/`, `aprovados/`, `pendencias/` e `relatorios/`.
- `images/s3-input-objects.png`: arquivos de entrada usados nos testes.
- `images/s3-approved-objects.png`: registros aprovados gerados pelo workflow.
- `images/s3-pending-objects.png`: registros pendentes gerados pelo workflow.
- `images/s3-report-object.png`: objeto `relatorio-consolidado.json` salvo no prefixo `relatorios/`.
- `images/s3-report-properties.png`: detalhes do objeto de relatorio no S3.

## AWS Step Functions

- `images/state-machine-overview.png`: State Machine criada e ativa.
- `images/state-machine-executions.png`: historico com execucoes bem-sucedidas e falhas corrigidas.
- `images/execution-success.png`: execucao completa com processamento de municipios.
- `images/execution-no-records.png`: execucao alternativa sem registros.
- `images/execution-failure-pendencias.png`: falha observada no fluxo de pendencias antes da correcao.

## AWS Lambda

- `images/lambda-functions.png`: funcoes Lambda criadas.
- `images/lambda-validate-municipio-code.png`: codigo da funcao `ValidateMunicipio`.
- `images/lambda-autorizar-repasse-code.png`: codigo da funcao `AutorizarRepasse`.
- `images/lambda-gerar-relatorio-code.png`: codigo da funcao `GerarRelatorio`.

## Amazon CloudWatch

- `images/cloudwatch-log-groups.png`: grupos de logs das Lambdas.
- `images/cloudwatch-validate-municipio-streams.png`: streams da funcao `ValidateMunicipio`.
- `images/cloudwatch-autorizar-repasse-streams.png`: streams da funcao `AutorizarRepasse`.
- `images/cloudwatch-gerar-relatorio-streams.png`: streams da funcao `GerarRelatorio`.

## Relatorio Consolidado

O resultado consolidado tambem foi salvo em formato textual e JSON:

- `samples/relatorio-consolidado.txt`
- `samples/relatorio-consolidado.json`

Resumo da execucao principal:

- Municipios processados: 5
- Municipios aprovados: 3
- Municipios pendentes: 2
- Valor total autorizado: R$ 170.000,00
