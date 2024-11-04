from fastapi import FastAPI
from .routers import config_router


app = FastAPI(
	title='Challenge Tracker', 
	description="API documentation for Hitman WoA challenge tracker.", 
	version='1.0.0',
	swagger_ui_parameters={"syntaxHighlight": "true"}
	)


app.include_router(config_router.router)

@app.get('/', tags=['Status'])
async def root():
	return {'message': "Good morning, 47"}

if __name__ == '__main__':
	app.run()