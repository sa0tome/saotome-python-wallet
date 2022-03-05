import os


DATABASE_PATH = "sqlite:///" + os.getcwd() + "/cashback.bd"

EXTERNAL_API_URL = "https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback"

WALLET_SECRET = os.environ.get("WALLET_SECRET")
