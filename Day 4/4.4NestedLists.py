fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])






'''
Untuk menghindari indexError jika kita sudah menggunakan len() dan mengetahui jumlah pastinya misal ada 50 list melalui len

untuk dapetin nilai itu kita harus nulisnya 49 karna python menghitung mulai dari 0

cara supaya persis 50 item seperti yang diberi len() adalah dengan cara:

num_of_state = len(states_of_america)
print(states_of_america[num_of_state - 1])

'''