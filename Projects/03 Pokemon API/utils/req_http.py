import asyncio

import requests

# A few handy JSON types
JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]


def http_get_sync(url: str) -> dict[str, JSON]:
    response = requests.get(url)
    return response.json()


async def http_get(url: str) -> dict[str, JSON]:
    return await asyncio.to_thread(http_get_sync, url)
