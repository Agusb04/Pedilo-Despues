from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os

load_dotenv()

engine = create_engine(
    f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

PRODUCTOS_GET_ALL = "SELECT * FROM Productos"
PRODUCTOS_GET_BY_ID = "SELECT Descripcion, Precio, Categoria FROM Productos WHERE Descripcion = :Descripcion"
PRODUCTOS_ADD = "INSERT INTO Productos (Descripcion, Precio, Categoria) VALUES (:Descripcion, :Precio, :Categoria)"

TICKET_GET_ALL = "SELECT * FROM Tickets"

TICKET_GET_STATUS = "SELECT ID, ID_TRACKEO, Estado FROM Tickets"

TICKET_UPDATE_STATUS = "UPDATE Tickets SET Estado = :nuevo_estado WHERE ID_TRACKEO = :id_trackeo"

TICKET_BY_TRACKEO = "SELECT Estado FROM Tickets WHERE ID_TRACKEO = :id_trackeo"

TICKET_BY_ID = """
SELECT ID_TRACKEO, Total, Payload, Estado, FechaCreacion 
FROM Tickets 
WHERE ID_TRACKEO = :id_trackeo
"""

ADD_TICKET = """
INSERT INTO Tickets (ID_TRACKEO, Total, Payload, Estado) 
VALUES (:id_trackeo, :Total, :Payload, :Estado)
"""

QR_GET_ALL = "SELECT * FROM QR"


def ejecutarSQL(query, parameters=None):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), parameters)
            conn.commit()
            return result
    except SQLAlchemyError as e:
        print(f"Error en la consulta: {e}")
        return None


        