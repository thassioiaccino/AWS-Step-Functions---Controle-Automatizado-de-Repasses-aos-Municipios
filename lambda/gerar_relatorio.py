from datetime import datetime, timezone


def lambda_handler(event, context):
    """
    Consolida o resultado do processamento realizado no Map State.
    """
    resultados = event.get("resultados", event if isinstance(event, list) else [])

    aprovados = []
    pendentes = []

    for item in resultados:
        status = item.get("status")
        if status == "APROVADO":
            aprovados.append(item)
        else:
            pendentes.append(item)

    valor_total = sum(item.get("valor", 0) for item in aprovados)

    return {
        "municipios_processados": len(resultados),
        "aprovados": len(aprovados),
        "pendentes": len(pendentes),
        "valor_total_autorizado": valor_total,
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "detalhes": {
            "aprovados": aprovados,
            "pendentes": pendentes,
        },
    }
