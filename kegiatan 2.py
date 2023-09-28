# Diberikan data campuran
#[] random list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Mengubah susuan syntax
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_data = ()
string_data = []
int_data = {}

for data in random_list:
    if isinstance(data, float):
        float_data +=(data,)
    elif isinstance(data, str):
        string_data.append(data)
    elif isinstance(data, int):
        int_data[data] = data

print("Data Float disimpan dalam bentuk tuple :")
print(float_data)
print("Data String disimpan kedalam list :")
print(string_data)
print("Data int disimpan dalam dictionary :")
print(int_data)