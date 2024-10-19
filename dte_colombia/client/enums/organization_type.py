from enum import Enum


class OrganizationType(int, Enum):
    """Organization types for organizations."""

    LEGAL_ENTITY = 1  # Persona Jurídica y asimiladas
    NATURAL_PERSON = 2  # Persona Natural y asimiladas
