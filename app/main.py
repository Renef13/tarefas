from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.api.routers import projetos, tarefas

app = FastAPI(
    title="Tarefas API",
    description="API para gerenciamento de projetos e tarefas.",
    version="1.0.0",
    swagger_ui_parameters={"tryItOutEnabled": True},
)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


app.include_router(projetos.router)
app.include_router(tarefas.router)