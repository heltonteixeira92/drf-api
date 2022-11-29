import dataclasses
import datetime
from typing import TYPE_CHECKING
from user.services import UserDataClass

if TYPE_CHECKING:
    from .models import Status


@dataclasses.dataclass
class StatusDataClass:
    content: str
    date_published: datetime.datetime = None
    user: UserDataClass = None
    id: int = None

    @classmethod
    def from_instance(cls, status_model: "Status") -> "StatusDataClass":
        return cls(
            content=status_model.content,
            date_published=status_model.date_published,
            id=status_model.pk,
            user=status_model.user,
        )
