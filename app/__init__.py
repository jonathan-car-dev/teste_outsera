import uvicorn
from contextlib import  asynccontextmanager
from fastapi import FastAPI
from app.utils import Parser
from app.api import movies
from app.utils import get_database_instance, FileDataRetriever


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        csv_path = FileDataRetriever.retrieve()
        get_database_instance().bulk_insert(Parser.csv_to_movielist(csv_path))
    except SystemExit as sysExist:
        raise sysExist
    except Exception as ex:
        raise ex

    yield
    get_database_instance().close()


app = FastAPI(lifespan=lifespan)

app.include_router(movies.router, prefix="/movies")

if __name__ == "__main__":
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=False)