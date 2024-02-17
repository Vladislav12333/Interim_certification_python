# Импортируем библиотеки
import random
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем экземпляр OneHotEncoder
enc = OneHotEncoder(sparse=False)

# Обучаем OneHotEncoder на столбце whoAmI
enc.fit(data[['whoAmI']])

# Преобразуем столбец whoAmI в one hot вид
one_hot = enc.transform(data[['whoAmI']])

# Создаем новый DataFrame с one hot столбцами
one_hot_df = pd.DataFrame(one_hot, columns=enc.get_feature_names(['whoAmI']))

# Соединяем исходный DataFrame с one hot DataFrame
data = data.join(one_hot_df)

# Выводим результат
data.head()