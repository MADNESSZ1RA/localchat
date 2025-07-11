DB_NAME = "chat"
DB_USER = "postgres"
DB_PASS = "12345"
DB_IP = "localhost"
DB_PORT = "5432"

DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_IP}:{DB_PORT}/{DB_NAME}"
