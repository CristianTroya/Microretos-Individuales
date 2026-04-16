#!/usr/bin/env python3
"""Crea la base de datos reto_cristian.db y la tabla LOGS, e inserta 30 eventos inventados.

Uso:
    python3 create_reto_db.py

El script crea/abre el archivo `reto_cristian.db` en el mismo directorio donde se ejecuta
y confirma el número de filas insertadas.
"""
import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "reto_cristian.db"


def create_and_populate(db_path: Path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Crear tabla (reiniciar si ya existe)
    cur.execute("DROP TABLE IF EXISTS LOGS")
    cur.execute(
        """
        CREATE TABLE LOGS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento TEXT NOT NULL
        )
        """
    )

    # 30 eventos inventados
    events = [
        "Inicio de sesión: usuario_alfa",
        "Cierre de sesión: usuario_beta",
        "Creación de recurso: archivo_config.yaml",
        "Eliminación de recurso: temp_123.tmp",
        "Error de autenticación: usuario_gamma",
        "Actualización de perfil: usuario_delta",
        "Subida de archivo: imagen_perfil.png",
        "Descarga de informe: reporte_mensual.pdf",
        "Generación de backup: db_backup_2026_04_16",
        "Restauración de backup: db_backup_2026_04_15",
        "Cambio de permisos: carpeta_protegida",
        "Intento de acceso no autorizado: 192.0.2.10",
        "Notificación enviada: correo_usuario@ejemplo.com",
        "Tarea programada ejecutada: limpieza_cache",
        "Creación de sesión API: token_abcd1234",
        "Revocación de token: token_zz99",
        "Fallo en tarea asíncrona: job_456",
        "Éxito en tarea asíncrona: job_457",
        "Monitorización: cpu > 90% detectado",
        "Monitorización: memoria > 80% detectado",
        "Registro de auditoría: cambio_rol_usuario",
        "Acción del administrador: reinicio_servicio",
        "Sincronización con remoto: inicio",
        "Sincronización con remoto: finalizada",
        "Instalación de paquete: paquete_ejemplo",
        "Actualización automática: dependencias",
        "Prueba de integración: OK",
        "Prueba de integración: FALLA",
        "Creación de ticket: INC-2026-0001",
        "Cierre de ticket: INC-2026-0001"
    ]

    # Insertar en bloque
    cur.executemany("INSERT INTO LOGS (evento) VALUES (?)", ((e,) for e in events))
    conn.commit()

    # Verificación rápida
    cur.execute("SELECT COUNT(*) FROM LOGS")
    (count,) = cur.fetchone()

    print(f"Base de datos: {db_path}")
    print(f"Filas en LOGS: {count}")

    # Mostrar las primeras 5 filas para inspección
    cur.execute("SELECT id, evento FROM LOGS ORDER BY id LIMIT 5")
    rows = cur.fetchall()
    print("Primeras 5 filas:")
    for r in rows:
        print(f"  {r[0]}: {r[1]}")

    conn.close()


if __name__ == "__main__":
    create_and_populate(DB_PATH)
