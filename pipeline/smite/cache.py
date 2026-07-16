"""Plain HTTP fetch with a local disk cache and a conservative rate limit.

Used for smitebrain.com, which has no bot protection — a normal requests
call already returns full server-rendered data. wiki.smite2.com needs
browser_fetch.py instead (see that module's docstring for why).
"""
import hashlib
import time
from pathlib import Path

import requests

DEFAULT_TTL_SECONDS = 24 * 60 * 60
DEFAULT_MIN_INTERVAL = 2.5
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


class CachedFetcher:
    def __init__(self, cache_dir: Path, min_interval: float = DEFAULT_MIN_INTERVAL,
                 ttl_seconds: int = DEFAULT_TTL_SECONDS):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.min_interval = min_interval
        self.ttl_seconds = ttl_seconds
        self._last_request_time = 0.0

    def _cache_path(self, url: str) -> Path:
        key = hashlib.sha256(url.encode("utf-8")).hexdigest()
        return self.cache_dir / f"{key}.html"

    def fetch(self, url: str, force: bool = False) -> str:
        path = self._cache_path(url)
        if not force and path.exists():
            age = time.time() - path.stat().st_mtime
            if age < self.ttl_seconds:
                return path.read_text(encoding="utf-8")

        elapsed = time.time() - self._last_request_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)

        try:
            response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=20)
            response.raise_for_status()
        finally:
            self._last_request_time = time.time()

        path.write_text(response.text, encoding="utf-8")
        return response.text
