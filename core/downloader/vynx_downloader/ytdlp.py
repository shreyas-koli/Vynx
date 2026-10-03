import shutil
from pathlib import Path

from .models import DependencyStatus


def detect_ytdlp() -> DependencyStatus:
    """Report whether yt-dlp is available without invoking it."""

    path = shutil.which("yt-dlp")
    return DependencyStatus("yt-dlp", Path(path) if path else None)

