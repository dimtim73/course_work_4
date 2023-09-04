from scr.work_api import SJ_API, HH_API, Vacancy
import json



hh_api = HH_API()
sj_api = SJ_API()


hh_vac = hh_api.get_vacancies(query='python')
sj_vac = sj_api.get_vacancies('python')



for vac in hh_vac['items']:
    name = vac['name']
    salary = vac['salary']
    company = vac['employer']['name']
    description = vac['snippet']['requirement']

    vac_one = Vacancy(name, salary, description, company)




# print(json.dumps(hh_vac, indent=2, ensure_ascii=False))

#
for vac in sj_vac['objects']:
    name = vac['profession']
    salary_from = vac.get('payment_from') or 0
    salary_to = vac.get('payment_to') or 0
    salary_currency = vac.get('currency') or 'RUB'
    salary = f'{salary_from}-{salary_to}{salary_currency}'

    company = vac['client']['title']
    description = vac['candidat']

    vac_one = Vacancy(name, salary, description, company)


print(Vacancy.all_vacancies)

# print(json.dumps(sj_vac, indent=2, ensure_ascii=False))
def save_to_file():
    with open('data_vac.json', 'w', encoding='windows-1251') as f:
        f.write(json.dumps(Vacancy.all_vacancies))


save_to_file()

