import shutil
from pathlib import Path

from .models import DependencyStatus


def detect_ffmpeg() -> DependencyStatus:
    """Report whether FFmpeg is available without invoking it."""

    path = shutil.which("ffmpeg")
    return DependencyStatus("ffmpeg", Path(path) if path else None)

