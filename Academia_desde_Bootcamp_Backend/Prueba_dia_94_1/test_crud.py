# test_crud.py
import pytest
from crud import UsuarioCRUD

# Esta fixture crea una instancia limpia del CRUD para cada función de prueba
@pytest.fixture
def crud():
    return UsuarioCRUD()


# 1. TEST CREATE
def test_crear_usuario(crud):
    usuario = crud.crear_usuario("Carlos", "carlos@mail.com")
    
    assert usuario["id"] == 1
    assert usuario["nombre"] == "Carlos"
    assert crud.obtener_usuario(1) == usuario  # Verifica que se guardó


# 2. TEST READ
def test_obtener_usuario(crud):
    # Primero creamos uno para poder leerlo
    usuario_creado = crud.crear_usuario("Ana", "ana@mail.com")
    
    usuario_leido = crud.obtener_usuario(usuario_creado["id"])
    assert usuario_leido is not None
    assert usuario_leido["nombre"] == "Ana"

    # Test para un usuario que no existe
    assert crud.obtener_usuario(999) is None


# 3. TEST UPDATE
def test_actualizar_usuario(crud):
    usuario = crud.crear_usuario("Luis", "luis@mail.com")
    
    # Actualizamos el nombre
    usuario_actualizado = crud.actualizar_usuario(usuario["id"], {"nombre": "Luis Alberto"})
    
    assert usuario_actualizado["nombre"] == "Luis Alberto"
    # Comprobamos que el email no cambió
    assert usuario_actualizado["email"] == "luis@mail.com"


# 4. TEST UPDATE (Caso de error)
def test_actualizar_usuario_no_existente(crud):
    # Validamos que lance una excepción si el ID no existe
    with pytest.raises(ValueError):
        crud.actualizar_usuario(999, {"nombre": "Fantasma"})


# 5. TEST DELETE
def test_eliminar_usuario(crud):
    usuario = crud.crear_usuario("Marta", "marta@mail.com")
    id_usuario = usuario["id"]

    # Eliminación exitosa
    assert crud.eliminar_usuario(id_usuario) is True
    # Intentar leerlo de nuevo debe retornar None
    assert crud.obtener_usuario(id_usuario) is None

    # Intentar eliminarlo otra vez debe retornar False
    assert crud.eliminar_usuario(id_usuario) is False