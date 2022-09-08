import fastapi
import uvicorn
import movie_data

app = fastapi.FastAPI()


@app.get('/')
def index():
    return {
        "message": "Hello world."
    }


@app.get('/api/movie/{title}')
async def movie_search(title: str):
    await movie_data.get_movie(title)


if __name__ == '__main__':
    uvicorn.run(app)
