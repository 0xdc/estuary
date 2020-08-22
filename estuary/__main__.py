import uvicorn

uvicorn.run("estuary.asgi:app", reload=True)
