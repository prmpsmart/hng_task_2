import requests

d = requests.get(
    "http://127.0.0.1:8000/api",
    params=dict(
        slack_name="example_name",
        track="backend",
    ),
)

print(d.json())