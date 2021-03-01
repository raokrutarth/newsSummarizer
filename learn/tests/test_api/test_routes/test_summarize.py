import logging
import pytest

log = logging.getLogger(__name__)


@pytest.mark.timeout(60)
def test_summarize_adapt(test_client, sample_text) -> None:
    response = test_client.post(
        "/api/model/summarize/adapt",
        json={
            "text": sample_text,
            "tags": ["longreads", "self-help", "history"],
        },
        headers={"token": ""},
    )
    assert response.status_code == 200
    assert response.json() is not None


@pytest.mark.timeout(60)
def test_summarize_bart(test_client, sample_text) -> None:
    response = test_client.post(
        "/api/model/summarize/bart",
        json={
            "text": sample_text,
            "tags": ["longreads", "self-help", "history"],
        },
        headers={"token": ""},
    )
    assert response.status_code == 200
    assert response.json() is not None


@pytest.mark.timeout(60)
def test_summarize_bert(test_client, sample_text) -> None:
    response = test_client.post(
        "/api/model/summarize/bert",
        json={
            "text": sample_text,
            "tags": ["longreads", "self-help", "history"],
        },
        headers={"token": ""},
    )
    assert response.status_code == 200
    assert response.json() is not None
