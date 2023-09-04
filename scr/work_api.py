import os
from abc import ABC, abstractmethod
import requests


"""Абстрактный класс для работы с API сайтов:"""
class ABCEngine(ABC):

    @abstractmethod

    def get_vacancies(self, query):
        pass



class HH_API(ABCEngine):
    """Класс для работы с API HeadHunter"""

    def get_vacancies(self, query: str):
        options = {'text': f'NAME:{query}'}
        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, options)
        vacancies = response.json()

        return vacancies




class SJ_API(ABCEngine):
    """Класс для получения вакансий с SuperJob"""


    def get_vacancies(self, query: str):
        SUPERJOB_API_KEY = os.getenv('SUPERJOB_API_KEY')
        options = {'name': query}
        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {"X-Api-App-Id": SUPERJOB_API_KEY}
        response = requests.get(url, options, headers=headers)
        vacancies = response.json()
        return vacancies







class Vacancy():
    """Класс для работы с вакансиями"""

    all_vacancies = []

    def __init__(self, name, salary, description, company):
        self.name = name
        self.salary = salary
        self.description = description
        self.company = company
        self.all_vacancies.append({'name': self.name, 'salary': self.salary , 'description': self.description, 'company': self.company})



