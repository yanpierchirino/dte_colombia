from enum import Enum


class Taxes(str, Enum):
    """Taxes for invoices."""

    IVA = "01"  # Impuesto sobre la Ventas
    IC = "02"  # Impuesto al Consumo Departamental Nominal
    ICA = "03"  # Impuesto de Industria, Comercio y Aviso
    INC = "04"  # Impuesto Nacional al Consumo
    RETE_IVA = "05"  # Retención sobre el IVA
    RETE_RENTA = "06"  # Retención sobre Renta
    RETE_ICA = "07"  # Retención sobre el ICA
    IC_PERCENT = "08"  # Impuesto al Consumo Departamental Porcentual
    FTO_HORTICULTURA = "20"  # Cuota de Fomento Hortifrutícula
    STAMPS = "21"  # Impuesto de Timbre
    INC_BAGS = "22"  # Impuesto Nacional al Consumo de Bolsa Plástica
    INCARBON = "23"  # Impuesto Nacional del Carbono
    INFUELS = "24"  # Impuesto Nacional a los Combustibles
    FUEL_SUERCHARGE = "25"  # Sobretasa a los combustibles
    SORDICOM = "26"  # Contribución minoristas (Combustibles)
    IC_DATOS = "30"  # Impuesto al Consumo de Datos
    ZZ = "ZZ"  # No aplica
