#1 python image
FROM python:3.13-slim

#want to see o/p instanly
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#3 CREATE ONE FOLDER
WORKDIR /app

#4. Install dependecy install requirment.txt
COPY requirements.txt /app/

#5. Install Lib
RUN pip install --no-cache-dir -r requirements.txt

#6. Remaining codecopy
COPY . /app/

#7. Sever start command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]