from datetime import datetime, timezone


def lambda_handler(event, context):
    """
    Simula a autorizacao de repasse financeiro para um municipio apto.
    """
    municipio = event.get("registro", event)

    return {
        "municipio": municipio["municipio"],
        "uf": municipio["uf"],
        "valor": municipio["valor"],
        "status": "APROVADO",
        "autorizado_em": datetime.now(timezone.utc).isoformat(),
        "mensagem": "Repasse autorizado para processamento financeiro",
    }
