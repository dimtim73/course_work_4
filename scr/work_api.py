import os
from abc import ABC, abstractmethod
import requests


"""Абстрактный класс для работы с API сайтов:"""
class ABCEngine(ABC):

    @abstractmethod

    def get_vacancies(self, query):
        pass


"""Класс для работы с API HeadHunter"""
class HH_API(ABCEngine):
    def get_vacancies(self, query: str):
        options = {'name':'query'}
        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, options)
        vacancies = response.json()
        return vacancies

 """Класс для получения вакансий с SuperJob"""

SUPERJOB_API_KEY = os.getenv('SUPERJOB_API_KEY')
class SJ_API(ABCEngine):


    def get_vacancies(self, query: str):
        options = {'name': query}
        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {"X-Api-App-Id": SUPERJOB_API_KEY}
        response = requests.get(url, options, headers=headers)
        vacancies = response.json()
        return vacancies


    """Класс для работы с вакансиями"""
class Vacancy:

    all_vacancies = []

    def __init__(self, title, salary, description, company, city):
        self.title = title
        self.salary = salary
        self.description = description
        self.company = company
        self.city = city


    """Метод для создания экземпляров классов вакансий с данными из HeadHunter"""
    @classmethod
    def vacancies_from_hh(cls, data):
        pass


    """Метод для создания экземпляров классов вакансий с данными из SuperJob"""
    @classmethod
    def vacancies_from_sj(cls, data):
        pass


