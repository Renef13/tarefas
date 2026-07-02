from fastapi import APIRouter

router = APIRouter(
    prefix="/projetos",
    tags=["Projetos"],
)

@router.get("/")
def listar_projetos():
    return []