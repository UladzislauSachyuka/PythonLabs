FROM python:3

COPY requirements.txt .
COPY main.py .
COPY constants.py .
COPY operation.py .
COPY helloworld.py .
COPY even_numbers.py .

 RUN pip install --no-cache-dir -r requirements.txt
 
 CMD [ "python", "main.py" ]
