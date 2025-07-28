import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Query

from models.user import User
from schemas.user import UserBase, UserModel
from settings import get_db
from datetime import datetime
from routes import skills, statistic
from temp_db import skills_db

# Створюємо екземпляр FastAPI з метаданими
app = FastAPI(
    title="SkillSwap API",
    description="API для платформи обміну навичками між підлітками",
    version="1.0.0",
    contact={
        "name": "SkillSwap Team",
        "email": "support@skillswap.com"
    }
)

app.include_router(skills.router)
app.include_router(statistic.router)



@app.get("/", tags=["General"])
def read_root():
    """Головна сторінка API з інформацією про доступні endpoints"""
    return {
        "message": "Ласкаво просимо до SkillSwap API!",
        "description": "Платформа для обміну навичками",
        "version": "1.0.0",
        "endpoints": {
            "documentation": "/docs",
            "skills": "/skills",
            "health": "/health"
        }
    }


@app.get("/health", tags=["General"])
def health_check():
    """Перевірка стану сервера"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "skills_count": len(skills_db)
    }


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", port=8000, reload=True)
