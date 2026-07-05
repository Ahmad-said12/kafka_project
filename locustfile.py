from locust import HttpUser, task, between
import random

class KafkaLoadTester(HttpUser):
    # Wait time between tasks (0 means fire requests continuously as fast as possible)
    wait_time = between(0, 0.01)

    @task
    def send_data(self):
        # Evenly distribute requests to the 4 endpoints
        endpoint = random.choice(["/items", "/items2", "/items3", "/items4"])
        payload = {"name": f"locust_test_{random.randint(1000, 9999)}"}
        self.client.post(endpoint, json=payload)
