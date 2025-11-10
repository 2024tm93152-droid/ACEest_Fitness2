FROM python:3.10-slim
WORKDIR /app

RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt     --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org

COPY . .
EXPOSE 5000

CMD ["python", "ACEest_Fitness.py"]
