# Python 3.10 기반 이미지 사용
FROM python:3.10-slim

# 작업 디렉토리 생성
WORKDIR /app

# 필요한 파일 복사
COPY . .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI 실행 (main.py 에서 app 객체 가져옴)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]