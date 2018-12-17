is_ready = True
# Присвоюємо значення змінної в залежності від умови
if is_ready:
    state_msg = 'Ready'
    is_ready = False
else:
    state_msg = 'Not ready yet'

if is_ready:
    tmp = 'is ready is true'
else:
    tmp = 'is_ready is false'

print(state_msg)
print(tmp)
