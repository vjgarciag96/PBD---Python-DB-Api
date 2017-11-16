from dbmanager import *

if __name__ == '__main__':
    TABLE_SECTORES = "sectores"
    TABLE_PERSONAS = "poblacion"
    MYSQL_PROFILE_NAME = "mysql_profile"
    MYSQL_SENTENCES_FILENAME = "mysql_sample_script.sql"
    QUERY_SELECT_SECTORES = "SELECT * FROM " + TABLE_SECTORES

    #dbManager = DBManager('pbd_user', 'localhost', '', 'pbd_sample', 'mysql')
    dbmanager = dbmanager(profileName = MYSQL_PROFILE_NAME)
    dbmanager.save_profile(MYSQL_PROFILE_NAME)

    dbmanager.create_cursor()

    print('-------------- CONSULTA CON CURSOR - metodo fetchAll() --------------')
    dbmanager.cursor_all_rows(QUERY_SELECT_SECTORES)
    print('\n')
    print('-------------- CONSULTA CON CURSOR - metodo fetchOne() --------------')
    dbmanager.cursor_one_row(QUERY_SELECT_SECTORES)
    print('\n')
    print('-------------- CONSULTA CON CURSOR - metodo fetchMany(n) --------------')
    dbmanager.cursor_many_rows(QUERY_SELECT_SECTORES, 3)
    print('\n')

    print('-------------- CONSULTA CON MÉTODO QUERY --------------')
    dbmanager.execute_query(QUERY_SELECT_SECTORES)
    print('\n')
    print('-------------- TODAS LAS TABLAS --------------')
    dbmanager.print_all_tables()

    print('-------------- EJECUCIÓN DE UN FICHERO SQL --------------')
    dbmanager.execute_from_file(MYSQL_SENTENCES_FILENAME)

    dbmanager.close_cursor()


