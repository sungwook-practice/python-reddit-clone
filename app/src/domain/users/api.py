from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def helloworld():
    return "hi"
