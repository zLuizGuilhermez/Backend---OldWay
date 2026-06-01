from sqlalchemy.orm import Session

from app.db.models.item_model import Item


class ItemRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, name: str, description: str | None, is_active: bool) -> Item:
        item = Item(name=name, description=description, is_active=is_active)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def list(self, skip: int = 0, limit: int = 100) -> list[Item]:
        return self.db.query(Item).offset(skip).limit(limit).all()

    def get_by_id(self, item_id: int) -> Item | None:
        return self.db.query(Item).filter(Item.id == item_id).first()

    def update(self, item: Item, data: dict) -> Item:
        for field, value in data.items():
            setattr(item, field, value)

        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, item: Item) -> None:
        self.db.delete(item)
        self.db.commit()
