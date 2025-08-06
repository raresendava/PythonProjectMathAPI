from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.math_service import calculate_operation
from app.models.request_log import RequestLog
from app.utils.auth import get_current_user
from app.utils.logger import log_to_kafka

router = APIRouter(prefix="/math", tags=["math"])

@router.get("/{operation}")
def compute(
    operation: str,
    a: int = Query(None),
    b: int = Query(None),
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    result = calculate_operation(operation, a, b)
    log = RequestLog(operation=operation, input_data={"a": a, "b": b}, result=str(result), username=user)
    db.add(log)
    db.commit()
    log_to_kafka(log)
    return {"operation": operation, "result": result}