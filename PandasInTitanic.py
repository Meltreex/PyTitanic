import pandas as pd
from collections import Counter

file = pd.read_csv('Titanic.csv')

#Удаление пустых строк
file.dropna(inplace=True)

#Заменяю индексы
file.index = [i for i in range(183)]

#1. Сколько мужчин / женщин находилось на борту?
def return_count_male_female():
    female = sum(file['Sex'] == 'female')
    male = sum(file['Sex'] == 'male')
    return female, male

#2. Сколько мужчин / женщин выжило?
def return_survived_male_female():
    survived_female = sum((file['Sex'] == 'female') & (file['Survived'] == 1))
    survived_male = sum((file['Sex'] == 'male') & (file['Survived'] == 1))
    return survived_female, survived_male

#3. Названия столбцов в базе данных.
def return_name_columns():
    return list(file.columns)

#4. Переименуем столбец Pclass в PassengerClass
def rename_column():
    name_columns_list = list(file.columns)
    name_columns_list[2] = 'PassengerClass'
    file.columns = name_columns_list
    return file

#5. Выберите из базы данных все строки, которые соответствуют пассажирам 1 или 2 класса.
def choose_PassengerClass():
    survived_female = [(file['Pclass'] == 1) | (file['Pclass'] == 2)]
    return survived_female

#6. Информация о таблице
def show_information_dataframe():
    return file.info()

#7. Предоставьте уникальные значения столбца Pclass
def uniq_row():
    return file.Pclass.unique()

#8. Сгруппируйте строки в датафрейме в соответствии со значениями переменной Sex
def group_row():
    for item in file.groupby('Sex'):
        print(item)

#9. Выведите статистическую сводку по столбцу Survived
def describe_surv():
    return file.Survived.describe()

#10. Отберем пассажиров, которые сели в Embarked=Q и заплатили более 78 за билет (Fare > 78)
def show_value():
    return file[(file['Embarked'] == 'Q') & (file['Fare'] >= 78)]

#11. Каковы медиана и стандартное отклонение платежей (Fare)? Округлите до 2 десятичных знаков.
def show_median_and_std():
    return f'Медиана - {round(file.Fare.median(), 2)} \nСтандартное отклонение - {round(file.Fare.std(), 2)}'

#12. Найдите самое популярное имя среди пассажиров.
def popular_name():
    lst = []
    for num, row in file.iterrows():
        if row['Sex'] == 'male':
            lst.append(row['Name'].split()[2])
        popular = Counter(lst).most_common(1)
    return popular[0][0]

#13. Приведите все названия столбцов в датафрейме к нижнему регистру и сохраните изменения.
def rename_low_reg_save():
    lst_name_columns = [i.lower() for i in list(file.columns)]
    file.columns = lst_name_columns
    file.to_csv('rename_file.csv')
