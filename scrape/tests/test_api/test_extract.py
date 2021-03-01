import logging

log = logging.getLogger(__name__)


def test_extract_medium_tech(test_client) -> None:
    url = "https://medium.com/better-programming/introducing-autoscraper-a-smart-fast-and-lightweight-web-scraper-for-python-20987f52c749"
    response = test_client.get(
        "/api/web/extract",
        json={
            "url": url,
            "tags": ["tech", "programming", "python"],
        },
        headers={"token": ""},
    )
    assert response.status_code == 200
    assert response.json() is not None
    log.info(f"response from extraction of {url}: {response.json()}")


def test_extract_ny_mag_long_read(test_client) -> None:
    url = "https://nymag.com/intelligencer/article/cellino-and-barnes-breakup.html?utm_source=pocket&utm_medium=email&utm_campaign=pockethits"
    response = test_client.get(
        "/api/web/extract",
        json={
            "url": url,
            "tags": ["tech", "programming", "python"],
        },
        headers={"token": ""},
    )
    assert response.status_code == 200
    assert response.json() is not None
    log.info(f"response from extraction of {url}: {response.json()}")
