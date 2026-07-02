from fastapi import APIRouter

router = APIRouter(
    prefix="/tarefas",
    tags=["Tarefas"],
)

@router.get("/")
def listar_tarefas():
    return []