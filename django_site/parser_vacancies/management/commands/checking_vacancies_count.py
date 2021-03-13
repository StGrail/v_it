from datetime import date

from django.db.utils import IntegrityError
from vacancies.models import Vacancies
from parser_vacancies.models import Vacancies_count
from parser_vacancies.management.commands import config_parser



def check_vacancies_table() -> str:
    """
    Функция, которая определяет наличие вакансий в БД и возвращает 
    URL для запроса

    """
    vacancies_count = Vacancies.objects.filter().count()
    if vacancies_count:
        url_to_parser = config_parser.REQUEST_URL_PERIOD
        return url_to_parser, vacancies_count
    print('Database is empty')
    url_to_parser = config_parser.REQUEST_URL
    return url_to_parser, vacancies_count


def save_vacancies_count_to_db(added_today: int, total_vacancies_count: int):
    """
    Функция, которая сохраняет в БД количество вакансий, сохраненных в БД при очередном включении
    парсера, дату включения, а также общее количество вакансий в БД
    """
    row_vacancies_count = Vacancies_count(
        added_today=added_today,
        total_vacancies_count=total_vacancies_count
    )
    try:
        row_vacancies_count.save()
    except IntegrityError:
        vacancies_count = Vacancies_count.objects.get(date=date.today())
        vacancies_count.added_today += added_today
        vacancies_count.total_vacancies_count = total_vacancies_count
        added_today = vacancies_count.added_today
        vacancies_count.save(update_fields=['added_today', 'total_vacancies_count'])
    print(f'Today added {added_today} vacancies. Total {total_vacancies_count} vacancies')


