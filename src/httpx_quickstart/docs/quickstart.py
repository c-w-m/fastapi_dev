import httpx

try:
    r = httpx.get('http://httpbin.org/get')
    print(r)
except httpx.RequestError as exc:
    print(f"An error occurred while requesting {exc.request.url!r}.")

try:
    # this does not work with https
    r = httpx.get('https://httpbin.org/get')
    print(r)
except httpx.RequestError as exc:
    print(f"An error occurred while requesting {exc.request.url!r}.")

try:
    response = httpx.get('http://httpbin.org/get')
    response.raise_for_status()
    print(response)
except httpx.HTTPError as exc:
    print(f"Error while requesting {exc.request.url!r}.")

try:
    # this does not work with https
    response = httpx.get('https://httpbin.org/get')
    response.raise_for_status()
    print(response)
except httpx.HTTPError as exc:
    print(f"Error while requesting {exc.request.url!r}.")
