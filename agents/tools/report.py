from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel

def write_report(filename: str, html: str) -> str:
    with open(filename, "w") as f:
        f.write(html)
    return "Report generated successfully"

class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str

write_report_tool = StructuredTool.from_function(
    name="write_report",
    description="Write an html report to a file. Use this tool whenever someone asks for a report.",
    func=write_report,
    args_schema=WriteReportArgsSchema
)