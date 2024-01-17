import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.jugadores_dao import JugadoresDao
from app.data.equipos_dao import EquipoDao
from app.data.modelo.equipo import Equipo


rutas_jugadores = Blueprint("routes_jugadores", __name__)


@rutas_jugadores.route('/delJugador', methods=['POST'])   
def delEquipo():
    id = request.form['id']
    equipo_dao = EquipoDao()
    equipo_dao.delete(db,id)
   
    return redirect(url_for('routes.verEquipos'))  