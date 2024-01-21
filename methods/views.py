from django.http import HttpResponse, HttpRequest
from .models import Car, Customer
from django.shortcuts import render

# Create your views here.

# def index(request):
#     try:
#         cars = Car.objects.all()
#         return HttpResponse(cars)
#     except:
#         return HttpResponse('Error')

# def index(request):
#     cars = Car.objects.all().filter(id=1)        # получение объекта класса Car по id
#     context = {
#         'cars': cars
#     }
#     return render(request, 'methods/index.html', context)

# Пример  НЕ РАБОТАЕТ !!! Просто пример QuerySet
#         QuerySet - тип данных, который работает с запросами.
#         QuerySet преобразует методы Python в SQL-запросы !!!
# def index(request):
#     cars = Car.objects.all()         # ЭТИ все 3 запроса образуют ОДИН QuerySet
#     cars = cars.filter(id=1)         # т.е. все 3 запроса выполняются одновременно
#     cars = cars.count()
#     # cars = Car.objects.all().filter(id=1).count()   # Либо можно в одну строку - 3 запроса образуют ОДИН QuerySet
#     context = {'cars': cars}
#     return render(request, 'methods/index.html', context)


# РАБОТАЕТ !!!
# def index(request):
#     cars = Car.objects.filter(car_brand='MERSEDES')   # получение из Таблицы ВСЕХ авто марки MERSEDES
#     context = {
#         'cars': cars
#     }
#     return render(request, 'methods/index.html', context)

# РАБОТАЕТ !!!
# def index(request):
#     cars = Car.objects.order_by('car_brand', 'price')   # сортировка по названию ВСЕХ АВТО
#     context = {
#         'cars': cars
#     }
#     return render(request, 'methods/index.html', context)

# РАБОТАЕТ !!!
# def index(request):
#     cars = Car.objects.distinct('car_brand')   # ВЫВОД только уникальных значений (убирает дубликаты)
#     context = {
#         'cars': cars
#     }
#     return render(request, 'methods/index.html', context)


# РАБОТАЕТ !!!
# Метод exists() (и его асинхронная версия aexists()) возвращает True,
# если набор QuerySet содержит данные, и False - если не содержит:
# def index(request):
#     is_cars = Car.objects.filter(car_brand='BMW').exists()
#     if is_cars:
#         return HttpResponse('True')
#     else:
#         return HttpResponse('False')


# РАБОТАЕТ !!!
# Метод contains() (и его асинхронная версия acontains()) возвращает True,
# если набор QuerySet содержит определенный ОБЪЕКТ, и False - если не содержит:
def index(request):
    car = Car.objects.get(car_brand='BMW')
    cars = Car.objects.contains(car)
    if cars:
        return HttpResponse('True')
    else:
        return HttpResponse('False')



# METOД raw() ???????????????????????????????
# Django автоматически транслирует методы QuerySet в соответствующие SQL-выражения,
# которые затем выполняются в базе данных. Однако фреймворк также позволяет непосредственно
# определить SQL-запрос и выполнять его. Для этого применяется метод raw(), в который передается SQL-запрос:
# В данном случае в raw() передается запрос, который получает значения полей id и name из таблицы methods_car

# def index(request):
#     cars = Car.objects.raw('SELECT id, car_brand FROM methods_car')
#
    # context = {
    #     'cars': cars
    # }
    # return render(request, 'methods/index.html', context)


# СОЗДАНИЕ ОБЪЕКТА -
# ВАРИАНТ 1.1
def create(request):
    try:
        car = Car(
            car_brand='MERSEDES',
            year_production=2023,
            price=44_000,
            color='White'
        )
        car.save()
        return HttpResponse('Created')
    except:
        return HttpResponse('Error')

# ВАРИАНТ 1.2
# def create(request: HttpRequest) -> HttpResponse:
#     try:
#         car = Car(
#             car_brand='TOYOTA',
#             year_production=2023,
#             price=41_000,
#             color='White'
#         )
#         car.save()
#         return HttpResponse('Created')
#     except:
#         return HttpResponse('Error')

# СОЗДАНИЕ ОБЪЕКТА - 2 ВАРИАНТ - Добавление в БД сразу несколько АВТОМОБИЛЕЙ !!!
# def create(request):
#     try:
#         car1 = Car(
#             car_brand='GEELY',
#             year_production=2021,
#             price=18_000,
#             color='White'
#         )
#         car2 = Car(
#             car_brand='HAVAL',
#             year_production=2023,
#             price=19_500,
#             color='Blue'
#         )
#         car3 = Car(
#             car_brand='SsangYong',
#             year_production=2023,
#             price=17_500,
#             color='Green'
#         )
#         list_cars = [car1, car2, car3]
#         for car in list_cars:
#             car.save()
#         return HttpResponse('Created')
#     except:
#         return HttpResponse('Error')


# ОБНОВЛЕНИЕ ДАННЫХ:
def edit(request):
    try:
        car = Car.objects.get(id=7)        # получение объекта класса Car по id
        car.price = 50000                  # изменение нужного поля = "price"
        car.color = 'yellow'
        # car.save(update_fields=['price'])  # обновление только одного поля(...)
        car.save()                           # или обновление ВСЕХ полей
        return HttpResponse('edited')
    except:
        return HttpResponse('Error')



# УДАЛЕНИЕ ДАННЫХ: 1 Вариант ??????????????????????????
def delete(request):
    car = Car.objects.filter(car_brand='HAVAL').exists()
    if car:                                # Здесь BOOLean ответ (True or False) сущ-ет в Таблице или НЕТ !
        Car.objects.delete(car)
    return HttpResponse('deleted')


# 2 Вариант по id:
# def delete(request):
#     try:
#         car = Car.objects.get(id=7)             # получение объекта класса Car по id
#         car.delete()
#         return HttpResponse('deleted')
#     except:
#         return HttpResponse('Error')



def get_car_customer(request):
    try:
        cust_car = Customer.objects.filter(car_id=5)  # получить ВСЕХ ПОКУПАТЕЛЕЙ автомобиля с id=5
        return HttpResponse(cust_car)
    except:
        return HttpResponse('Error')

# def get_car_customer(request):
#     try:
#         car_name = Customer.objects.get(id=1).car.car_brand  # получить АВТОМОБИЛЬ, который приобрел покупатель с id=1
#         return HttpResponse(car_name)
#     except:
#         return HttpResponse('Error')

# ПРИМЕР с УРОКА:
# def get_user_from_post(request):
#     user = Post.objects.filter(user_id=12)  # получить все посты пользователя с id=12
#     # user_name = Comment.objects.get(id=1).user.name - получить имя пользователя, который оставил комментарий с id=1
#     # user_name = Post.objects.get(id=1).user.name - получить имя пользователя, который оставил пост с id=1
#     return HttpResponse(user)