from fastapi import APIRouter

#import endpoints
from .endpoints.authentication import router as auth_router

router = APIRouter()
router.include_router(auth_router)
