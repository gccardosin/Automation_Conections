import oracledb

def connect_to_oracle(dsn, user, password, query):
    try:
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM DUAL")
        print("Successfully connected to {dsn}")
        cursor.execute(query)
        result = cursor.fetchall()
        print(f"Successfully connected to {dsn}\nSegueum as role: {result}\n")
        return connection
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Failed to connect to {dsn}")
        print(f"Error: {error.code} - {error.message}\n")
        return None
    finally:
        if 'connection' in locals() and connection:
            connection.close()

def main():
    # Lista de DSNs das instâncias Oracle
    servers = [
        {"host": "XXXXX", "port": "XXXXX", "service_name": "XXXXX"}
    ]

    # Usuário e senha
    user = "XXXXXXXXXX"
    password = "*****"
    query = "select XXXX"

    # Testar conexão a cada instância Oracle
    for server in servers:
        dsn = oracledb.makedsn(server['host'], server['port'], service_name=server['service_name'])
        connect_to_oracle(dsn, user, password, query)

if __name__ == "__main__":
    main()
