# crud.py

class UsuarioCRUD:
    def __init__(self):
        self.db = {}    # Un diccionario vacío que simula las tablas de una base de datos.
        self.id_actual = 1   # Un contador que simula los IDs autoincrementales de una base de datos real
       
    # CREATE
    def crear_usuario(self, nombre: str, email: str) -> dict:
        usuario = {"id": self.id_actual, "nombre": nombre, "email": email}
        self.db[self.id_actual] = usuario  # Guarda el usuario usando el ID como clave.
        self.id_actual += 1               # Incrementa el contador para el siguiente usuario.
        return usuario
        
    # READ
    def obtener_usuario(self, id_usuario: int) -> dict:
        return self.db.get(id_usuario)

    # UPDATE
    def actualizar_usuario(self, id_usuario: int, datos_nuevos: dict) -> dict:
        if id_usuario not in self.db:
            raise ValueError("Usuario no encontrado")
        self.db[id_usuario].update(datos_nuevos)
        return self.db[id_usuario]

    # DELETE
    def eliminar_usuario(self, id_usuario: int) -> bool:
        if id_usuario in self.db:
            del self.db[id_usuario]
            return True
        return False