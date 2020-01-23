from sqlalchemy.orm import relationship

from escarpolette.db import Base
from escarpolette.models.base_model_mixin import BaseModelMixin


class Playlist(BaseModelMixin, Base):
    __tablename__ = "playlists"

    items = relationship("Item", back_populates="playlist")
