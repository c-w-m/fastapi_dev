# [FastAPI CLI Example](https://fastapi.tiangolo.com/#example)

1. create [main.py](../src/main.py)
2. run

```shell
uvicorn main:app --reload
```

![initial_cli_demo_uvicorn_main.png](img/initial_cli_demo_uvicorn_main.png)

![initial_cli_demo_browser_hello_world.png](img/initial_cli_demo_browser_hello_world.png)

3. send a query

```shell
http://127.0.0.1:8000/items/5?q=somequery
```

![initial_cli_demo_somequerry](img/initial_cli_demo_browser_somequerry.png)

4. get ineractive docs

```shell
http://127.0.0.1:8000/docs
```

![initial_cli_demo_browser_docs.png](img/initial_cli_demo_browser_docs.png)
