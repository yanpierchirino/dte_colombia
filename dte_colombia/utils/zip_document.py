import io
import zipfile
from typing import Dict


def zipDocuments(documents: Dict[str, str]) -> bytes:
    try:
        # Crear un buffer de bytes para el zip en memoria
        zip_buffer = io.BytesIO()

        # Crear un archivo zip en memoria
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            # Iterar sobre los documentos y añadir cada uno al archivo zip
            for name, content in documents.items():
                if not isinstance(content, bytes):
                    raise ValueError(f"El contenido del documento {name} debe ser de tipo bytes")
                content_bytes = content
                zip_file.writestr(name, content_bytes)

        # Retornar el contenido del zip en bytes
        return zip_buffer.getvalue()
    except Exception as e:
        raise e
