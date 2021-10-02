FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80

COPY ./fast_api /fast_api

CMD ["uvicorn", "fast_api.main:app", "--host", "0.0.0.0", "--port", "80"]