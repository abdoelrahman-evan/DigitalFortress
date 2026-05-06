import os

# المسار للمجلد المخفي الذي أنشأته
path = ".vault/secrets.txt"

# التأكد من وجود الملف قبل فتحه
if os.path.exists(path):
    with open(path, "r") as file:
        secret_data = file.read()
        print("🔑 تم الوصول للخزانة بنجاح!")
        print("📝 المحتوى المخفي هو:", secret_data)
else:
    print("It's personal info")
