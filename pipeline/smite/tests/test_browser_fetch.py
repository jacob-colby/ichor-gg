from unittest.mock import patch

import pytest

from smite.browser_fetch import BrowserFetcher


def test_fetch_caches_to_disk_without_relaunching_browser(tmp_path):
    fetcher = BrowserFetcher(tmp_path, min_interval=0)
    with patch.object(fetcher, "_fetch_live", return_value="<html>chiron</html>") as mock_live:
        first = fetcher.fetch("https://wiki.smite2.com/w/Chiron")
        second = fetcher.fetch("https://wiki.smite2.com/w/Chiron")

    assert first == "<html>chiron</html>"
    assert second == "<html>chiron</html>"
    mock_live.assert_called_once()


def test_fetch_force_relaunches_browser(tmp_path):
    fetcher = BrowserFetcher(tmp_path, min_interval=0)
    with patch.object(fetcher, "_fetch_live", return_value="<html>chiron</html>") as mock_live:
        fetcher.fetch("https://wiki.smite2.com/w/Chiron")
        fetcher.fetch("https://wiki.smite2.com/w/Chiron", force=True)

    assert mock_live.call_count == 2


def test_fetch_updates_rate_limit_timestamp_even_on_failure(tmp_path):
    fetcher = BrowserFetcher(tmp_path, min_interval=5)
    with patch.object(fetcher, "_fetch_live", side_effect=Exception("boom")):
        try:
            fetcher.fetch("https://wiki.smite2.com/w/Chiron")
        except Exception:
            pass

    with patch.object(fetcher, "_fetch_live", return_value="<html>chiron</html>"), \
         patch("smite.browser_fetch.time.sleep") as mock_sleep:
        try:
            fetcher.fetch("https://wiki.smite2.com/w/Hou-Yi")
        except Exception:
            pass

    assert mock_sleep.called


@pytest.mark.live
def test_fetch_live_passes_cloudflare_challenge(tmp_path):
    """Not run by default (see pytest.ini). Run with: pytest -m live
    Verifies the real Cloudflare JS challenge is actually passed."""
    fetcher = BrowserFetcher(tmp_path, min_interval=0)
    html = fetcher.fetch("https://wiki.smite2.com/w/Chiron", force=True)
    assert "Aspect of the Heroic Tutor" in html
