from __future__ import annotations as _annotations
from typing import Annotated
from fastapi import FastAPI, UploadFile
from fastui.forms import FormFile
from pydantic import BaseModel, Field
from patched_forms import patched_fastui_form

app = FastAPI()

class FileUploadForm(BaseModel):
    file: (
        Annotated[UploadFile, FormFile(accept=".xlsx, .xls", max_size=int(1e7))] | None
    ) = Field(None, description="Uploaded Spreadsheet")

@app.get(
    "/forms/upload",
    response_model=FastUI,
    response_model_exclude_none=True,
    include_in_schema=False,
    tags=["patched_ui"],
)
async def get_upload_form() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.ModelForm(
                    model=FileUploadForm,
                    submit_url="/forms/upload",
                ),
            ]
        )
    ]

@app.post(
    "/forms/upload",
    response_model=FastUI,
    response_model_exclude_none=True,
    include_in_schema=False,
    tags=["test"],
)
async def display_test_model(
    form: Annotated[FileUploadForm, patched_fastui_form(FileUploadForm)],
) -> list[AnyComponent]:
    if (
        and form.file.filename != ""
        and form.file.size > 0
    ):
        upload_directory = "uploads"
        os.makedirs(upload_directory, exist_ok=True)
        uploaded_file_path = os.path.join(upload_directory, form.file.filename)
        file_content = await form.file.read()
        with open(uploaded_file_path, "wb") as f:
            f.write(file_content)

        await form.file.close()

    return [c.FireEvent(event=GoToEvent(url="/upload/create"))]

@app.get("/api/", response_class=RedirectResponse, tags=["Redirects"])
async def home_redirect_backend() -> RedirectResponse:
    return RedirectResponse("/openapi.json", status_code=302)


@app.get("/", response_class=RedirectResponse, tags=["Redirects"])
async def home_redirect() -> RedirectResponse:
    return RedirectResponse("/upload", status_code=302)


@app.get("/{path:path}", tags=["FastUI HTML"])
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="FastUI Demo", api_root_url="/forms"))

