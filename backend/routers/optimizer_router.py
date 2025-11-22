from flask import Blueprint, request
from services.langchain_service import optimize_resume
from util.read_file import get_data_from_file_type
from base_models.response import Response

optimizer_router = Blueprint('resumeOptimizer', __name__)

@optimizer_router.post('/optimize')
def optimizer() -> Response:
   job_description = request.form['job_description']
   resume_bytes = request.files['resume']

   parser_response = get_data_from_file_type(resume_bytes)

   if (parser_response.error):
      return Response(success=False, error=parser_response.error)

   optimized_resume = optimize_resume(job_description, parser_response.text)

   return Response(success=True, 
                   filename=resume_bytes.filename, 
                   content_type=resume_bytes.content_type,
                   generated_resume=str(optimized_resume)).model_dump() 