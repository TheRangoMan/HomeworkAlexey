from homework18_1 import ApiHandler

api = ApiHandler("https://jsonplaceholder.typicode.com")

# получаем список пользователей
users = api.get_data("/users")
print(users)
'''
# добавляем нового пользователя
new_user = {"name": "John Doe", "email": "johndoe@example.com"}
added_user = api.add_data("/users", new_user)
print(added_user)

# обновляем данные пользователя
updated_user = {"name": "John Doe Jr.", "email": "johndoe@example.com"}
api.update_data("/users/1", updated_user)

# удаляем пользователя
api.delete_data("/users/1")
'''