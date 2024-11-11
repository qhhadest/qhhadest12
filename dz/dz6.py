result = []
def divider(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("не можна ділити на 0")
        return
    except TypeError:
        print("Ви не можете ділити нечислові значення")
        return
    except ValueError:
        print("Ви не можете ділити нечислові значення")
        return

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
result = []
for key in data:
   res = divider(key, data[key])
   result.append(res)

print(result)