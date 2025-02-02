from pathlib import Path

def parse_log_line(line: str) -> dict:
    
    parts = line.split(" ")
    return {
        "date": parts[0],
        "time": parts[1],   
        "level": parts[2],  
        "message": parts[3]
    }

log = "2024-01-22 08:30:01 INFO User logged in successfully."
print (parse_log_line(log))

def load_logs(file_path: str) -> list:
    path = Path(file_path)
    if not path.exists():
        print("Ошибка: Файл не найден!")
        return []
    
    logs = []
    
    
    with path.open(encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:  
                continue
            log_entry = parse_log_line(line.strip())  
            logs.append(log_entry)

    return logs


log_file = "C:/Users/Серёжа/git/first_nepo/logs.txt"  
logs_data = load_logs(log_file)


for log in logs_data[:]:  
    print(log)
