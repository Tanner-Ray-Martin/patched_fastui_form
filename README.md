# patched_fastui_form
get's rid of the upload bug from fastui_forms

[From PR](https://github.com/pydantic/FastUI/issues/146#issuecomment-1925926007)

And [Working example](https://github.com/dimonlime/ERP-system/blob/698ec52820fc76a28754edd33a8dca56f8c12882/main.py#L104)


## Installation

Clone this repo
```
git clone https://github.com/Tanner-Ray-Martin/patched_fastui_form.git
```

To get started with this project, you'll need to install the necessary dependencies. You can do this using `pip`:
```
pip install uvicorn
pip install fastapi
pip install fastui
```

These commands will install:
- **Uvicorn**: A lightning-fast ASGI server used to serve FastAPI applications.
- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+.
- **FastUI**: A user interface framework built on top of FastAPI for creating web applications with rich UI components.

## Running the Application

After installing the dependencies, you can run your FastAPI application using Uvicorn. If your application entry point is `example.py`, use the following command:

```
uvicorn example:app --reload
```

This command will start the server and serve your FastAPI application. The `--reload` flag enables auto-reloading, making it easier to see changes during development.

