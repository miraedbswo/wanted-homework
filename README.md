# wanted-homework
[![Python Version: 3.8](https://badgen.net/badge/python/3.8/green)](https://docs.python.org/3.8/)

## API Spec

| http_method | path     | args | body                           | description |
| ----------- | -------- | ---- | ------------------------------ | ------------------------------ |
| POST        | /api/tag |      | {company_id: int, tag_id: int} |회사 태그 생성|
| DELETE      | /api/tag |      | {company_id: int, tag_id: int} |회사 태그 삭제|
| GET |/api/search|?name=str||이름으로 회사 검색|
| GET |/api/search|?tag=str||태그로 회사 검색|

## Table Structure

![image](./images/structure.png)


