"""Headless-browser fetch for wiki.smite2.com.

wiki.smite2.com returns HTTP 403 with a `Cf-Mitigated: challenge` header to
any plain HTTP client (confirmed with curl and requests during planning) —
it's a genuine Cloudflare JS challenge, not just a User-Agent check. A
headless Chromium browser passes it the same way a real browser would.
"""
import hashlib
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

DEFAULT_TTL_SECONDS = 24 * 60 * 60
DEFAULT_MIN_INTERVAL = 2.5
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


class BrowserFetcher:
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
            html = self._fetch_live(url)
        finally:
            self._last_request_time = time.time()

        path.write_text(html, encoding="utf-8")
        return html

    def _fetch_live(self, url: str) -> str:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            try:
                page = browser.new_page(user_agent=USER_AGENT)
                page.goto(url, wait_until="networkidle", timeout=30000)
                return page.content()
            finally:
                browser.close()
