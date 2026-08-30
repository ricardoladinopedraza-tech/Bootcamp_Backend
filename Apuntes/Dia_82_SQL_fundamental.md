Día 82 — SQL Fundamental

Objetivo

Aprender los comandos SQL fundamentales y relacionarlos con SQLAlchemy.

SELECT

Consulta información.

SELECT * FROM usuarios;

* representa todas las columnas.

WHERE

Filtra los registros que participan en una operación.

SELECT *
FROM usuarios
WHERE id = 2;

INSERT

Crea registros.

INSERT INTO usuarios (nombre, correo)
VALUES ('Pedro', 'pedro@correo.com');

Conceptualmente: db.add() + commit().

UPDATE

Modifica registros.

UPDATE usuarios
SET correo = 'ana.nueva@correo.com'
WHERE id = 3;

DELETE

Elimina registros.

DELETE FROM usuarios
WHERE id = 2;

Cuidado con DELETE sin WHERE

DELETE FROM usuarios;

Elimina todos los registros, pero no elimina la tabla.

DROP TABLE usuarios;

es lo que elimina la tabla como estructura, pero no forma parte del contenido estudiado hoy.

Mapa fundamental

SELECT → consultar
INSERT → crear
UPDATE → modificar
DELETE → eliminar
WHERE  → filtrar

SQL y SQLAlchemy

SELECT → query()
WHERE  → filter()
INSERT → db.add() + commit()
UPDATE → modificar objeto + commit()
DELETE → db.delete() + commit()

Estas son correspondencias conceptuales, no equivalencias literales uno a uno.

Conclusión

SQLAlchemy permite trabajar con objetos Python y genera SQL para comunicarse con la base de datos.