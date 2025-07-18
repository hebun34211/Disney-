FROM python:3.7 as pyth
RUN mkdir /project
WORKDIR /project
COPY requirements.txt /project/requirements.txt

RUN pip install -r requirements.txt
COPY . /project/

FROM node:8-alpine
WORKDIR /opt/app
COPY package.json package-lock.json* ./
RUN npm cache clean --force && npm install
COPY . /opt/app

ENV PORT 80
EXPOSE 80

COPY --from=pyth /project /opt/app
CMD [ "npm", "start" ]


