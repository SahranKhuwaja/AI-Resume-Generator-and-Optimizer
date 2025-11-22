from flask import Blueprint, request
from services.langchain_service import generate_resume

generator_router = Blueprint('resumeGenerator', __name__)

@generator_router.post('/generate')
def generator():
   return "Hello World"