FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE $PORT 
CMD streamlit run --server.port $PORT app.py
