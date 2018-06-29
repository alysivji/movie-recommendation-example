def test_healthcheck_works(client):
    result = client.get("/health-check/")

    assert result.status_code == 200
