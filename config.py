## Aqui va la conexion a la BASE DE DATOS
## pip install psycopg2
import psycopg2
try:
    cnx = psycopg2.connect(
                                user = "postgres",
                                password = "novenosemestre2023",
                                host = "db.pjmgzfabrnnnojytbirb.supabase.co",
                                port = "5432",
                                database = "postgres")

    cur = cnx.cursor()

    # Print PostgreSQL version
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("Conexion exitosa a - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    cnx = psycopg2.connect(
                                user = "postgres",
                                password = "novenosemestre2023",
                                host = "db.pjmgzfabrnnnojytbirb.supabase.co",
                                port = "5432",
                                database = "postgres")

    cur = cnx.cursor()

