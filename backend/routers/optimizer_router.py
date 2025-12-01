from flask import Blueprint, request, send_file
from services.langchain_service import optimize_resume
from util.read_file import get_data_from_file_type
from base_models.response import Response
from fpdf import FPDF
from io import BytesIO

optimizer_router = Blueprint('resumeOptimizer', __name__)

@optimizer_router.post('/optimize')
def optimizer() -> Response:
   job_description = request.form['job_description']
   resume_bytes = request.files['resume']

   parser_response = get_data_from_file_type(resume_bytes)

   if (parser_response.error):
      return Response(success=False, error=parser_response.error)

   optimized_resume = optimize_resume(job_description, parser_response.text)

   pdf_bytes = text_to_bytes(str(optimized_resume))
   pdf_stream = BytesIO(pdf_bytes)
   pdf_stream.seek(0)

   return send_file(pdf_stream,
                    as_attachment=True,
                    download_name="optimized_resume.pdf",
                    mimetype="application/pdf")

def text_to_bytes(text: str) -> bytes:
   pdf = FPDF()
   pdf.add_page()
   pdf.set_auto_page_break(auto=True, margin=15)
   pdf.set_font("Arial", size=11)
   pdf.multi_cell(0, 6, txt=text)

   pdf_buffer = BytesIO()
   pdf.output(pdf_buffer)

   pdf_bytes = pdf_buffer.getvalue()
   pdf_buffer.close()
   return pdf_bytes
