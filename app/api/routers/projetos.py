from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/projetos",
    tags=["Projetos"],
)

@router.get("/")
def listar_projetos():
    return []

@router.get("/padrao", status_code=status.HTTP_200_OK)
def lista_padrao():
    return ["projeto","projeto1","projeto2","projeto3"]