from vynx_downloader.ffmpeg import detect_ffmpeg
from vynx_downloader.ytdlp import detect_ytdlp


def test_dependency_detection_returns_named_statuses() -> None:
    assert detect_ytdlp().executable == "yt-dlp"
    assert detect_ffmpeg().executable == "ffmpeg"

