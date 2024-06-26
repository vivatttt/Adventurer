<p align="center">
      <img src="https://i.ibb.co/G7qXfd7/image.png" width="500">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Flask-3.0.3-red">
   <img src="https://img.shields.io/badge/markdown2-2.4.13-green">
   <img src="https://img.shields.io/badge/SQLAlchemy-2.0.29-purple">
</p>

## About
> **Adventurer** helps the seekers to find, and the inspired to share

That web-site is created both for people who are looking for ideas for their projects and people, who always have concepts, but can't coupe with realisation. <br>

On the **Adventurer** you can find a whole new concept, you've never seen before.

## Demonstration
<p align="center">
      <img src="https://github.com/vivatttt/Adventurer/blob/main/demonstration.gif">
</p>

## Description
This service offers two main functionalities: posting project descriptions or discovering new and interesting projects. Descriptions are written in Markdown to enhance the visual appeal of posts. One standout feature of Adventurer is its specialized database structure and algorithm designed specifically for **quickly searching posts by hashtags**.

## Getting started
To launch the **Adventurer** run following on your **Linux** PC

Download the Virtual Enviroment
```shell
python3 -m venv env
```
```shell
source env/bin/activate
```
Then install all the necessary frameworks
```shell
pip install -r requirements.txt
```
Then you need to initialize DataBase on your PC<br>
So:
1. Create database.db in main directory
2. Run following:
   ```shell
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
   ```
And finally <br>
```shell
make run
```
And enjoy `localhost:8000`
## Gallery <br>

<p align="center">
      <img src="https://i.ibb.co/BjnQRZz/image.png" alt = "Start page" width="900">
</p>

<p align="center">
      <img src="https://i.ibb.co/1Gn8BSf/image.png" alt = "Explore page" width="900">
</p>

<p align="center">
      <img src="https://i.ibb.co/vsKNx3Z/image.png" alt = "Create page" width="900">
</p>

<p align="center">
      <img src="https://i.ibb.co/gRLWfCq/image.png" alt = "Preview page" width="900">
</p>

