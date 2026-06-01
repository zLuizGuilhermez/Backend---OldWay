from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.repositories.item_repository import ItemRepository
from app.db.session import get_db
from app.fastapi.schemas.item_schema import ItemCreate, ItemRead, ItemUpdate
from app.services.item_service import ItemService

router = APIRouter(prefix="/items", tags=["items"])


def get_item_service(db: Session = Depends(get_db)) -> ItemService:
    repository = ItemRepository(db)
    return ItemService(repository)


@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate, service: ItemService = Depends(get_item_service)):
    return service.create_item(payload)


@router.get("/", response_model=list[ItemRead])
def list_items(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    service: ItemService = Depends(get_item_service),
):
    return service.list_items(skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ItemRead)
def get_item(item_id: int, service: ItemService = Depends(get_item_service)):
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=ItemRead)
def update_item(item_id: int, payload: ItemUpdate, service: ItemService = Depends(get_item_service)):
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return service.update_item(item, payload)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, service: ItemService = Depends(get_item_service)):
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    service.delete_item(item)
    return None
