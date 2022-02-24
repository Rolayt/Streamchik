#!/usr/bin/env python
# coding: utf-8

# <div style="background: #0000; padding: 5px; border: 3px solid blue; border-radius: 5px;">
# <font size="4", color = "black">
# <b>КОММЕНТАРИЙ РЕВЬЮЕРА</b>
# <br />
# Рад приветствовать тебя, Константин! <br />
# <br />    
# <br />
# Меня зовут Георгий Озбетелашвили, можно просто Гио. 
# <br />
# Благодарю тебя, что прислал задание! Я перейду сразу на "ты" (если неудобно, то скажи мне). Ты сделал большую работу над проектом! Правильные расчеты, хорошие выводы, все логично и скурпулезно. <br /><br /> Я буду комментировать твои задания по следующим принципам: <br />
# <b>ТАКОЙ ШРИФТ</b> - всегда начало моего комментария <br />
# <font color='blue'>такой фон</font> - комментарии с интересной ссылкой и дополнительной инфой<br/>
# <font color='green'>такой фон</font> - комментарии о том, что всё сделано правильно. Могу тут же оставить полезную рекомендацию <br/>
# <font color='orange'>такой фон</font> - комментарии о том, что всё хорошо, однако есть на что обратить внимание<br/>
# <font color='red'>такой фон</font> - комментарии о том, что есть критически важный момент, которому стоит уделить особое внимание и исправить.<br/>
# Чтобы было легче различать комментарии, я буду прикладывать к каждому типу комментария свой смайлик. Они буду ниже в примерах.
# <br /><br />
# Я буду стараться передавать тебе свой опыт и направлять тебя к правильному и эффективному решению, чтобы в дальнейшем ты мог расти дальше как крутой специалист ;) Будет круто, если будешь оставлять свои комментарии (просьба не удалять мои)! Помни, что глупых вопросов не бывает! А твой дружелюбный сосед ревьюер всегда будет рядом и поможет тебе)<br>
# <br> Ну что, народ, погнали!<br>
#     </font>

# <div style="background: #0000; padding: 5px; border: 3px solid blue; border-radius: 5px;">
# <font size="4", color = "black">
# <b>КОММЕНТАРИЙ РЕВЬЮЕРА v2</b>
# <br />Здравствуй, Константин! Спасибо тебе за важные исправления! Принимаю работу 😎<br>
#     <br> Мои новые комментарии будут с припиской  v2<br> 
#     </font>

# # Примеры комментариев

# <div class="alert alert-info"; style="border-left: 7px solid blue">
# <font size="4"><b>Комментарий ревьюера 🎓</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#       <br />Тут полезная ссылочка, советую посмотреть, если будет время :) Данная тема часто спрашивается на собеседованиях на джун-позиции  <br/>
#         <br /> <a href="https://webdevblog.ru/vvedenie-v-generatory-python/">Введение в генераторы Python</a>
#     <br />
#     </font>
# 
# </div>

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Все отлично, интересная логика решения!  
#      <br />
#     </font>
# 
# </div>

# <div class="alert alert-warning" ; style="border-left: 7px solid orange">
# <font size="4"><b>Комментарий ревьюера 👀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Если таких замечаний >= 3, то следует исправить недочеты. Если кол-во замечаний меньше 3, то зачту проект 
#     <br />
#     </font>
# 
# </div>

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Стоит исправить ошибки)  
#     <br />
#     </font>
# 
# </div>

# # ОПИСАНИЕ ПРОЕКТА
# "Стримчик" - интернет магазин, который продает по всему миру компьютерные игры. Из открытых источников доступны исторические данные о продажах игр, оценки пользователей и экспертов, жанры и платформы (например, Xbox или PlayStation). Им нужно выявить определяющие успешность игры закономерности. Это позволит сделать ставку на потенциально популярный продукт и спланировать рекламные кампании.
# # ЗАДАЧА: 
# 1) Подготовить данные
# 
# 2) Провести исследовательский анализ данных
# 
# 3) Определить для пользователя каждого региона (NA, EU, JP):
# - Самые популярные платформы (топ-5). Опишите различия в долях продаж.
# - Самые популярные жанры (топ-5). Поясните разницу.
# - Влияет ли рейтинг ESRB на продажи в отдельном регионе?
# 
# 4) Проверить гипотезы:
# 
# - Средние пользовательские рейтинги платформ Xbox One и PC одинаковые;
# - Средние пользовательские рейтинги жанров Action (англ. «действие», экшен-игры) и Sports (англ. «спортивные соревнования») разные.
# 
# 5) И составить общий вывод

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Отлично, что есть введение с описанием проекта и его задачами. Было круто добавить описание данных
#     <br />
#     </font>
# 
# </div>

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Следует с помощью ячеек Markdown разделить проект на смысловые части. То есть Шаг 1. Знакомства с данными и тд
#     <br />
#     </font>
# 
# </div>

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀 v2</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Супер, спасибо за красивое оформление!
#      <br />
#     </font>
# 
# </div>

# # ШАГ 1: ЗНАКОМСТВО С ДАННЫМИ

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(
    '/datasets/games.csv',
    header = 0,
    names = ['name', 'platform', 'year_of_release', 'genre', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'critic_score', 'user_score', 'rating']
    )
# Я сразу заголовки привел в нормальный вид, т.к. вычитал, что проще заранее это сделать
df.info()


# In[3]:


df.describe()


# In[4]:


df.head()


# Что нужно поправить с типами данных:
# - year_of_release к году
# - Оценки игр к числам с плавающей точкой

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Хорошее знакомства с данными
#     <br />
#     </font>
# 
# </div>

# # ШАГ 2: ПОДГОТОВКА ДАННЫХ

# Для того, чтобы изменить тип данных, я сначала заполню пропуски в столбце 'year_of_release' на 2100(Чтобы мы их не теряли), в столбце с оценками на '-1'(Встречаются оценки '0' поэтому лучше заменить на -1)

# In[5]:


df['year_of_release'] = df['year_of_release'].fillna(2100)# пропуски в столбце с годом
df['year_of_release'] = df['year_of_release'].astype('int')


# In[6]:


df['critic_score'].unique()#ничего необычного. Пропуски заменяем на -1 и меням тип данных
df['critic_score'] = df['critic_score'].fillna(-1)
df['critic_score'] = df['critic_score'].astype('float')


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Молодец, круто поставил загрушки. Но в случае с годом можно просто удалить несколько строк, они не повлияют на результаты исследования
#     <br />
#     </font>
# 
# </div>

# In[7]:


df['user_score'].unique()


# В столбце с оценкой пользователей встречается вид оценки - 'tbd', что в переводе означает - БУДЕТ ОПРЕДЕЛЕНО. Значит это можно прировнять к пропускам, так как по факту оценки еще нет. 

# In[8]:


df.loc[df['user_score'] == 'tbd', 'user_score'] = np.nan
df['user_score'] = df['user_score'].fillna(-1)
df['user_score'] = df['user_score'].astype('float')


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Супер! Верно разрулил ситуацию
#     <br />
#     </font>
# 
# </div>

# В столбце с рейтингом тоже есть пропуски, заменю их на значения 'without_rating' 

# In[9]:


df['rating'].unique()#ничего необычного, спокойно заменяем
df['rating'] = df['rating'].fillna('without_rating')


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Тут тоже верная заглушка
#     <br />
#     </font>
# 
# </div>

# In[10]:


df.head()


# Теперь добавим в таблицу столбец суммарной продажей. Назову total_sales

# In[11]:


df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']
df.head()


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Верный подсчет!
#     <br />
#     </font>
# 
# </div>

# # ШАГ 3 Исследовательский анализ
# - Посмотрю сколько игр выпускалось в разные годы и в какой год наблюдается рост популярности игрушек

# In[12]:


df['year_of_release'].value_counts()


# In[13]:


df[df['year_of_release'] != 2100]['year_of_release'].plot(kind = 'hist', bins = 40)
plt.title('Распределение по году выпуска')
plt.legend()
plt.show()


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Молодец! Не забыл про заглушку, верно построил распределение
#     <br />
#     </font>
# 
# </div>

# По подсчетам и графику можно сделать вывод, что индустрия игр начала набирать обороты в 1995 году. В 2011 году виден спад. 

# - Посмотрим распределение по платформам

# In[14]:


table_platform = pd.pivot_table(df,
              index = 'platform',
              values = 'total_sales',
              aggfunc = np.sum)


# In[15]:


table_platform_sorted = table_platform.sort_values(by = 'total_sales')
table_platform_sorted


# In[16]:


list_platform = ['PS2', 'X360', 'PS3', 'Wii', 'DS']
for j in list_platform:
    df[df['year_of_release'] != 2100].query('platform == @j')['year_of_release'].plot(kind='hist', label=j, grid=True, bins=10, alpha=0.4, legend=True, figsize=(12, 5))
    plt.show()


# Итак, по платформам:
# Я выбрал топ-5 и построил графики распределения по годам. 
# По появлению новых и уходу старых платформ сложно сказать. Все зависит от платформы. Например PS2 стабильно держалась с 2000 до 2011 года(то есть 11 лет). X360 с 2005 по 2016 (11лет). PS2 с 2006 по 2016(10 лет). Значит с момента появления и ухода платформы проходит примерно 10 лет.

# Актуальный период примем с 2012 года. 

# <div class="alert alert-info" style="background:#ffdbf1;color:#2e00ab">
#     Есть поправить!
#     Значит возьмем с 2012 актуальный период

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Верно найден жизненный цикл платформы
#      <br />
#     </font>
# 
# </div>

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> К сожалению, слишком большой период взял. На интересуют прогнозы на 2017-й год. Поэтому следует брать самые свежые данные. Если брать данные за 10 лет, то к 2017 будем учитывать мертвые платформы. Поэтому следует использовать промежуток в 5 лет.
#     <br />
#     </font>
# 
# </div>

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀 v2</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Отлично! Подходящий актуальный период
#      <br />
#     </font>
# 
# </div>

# In[17]:


df_filtered = df.query('year_of_release >= 2012')
df_filtered.reset_index(inplace=True, drop = True)


# In[18]:


df_filtered.head(20)


# In[19]:


df_filtered[df_filtered['year_of_release'] != 2100]['platform'].unique()


# In[20]:


(
    df_filtered[df_filtered['year_of_release'] != 2100]
    .pivot_table(index='year_of_release', columns='platform', values='total_sales', aggfunc='sum')
    .plot(style='o-', grid=True, figsize=(14,8), title='Продажи с 2005 по 2016 год включительно')
)
plt.xlabel('Год')
plt.ylabel('Продажи, млн.копий')
plt.show()


# Судя по графику нет потенциально прибыльных платформ(хахаха). Все платформы либо уже ушли в 0, либо стремятся туда. На данный момент лидирует PS4 и XOne. 

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Молодец, верно найдены платформы. Согласен, потенциал почти все израсзодовали
#      <br />
#     </font>
# 
# </div>

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Тут стоит выбрать топ-5 платформ хотя бы, чтобы проводить дальнейшее исследование. "3 DS" тоже выглядит совсем неплохо. Чтобы точно выбрать актуальный топ, следует уменшить актуальный временной промежут (до 2014-го) и посчитать за этот период суммарные доходы для определения самых прибыльных. То есть можно построить столбчатую диаграмму, сравнивая суммарные доходы с 2014 до 2016-го (не в динамике, а просто суммы).
#     <br />
#     </font>
# 
# </div>

# <div class="alert alert-info" style="background:#ffdbf1;color:#2e00ab">
# <h3>Комментарий студента!!!!! </h3>
#     Сейчас попробую поправить

# In[21]:


df_filtered_2014 = df.query('year_of_release >= 2014')
df_filtered_2014.reset_index(inplace=True, drop = True)
dohod = pd.pivot_table(df_filtered_2014,
                      index = 'platform',
                      values = 'total_sales',
                      aggfunc = np.sum)
dohod = dohod.sort_values(by = 'total_sales')
dohod


# In[22]:


# комментарий ревьюера
dohod.plot(kind = 'bar')


# In[23]:


top5_platform = df_filtered.query('platform == ["PS4", "XOne", "3DS", "PS3", "X360"]')
top5_platform.reset_index(inplace=True, drop = True)


# <div class="alert alert-info" style="background:#ffdbf1;color:#2e00ab">
# <h3>Комментарий студента!!!!! </h3>
#     Тут мы видим топ 5 по продажам с 2014 года - это PS4, XOne, 3DS, PS3, X360. Диаграмму не строил, т.к. не вижу смысла. По цифрам же проще смотреть
#     

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀 v2</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Принято! Привел короткое оформление графика чуть выше, чтобы не возникали проблемы с построением. А так, все верно!
#      <br />
#     </font>
# 
# </div>

# - Строим ящик с усами по прадажам

# In[24]:


colors = ['#78C850', '#F08030', '#6890F0','#F8D030', '#F85888']
plot = top5_platform.boxplot('total_sales', by = 'platform', figsize=(8, 8)).set_ylim(0, 2.5)


# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     "Глобальный" имелось в виду по всем топовым платформам сделать разбивку. То есть надо отразить усы по каждой из перспективных платформ. Это можно реализовать, если вписать такие значения в параметры графика: by = 'platform'. Для более красивого вывода графика можешь посмотреть библиотеку seaborn и ее график boxplot()
#     <br />
#     </font>
# 
# </div>

# <div class="alert alert-info" style="background:#ffdbf1;color:#2e00ab">
# <h3>Комментарий студента!!!!! </h3>
#     Поправил boxplot. Но с визуализацией какая то беда. Я пытался поменять цвет и перевернуть чтобы проще смотреть было. А он не знает эти аргументы, которые я нагуглил. странно. 

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀 v2</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Получилась хорошая визуализация, которая дает полезную информацию. Неудача может быть связана с тем, что встроенные в pandas методы по визуализации сильно ограничены. Поэтому советовал библиотеку seaborn, там более широкие возможности по визуализации
#      <br />
#     </font>
# 
# </div>

# Выбросы начинаются с 0,95. 

# - выберу плэйстэйшн 4 как одну из самых популярных платформ. Посмотрим как влияют на продажи отзывы.

# In[25]:


df_diagramma = df_filtered.query('platform == "PS4" and critic_score >= 0')


# In[26]:


df_diagramma.plot(x='critic_score', y='total_sales', kind='scatter', title='Диаграмма рассеяния по отзывам критиков')


# In[27]:


df_diagramma['total_sales'].corr(df_diagramma['critic_score'])


# Корреляция 0.41 говорит о наличии слабой связи.  

# In[28]:


df_diagramma = df_filtered.query('platform == "PS4" and user_score >= 0')


# In[29]:


df_diagramma.plot(x='user_score', y='total_sales', kind='scatter', title='Диаграмма рассеяния по отзывам пользователей')


# In[30]:


df_diagramma['total_sales'].corr(df_diagramma['user_score'])


# Корреляция -0.3 означает очень слабую обратную связь. 

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Корреляция не -0.3, а -0.03. Верно строишь диаграммы и считаешь корреляцию. Интересно, как поменяются результаты после смены актуального периода
#      <br />
#     </font>
# 
# </div>

# - Рассмотрим X360

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Тоже неплохой выбор, точно входит в топ-5
#      <br />
#     </font>
# 
# </div>

# In[31]:


df_diagramma1 = df_filtered.query('platform == "X360" and critic_score >= 0')
df_diagramma1.plot(x='critic_score', y='total_sales', kind='scatter', title='Диаграмма рассеяния по отзывам критиков')


# In[32]:


df_diagramma1['total_sales'].corr(df_diagramma1['critic_score'])


# Корреляция 0.39 означает слабую связь.

# In[33]:


df_diagramma1 = df_filtered.query('platform == "X360" and user_score >= 0')
df_diagramma1.plot(x='user_score', y='total_sales', kind='scatter', title='Диаграмма рассеяния по отзывам пользователей')


# In[34]:


df_diagramma1['total_sales'].corr(df_diagramma1['user_score'])


# Корреляция 0.11 означает очень очень ооочень слабую связь.

# - Рассмотрим еще одну платформу - XOne

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Хороший выбор
#      <br />
#     </font>
# 
# </div>

# In[35]:


df_diagramma2 = df_filtered.query('platform == "XOne" and critic_score >= 0')
df_diagramma2.plot(x='critic_score', y='total_sales', kind='scatter', title='Диаграмма рассеяния по отзывам критиков')


# In[36]:


df_diagramma2['total_sales'].corr(df_diagramma2['critic_score'])


# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Ошибся с диаграммой 1. Поэтому ответ nan
#     <br />
#     </font>
# 
# </div>

# In[37]:


df_diagramma2 = df_filtered.query('platform == "XOne" and user_score >= 0')
df_diagramma2.plot(x='user_score', y='total_sales', kind='scatter', title='Диаграмма рассеяния по отзывам пользователей')


# In[38]:


df_diagramma2['total_sales'].corr(df_diagramma2['user_score'])


# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Та же ситуация
#     <br />
#     </font>
# 
# </div>

# <div class="alert alert-info" style="background:#ffdbf1;color:#2e00ab">
# <h3>Комментарий студента!!!!! </h3>
#     Даааа, зря я выбрал это название. ЗАпутался только в этих диаграммах. Просто в голову боллше ничего не пришло:)

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀 v2</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Отлично, теперь все верно. Для названия можно было бы использовать названия платформ
#      <br />
#     </font>
# 
# </div>

# Также слабые связи

# - Посмотрим на жанры

# In[39]:


df['genre'].count()


# In[40]:


table_genre = pd.pivot_table(df,
              index = 'genre',
              values = 'total_sales',
              aggfunc = 'count')
table_genre_sorted = table_genre.sort_values(by = 'total_sales')
table_genre_sorted


# Больше всего продаж конечно же у экшн игр. И получается наш топ 5: ЭКШН, СПОРТ, MISC(аркады), Ролевые и шутеры. ЭКШН игры очень сильно отрываются от второго место, аж на 1000 выпущенных игр. 

# <div class="alert alert-info" style="background:#ffdbf1;color:#2e00ab">
# <h3>Комментарий студента!!!!! </h3>
#     Так. С этим я долго искал как сделать сводную таблицу с count. Но особо ничего не нашел. Но зато придумал такую фишку с len. Теперь мы видим количество игр разных жанров. И получается, что лидируют ЭКШН, СПОРТ, MISC(аркады), Ролевые и шутеры.

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀 v2</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Все было очень легко. Надо было просто вставить слово "count" в параметр aggfunc. Сделал за тебя. Прошу запомни, что так можно делать. Даже можно использовать нескольо функций. Их следует перечислять в виде списка, например: aggfunc = ['count','mean','var'].
#      <br />
#     </font>
# 
# </div>

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     К сожалению, ты нашел сумму продаж, а не количество игр. Чтобы посчитать количество, следует написать "count"
#     <br />
#     </font>
# 
# </div>

# # Шаг 4: Составим портрет пользователя каждого региона

# - Начнем с топ-5 платформ

# In[41]:


df.groupby(by='platform').agg({'eu_sales':'sum'}).sort_values(by='eu_sales', ascending=False).head(5)
# топ 5 платформ в европе


# In[42]:


df.groupby(by='platform').agg({'na_sales':'sum'}).sort_values(by='na_sales', ascending=False).head(5)
# топ 5 платформ в северной америке


# In[43]:


df.groupby(by='platform').agg({'jp_sales':'sum'}).sort_values(by='jp_sales', ascending=False).head(5)
# топ 5 платформ в японии


# In[44]:


df.groupby(by='platform').agg({'other_sales':'sum'}).sort_values(by='other_sales', ascending=False).head(5)
# топ 5 платформ других продаж


# In[45]:


df.groupby(by='platform').agg({'total_sales':'sum'}).sort_values(by='total_sales', ascending=False).head(20)
# Все продажи для расчета долей


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br />Верная реализация, но не те данные
#      <br />
#     </font>
# 
# </div>

# In[47]:


platform = ['PS2', 'PS3', 'X360', 'Wii', 'PS']
total_sales = [1255.77, 939.65, 971.42, 907.51, 730.86]
sales_in_eu = [339.29, 330.29, 270.76, 262.21, 213.61]
dolya_eu = []
for i in range(len(platform)):
    dolya_eu.append(sales_in_eu[i]/total_sales[i])


# In[48]:


dolya_eu = pd.DataFrame(dolya_eu, index = platform)


# In[51]:


platform = ['DS', 'PS', 'PS2', 'SNES', '3DS']
total_sales = [1255.77, 939.65, 971.42, 907.51, 730.86]
sales_in_jp = [806.12, 213.61, 270.76, 200.04, 213.61]
dolya_jp = []
for i in range(len(platform)):
    dolya_jp.append(sales_in_jp[i]/total_sales[i])


# In[52]:


dolya_jp = pd.DataFrame(dolya_jp, index = platform)


# In[53]:


platform = ['X360', 'PS2', 'Wii', 'PS3', 'DS']
total_sales = [971.77, 1255.65, 907.51, 939.65, 806.12]
sales_in_na = [602.47, 583.84, 496.90, 393.49, 382.40]
dolya_na = []
for i in range(len(platform)):
    dolya_na.append(sales_in_jp[i]/total_sales[i])


# In[54]:


dolya_na = pd.DataFrame(dolya_na, index = platform)


# In[55]:


platform = ['PS2', 'PS3', 'X360', 'Wii', 'DS']
total_sales = [1255.65, 939.65, 971.77, 907.51, 806.12]
sales_in_other = [193.44, 135.68, 85.76, 79.07, 59.26]
dolya_other = []
for i in range(len(platform)):
    dolya_other.append(sales_in_jp[i]/total_sales[i])


# In[56]:


dolya_other = pd.DataFrame(dolya_other, index = platform)


# In[57]:


dolya_eu#список с долями продаж в европе


# Вывод по европе: Обожают консольки. Лидирует PS3

# In[58]:


dolya_jp#список с долями продаж в японии


# Вывод по японии: любят миниатюрные платформы для игрушел. Лидирует DS.

# In[59]:


dolya_na#список с долями продаж в северной америке


# Вывод по северной америке: основные покупатели игр на X360.

# In[60]:


dolya_other#список с долями других продаж


# Вывод по остальным продажам: Лидирует PS2.

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Неверно. У нас доли не могут быть больше 1. Доля считается относительно суммарных продаж, а не количества строк платформы
#     <br /><br />
#         Нас интересуют продажи по каждому региону, а не в совокупности
#     </font>
# 
# </div>

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀 v2</b></font>
#     <br />
#     <font size="3", color = "black">
#     <br /> Супер, молодец!
#      <br />
#     </font>
# 
# </div>

# - Топ 5 жанров

# In[61]:


df.groupby(by='genre').agg({'na_sales':'sum'}).sort_values(by='na_sales', ascending=False).head().plot(kind='bar')
df.groupby(by='genre').agg({'jp_sales':'sum'}).sort_values(by='jp_sales', ascending=False).head().plot(kind='bar')
df.groupby(by='genre').agg({'eu_sales':'sum'}).sort_values(by='eu_sales', ascending=False).head().plot(kind='bar')
df.groupby(by='genre').agg({'other_sales':'sum'}).sort_values(by='other_sales', ascending=False).head().plot(kind='bar')


# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Здесь тоже не то, что нужно. Нужно получить результаты по каждому региону
#     </font>
# 
# </div>

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀v2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Все верно!
#     </font>
# 
# </div>

# Вывод: экшн победил везде кроме японии. В японии лидируют ролевые игры. Misc везде занимают последнюю похицию. 

# In[62]:


df_rating = pd.pivot_table(df_filtered,
              index = 'rating',
              values = ('na_sales', 'jp_sales', 'eu_sales', 'other_sales'),
              aggfunc = np.sum)
df_rating = df_rating.sort_values(by = 'na_sales')
df_rating


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Тут похоже на правду. Следует использовать актуальный период, чтобы не выводились старые рейтинги
#     </font>
# 
# </div>

# 'E' означает 'everyone'. Поэтому в европе, северной америке и другим продажам игры с рейтингом 'E' лидируют по продажам. В японии лидером выступает 'without_rating', т.е. без рейтинга.

# Проверю гипотезы
# - H0 Средние пользовательские рейтинги платформ Xbox One и PC одинаковые
# - H1 Средние пользовательские рейтинги платформ Xbox One и PC разные 

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Верная формулировка
#     </font>
# 
# </div>

# Буду использовать критерий Мана-Уитни. Так как с ним не нужно проверять является ли распределение нормальным или нет. Экономим время

# In[63]:


import scipy.stats as stats


# In[64]:


alpha = 0.05
Xone = df_filtered[(df_filtered['platform'] == 'XOne') & (df_filtered['user_score'] >= 0)]['user_score']
Pc = df_filtered[(df_filtered['platform'] == 'PC') & (df_filtered['user_score'] >= 0)]['user_score']
results = stats.mannwhitneyu(Xone, Pc, alternative='two-sided')

if (results.pvalue < alpha):
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")


# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#    Значение 0 - тоже оценка игры, поэтому его тоже следует учитывать
#     <br /><br />
#         Стоит использовать услвные операторы для вывода результата теста
#     </font>
# 
# </div>

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀v2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Так намного лучше, спасибо!
#     </font>
# 
# </div>

# p-value = 6.32 
# Следовательно Нулевую гипотезу отвергнуть не удалось.

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Реализация почти верная, но данные не те
#     </font>
# 
# </div>

# Проверю гипотезы
# - H0 Средние пользовательские рейтинги жанров Action (англ. «действие», экшен-игры) и Sports (англ. «спортивные соревнования») разные.
# - H1 Средние пользовательские рейтинги жанров Action (англ. «действие», экшен-игры) и Sports (англ. «спортивные соревнования») одинаковые.

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Тоже верная формулировка!
#     </font>
# 
# </div>

# In[65]:


action = df_filtered[(df_filtered['genre'] == 'Action') & (df_filtered['user_score'] >= 0)]['user_score']
sports = df_filtered[(df_filtered['genre'] == 'Sports') & (df_filtered['user_score'] >= 0)]['user_score']
results = stats.mannwhitneyu(action, sports, alternative='two-sided')
if (results.pvalue < alpha):
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")


# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Тот же случай с 0. Его следует включить
#     </font>
# 
# </div>

# Отвергаем нулеую гипотезу

# ОБЩИЙ ВЫВОД: актуальным периодом был выбран период с 2012 по 2016 год. С момента появления платформы и её ухода проходит в среднем 10 лет. PS3, X360 и PS2 являются самыми популярными платформами. Потенциально выгодные платформы сейчас определить нельзя, т.к. все платформы идут на спад. Связь м\у отзывами и продажами слабая. Самые прибыльные жанры - это экшн и шутеры. По гипотезам - H0 Средние пользовательские рейтинги платформ Xbox One и PC одинаковые - отвергнуть не удалось, но -H0 Средние пользовательские рейтинги жанров Action (англ. «действие», экшен-игры) и Sports (англ. «спортивные соревнования») разные - отвергаем.

# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <font size="4"><b>Комментарий ревьюера 🦔 </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Вывод тоже следует переделать после исправлений выше.
#     <br /><br /> Я постарался детально описать инструкции по исправлению работы. Надеюсь, получится им следовать и улучшить свой проект! Главное, не расстраивайся и не опускай руки. Ты сделал большую работу, но стоит чутка потерпеть и доделать
#     </font>
# 
# </div>

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀v2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Молодец! Все верно, спасибо за исправления, ты сделал большую работу над ошибками. Принимаю работу и желаю удачи в дальнейших проекта!
#     </font>
# 
# </div>

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <font size="4"><b>Комментарий ревьюера 🚀</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Спасибо за проделанную работу! Если будут вопросы, то задавай их в ответных комментариях, с радостью отвечу на них!
#     </font>
# 
# </div>
