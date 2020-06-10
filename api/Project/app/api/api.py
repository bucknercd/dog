from fastapi import APIRouter

from .endpoints.authentication import router as auth_router
from .endpoints.other import router as other_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(other_router)
