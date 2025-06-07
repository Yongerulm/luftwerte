import os
import requests
from datetime import datetime


def fetch_aqi(token: str) -> int:
    url = f"http://api.waqi.info/feed/shanghai/?token={token}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    if data.get("status") != "ok":
        raise RuntimeError(f"API returned status {data.get('status')}")
    return data["data"].get("aqi")


def save_to_airtable(
    api_key: str, base_id: str, table_name: str, date: str, aqi: int
) -> None:
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "fields": {
            "Date": date,
            "AQI": aqi,
        }
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=10)
    resp.raise_for_status()


def main() -> None:
    waqi_token = os.environ.get("WAQI_TOKEN")
    airtable_key = os.environ.get("AIRTABLE_API_KEY")
    airtable_base = os.environ.get("AIRTABLE_BASE_ID")
    airtable_table = os.environ.get("AIRTABLE_TABLE_NAME")

    if not all([waqi_token, airtable_key, airtable_base, airtable_table]):
        raise SystemExit("Missing environment variables")

    aqi = fetch_aqi(waqi_token)
    now = datetime.utcnow().isoformat()
    save_to_airtable(airtable_key, airtable_base, airtable_table, now, aqi)
    print("Saved AQI data to Airtable.")


if __name__ == "__main__":
    main()
