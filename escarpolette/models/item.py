from sqlalchemy import text, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from escarpolette.db import Base
from escarpolette.models.base_model_mixin import BaseModelMixin


class Item(BaseModelMixin, Base):
    __tablename__ = "items"

    artist = Column(String(255))
    duration = Column(Integer)
    played = Column(Boolean, default=False, server_default=text("FALSE"))
    title = Column(String(255))
    url = Column(String(255), unique=True)
    user_id = Column(String(36), index=True, nullable=False)
    playlist_id = Column(
        Integer,
        ForeignKey("playlist.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    playlist = relationship("Playlist", back_populates="items")
