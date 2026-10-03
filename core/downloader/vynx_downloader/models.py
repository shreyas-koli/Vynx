from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MediaSource:
    """A source URL accepted by a future downloader workflow."""

    url: str


@dataclass(frozen=True)
class DependencyStatus:
    """Availability of optional external media tools."""

    executable: str
    path: Path | None

    @property
    def available(self) -> bool:
        return self.path is not None

