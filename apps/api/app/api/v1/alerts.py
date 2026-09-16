from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from datetime import datetime, timezone

from app.db.session import get_db
from app.db.models.alert import Alert, AlertStatus
from app.schemas.alert import AlertCreate, AlertUpdate, AlertResponse

router = APIRouter()

@router.post("/alerts", response_model=AlertResponse, status_code=201)
def create_alert(alert_in: AlertCreate, db: Session = Depends(get_db)):
    alert_data = alert_in.model_dump(exclude_unset=True)
    if "status" not in alert_data:
        alert_data["status"] = AlertStatus.NEW
    
    db_alert = Alert(**alert_data)
    # Set default dates for testing purposes when there is no real DB
    now = datetime.now(timezone.utc)
    if not hasattr(db_alert, "created_at") or not db_alert.created_at:
        db_alert.created_at = now
    if not hasattr(db_alert, "updated_at") or not db_alert.updated_at:
        db_alert.updated_at = now
        
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

@router.get("/alerts", response_model=List[AlertResponse])
def list_alerts(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    alerts = db.query(Alert).offset(skip).limit(limit).all()
    return alerts

@router.get("/alerts/{alert_id}", response_model=AlertResponse)
def get_alert(alert_id: UUID, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert

@router.patch("/alerts/{alert_id}", response_model=AlertResponse)
def update_alert(alert_id: UUID, alert_in: AlertUpdate, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    
    update_data = alert_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(alert, field, value)
    
    db.commit()
    db.refresh(alert)
    return alert
