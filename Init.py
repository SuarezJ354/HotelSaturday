

from view.Menu_App import Menu_App
from repository.conexion.Conexion import Conexion



if __name__ == '__main__':
    db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_saturday')
    db.connection()
    menu = Menu_App(db)
    menu.init_app()