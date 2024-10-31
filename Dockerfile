FROM node:14 as build-stage

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

COPY --from=build-stage /app/frontend/build ./frontend/build

EXPOSE 5000

ENV FLASK_APP=run:app

CMD ["flask", "run", "--host=0.0.0.0"]
