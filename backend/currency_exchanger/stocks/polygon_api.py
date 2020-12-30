from datetime import date, timedelta
from typing import Dict

import requests
from django.conf import settings


class PolygonAPIException(Exception):
    pass


def get_latest_rates() -> Dict[str, float]:

    two_days_prior = date.today() - timedelta(days=2)
    date_formatted = two_days_prior.strftime("%Y-%m-%d")

    try:
        rsp = requests.get(
            f"{settings.POLYGON_IO_BASE_URL}/v2/aggs/grouped/locale/us/market/stocks/"
            f"{date_formatted}?unadjusted=true&apiKey={settings.POLYGON_IO_API_KEY}"
        )
    except requests.RequestException as exc:
        raise PolygonAPIException("Connection to polygon.io failed") from exc

    rsp_json = rsp.json()
    print(rsp_json)

    if not rsp_json["status"] == "OK":
        raise PolygonAPIException(f"Failed to retrieve stocks: {rsp_json['error']['info']}")

    return rsp_json["results"]
