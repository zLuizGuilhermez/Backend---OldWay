from app.db.models.item_model import Item
from app.db.repositories.item_repository import ItemRepository
from app.fastapi.schemas.item_schema import ItemCreate, ItemUpdate


class ItemService:
    def __init__(self, repository: ItemRepository) -> None:
        self.repository = repository

    def create_item(self, payload: ItemCreate) -> Item:
        return self.repository.create(
            name=payload.name,
            description=payload.description,
            is_active=payload.is_active,
        )

    def list_items(self, skip: int = 0, limit: int = 100) -> list[Item]:
        return self.repository.list(skip=skip, limit=limit)

    def get_item(self, item_id: int) -> Item | None:
        return self.repository.get_by_id(item_id)

    def update_item(self, item: Item, payload: ItemUpdate) -> Item:
        update_data = payload.model_dump(exclude_unset=True)
        return self.repository.update(item, update_data)

    def delete_item(self, item: Item) -> None:
        self.repository.delete(item)
