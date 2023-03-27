# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%



def csv_to_df(file_path:str) ->pd.DataFrame:
    test_df=pd.read_csv(file_path)
    return test_df
    

#csv_to_df("StudentsPerformance.csv")

# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")

def capitalize_columns(df_data):
    new_columns=[]
    for columns in df_data.columns:
        if 'e' not in columns:
            new_columns.append(columns.upper())
        else:
            new_columns.append(columns)
    df_data.columns=new_columns
    return df_data

#capitalize_columns(new_df)

# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")

def math_passed_count(df_data):
    math_column=df_data["math score"]
    return math_column

#math_passed_count(new_df)

# %%
#new_df=csv_to_df("StudentsPerformance.csv")

def math_passed_count(df_data):
    math_column=df_data["math score"]
    answer=0
    for i in math_column:
        if i>=50:
            answer+=1
    return answer

#math_passed_count(new_df)

# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")

def did_pre_course(df_data):
    df_did_pre_course=df_data[df_data["test preparation course"] =="completed"]
    return df_did_pre_course

#did_pre_course(new_df)

# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")

def average_scores(df_data:pd.DataFrame) -> pd.DataFrame:
    new_df=df_data.copy()
    grouped=new_df.groupby('parental level of education')  
    return grouped.mean()

#average_scores(new_df)

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")
import random

def add_age(df_data):
    random.seed(42)
    df_data["age"]=np.random.randint(18,67,size=len(df_data))
    return df_data

#add_age(new_df)


# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")

def female_top_score(df_data):
    females=df_data.loc[df_data["gender"]=="female"]
    max_math_score=females["math score"].max()
    max_reading_score=females["reading score"].max()
    max_writing_score=females["writing score"].max()
    return (max_math_score, max_reading_score, max_writing_score)

#female_top_score(new_df)

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")

def add_grade(df_data):
    df_data["grade"]=(df_data["math score"]+df_data["reading score"]+df_data["writing score"])/3
    df_data["grade"]=df_data["grade"].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'D' if x >= 60 else 'F')
    
    return df_data

#add_grade(new_df)

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")
#import matplotlib.pyplot as plt

def math_bar_plot(df_data):
    math_scores=df_data.groupby("gender")["math score"].mean()
    fig, ax=plt.subplots()
    ax.bar(math_scores.index,math_scores.values)
    ax.set_title('Average Math Score by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    return fig

#math_bar_plot(new_df)
#plt.show()



# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")
#import matplotlib.pyplot as plt

def writing_hist(df_data:pd.DataFrame):
    new_df=df_data.copy()
    fig, ax=plt.subplots()
    ax.hist(new_df['writing score'],bins=10)
    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    return fig

#writing_hist(new_df)
#plt.show()

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%
#new_df=csv_to_df("StudentsPerformance.csv")
#import matplotlib.pyplot as plt

def ethnicity_pie_chart(df_data):
    race_numbers=df_data['race/ethnicity'].value_counts()
    fig, ax=plt.subplots()
    ax.pie(race_numbers.values, labels=race_numbers.index, autopct='%1.1f%%')
    ax.set_title('Proportion of Students by Race/Ethnicity')
    return fig

#ethnicity_pie_chart(new_df)
#plt.show()


