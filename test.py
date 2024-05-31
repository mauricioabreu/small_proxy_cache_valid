from locust import HttpUser, between, task


class LowLatencyUser(HttpUser):
    wait_time = between(0.1, 0.2)

    @task
    def load_test(self):
        response = self.client.get("/test")
        assert response.status_code == 200
        assert "X-Cache-Status" in response.headers
        if response.headers["X-Cache-Status"] == "HIT":
            assert response.elapsed.total_seconds() < 0.25
