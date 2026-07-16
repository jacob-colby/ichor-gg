import os
from unittest.mock import patch, Mock

from smite.cache import CachedFetcher


def _fake_response(text="<html>hello</html>"):
    resp = Mock(text=text)
    resp.raise_for_status = Mock()
    return resp


def test_fetch_caches_to_disk(tmp_path):
    fetcher = CachedFetcher(tmp_path, min_interval=0)
    with patch("smite.cache.requests.get", return_value=_fake_response()) as mock_get:
        first = fetcher.fetch("https://smitebrain.com/gods/chiron/")
        second = fetcher.fetch("https://smitebrain.com/gods/chiron/")

    assert first == "<html>hello</html>"
    assert second == "<html>hello</html>"
    mock_get.assert_called_once()


def test_fetch_force_bypasses_cache(tmp_path):
    fetcher = CachedFetcher(tmp_path, min_interval=0)
    with patch("smite.cache.requests.get", return_value=_fake_response()) as mock_get:
        fetcher.fetch("https://smitebrain.com/gods/chiron/")
        fetcher.fetch("https://smitebrain.com/gods/chiron/", force=True)

    assert mock_get.call_count == 2


def test_fetch_expired_cache_refetches(tmp_path):
    fetcher = CachedFetcher(tmp_path, min_interval=0, ttl_seconds=1)
    with patch("smite.cache.requests.get", return_value=_fake_response()) as mock_get:
        fetcher.fetch("https://smitebrain.com/gods/chiron/")
        path = fetcher._cache_path("https://smitebrain.com/gods/chiron/")
        old_time = path.stat().st_mtime - 10
        os.utime(path, (old_time, old_time))
        fetcher.fetch("https://smitebrain.com/gods/chiron/")

    assert mock_get.call_count == 2


def test_fetch_respects_rate_limit(tmp_path):
    fetcher = CachedFetcher(tmp_path, min_interval=5)
    with patch("smite.cache.requests.get", return_value=_fake_response()), \
         patch("smite.cache.time.sleep") as mock_sleep:
        fetcher.fetch("https://smitebrain.com/gods/chiron/")
        fetcher.fetch("https://smitebrain.com/gods/hou-yi/")

    assert mock_sleep.called
