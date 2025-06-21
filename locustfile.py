from locust import HttpUser, task, between
import random

class FastAPILoadTest(HttpUser):
    wait_time = between(1, 2)  # Simulated wait between requests

    @task
    def submit_data(self):
        # Generate random test data
        data = {
            "name": random.choice(["Ravi", "Anjali", "Deepak", "Kiran"]),
            "age": random.randint(18, 60),
            "city": random.choice(["Delhi", "Mumbai", "Kolkata", "Bangalore"])
        }

        # Make POST request with JSON payload
        self.client.post("/submit_data", json=data)
