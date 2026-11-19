FROM python:3.13-slim-bookworm
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

RUN useradd app
USER app

COPY --chown=app:app src ./src/

ENV PYTHONPATH="/usr/local/app/src/backend/"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]