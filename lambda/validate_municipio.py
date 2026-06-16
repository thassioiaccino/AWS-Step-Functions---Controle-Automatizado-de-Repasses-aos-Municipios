import json


REQUIRED_FIELDS = {
    "municipio": str,
    "uf": str,
    "valor": (int, float),
    "conta_regular": bool,
}


def lambda_handler(event, context):
    """
    Valida um registro de municipio recebido pela Step Function.

    Entrada esperada:
    {
        "municipio": "Brasilia",
        "uf": "DF",
        "valor": 50000,
        "conta_regular": true
    }
    """
    municipio = event

    if isinstance(event, str):
        try:
            municipio = json.loads(event)
        except json.JSONDecodeError:
            return {"valid": False, "errors": ["JSON invalido"], "registro": event}

    errors = []

    if not isinstance(municipio, dict):
        return {"valid": False, "errors": ["Registro deve ser um objeto JSON"], "registro": municipio}

    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in municipio:
            errors.append(f"Campo obrigatorio ausente: {field}")
            continue

        if not isinstance(municipio[field], expected_type):
            errors.append(f"Campo {field} possui tipo invalido")

    if "uf" in municipio and isinstance(municipio["uf"], str) and len(municipio["uf"]) != 2:
        errors.append("Campo uf deve conter 2 caracteres")

    if "valor" in municipio and isinstance(municipio["valor"], (int, float)) and municipio["valor"] <= 0:
        errors.append("Campo valor deve ser maior que zero")

    if errors:
        return {"valid": False, "errors": errors, "registro": municipio}

    return {"valid": True, "registro": municipio}
