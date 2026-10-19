import re
stats = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
error_users = set()
with open('logs.txt','r',encoding='utf-8') as f:
    for line in f:
        match_level = re.search(r'\b(INFO|WARNING|ERROR)\b', line)
        if match_level:
            level = match_level.group(1)
            stats[level] += 1
        if 'ERROR' in line:
            match_user = re.search(r'User\s(\d+)', line)
            if match_user:
                user_id = match_user.group(1)
                error_users.add(user_id)

for level, count in stats.items():
    print(f"{level}: {count}")
print('\nПользователи с ошибками:', ", ".join(sorted(error_users)))