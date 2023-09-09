import requests

d = requests.get(
    "https://hngtask2-prmpsmart.b4a.run/api",
    params=dict(
        slack_name="Miracle Apata",
        track="backend",
    ),
)

print(d.json())