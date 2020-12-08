from typing import Dict

import requests
from django.conf import settings


class FixerAPIException(Exception):
    pass


def get_latest_rates() -> Dict[str, float]:
    try:
        rsp = requests.get(
            f"{settings.FIXER_IO_BASE_URL}/latest?access_key={settings.FIXER_IO_API_KEY}"
        )
    except requests.RequestException as exc:
        raise FixerAPIException("Connection to fixer.io failed") from exc

    rsp_json = rsp.json()
    if not rsp_json["success"]:
        raise FixerAPIException(f"Failed to retrieve currency rates: {rsp_json['error']['info']}")

    return rsp_json["rates"]
