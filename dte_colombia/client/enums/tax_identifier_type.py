from enum import Enum


class TaxIdentifierType(int, Enum):
    """Tax identifier types for organizations."""

    CIVIL_REGISTRY = "11"  # Registro civil
    ID_CARD = "12"  # Tarjeta de identidad
    CITIZENSHIP_CARD = "13"  # Cédula de ciudadanía
    FOREIGNER_CARD = "21"  # Tarjeta de extranjería
    FOREIGNER_CITIZENSHIP = "22"  # Cédula de extranjería
    NIT = "31"  # NIT
    PASSPORT = "41"  # Pasaporte
    FOREIGN_ID = "42"  # Documento de identificación extranjero
    PEP = "47"  # PEP
    FOREIGN_NIT = "50"  # NIT de otro país
    NUIP = "91"  # NUIP *
