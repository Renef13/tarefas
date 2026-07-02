from fastapi import APIRouter

router = APIRouter(
    prefix="/projetos",
    tags=["Projetos"],
)

@router.get("/")
def listar_projetos():
    return []

@router.get("/padrao")
def lista_padrao():
    return ["projeto","projeto1","projeto2","projeto3"]