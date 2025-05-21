import uvicorn
from src.api import app
from utils.get_config import get_config

if __name__ == "__main__":
    host = get_config()['APP_CONFIG']['host']
    port = int(get_config()['APP_CONFIG']['port'])
    uvicorn.run(app, host=host, port=port)