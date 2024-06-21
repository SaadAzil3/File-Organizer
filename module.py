def switch_case(var:str, ex:list):
    for i in range(len(ex)):
        if var in ex[i]["extension"]:
            return ex[i]["name"]
        
    return "Other Files"

default_file_name_and_extension = [
    {"name": "Images", "extension": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".svg", ".webp"]},
    {"name": "PDF Files", "extension": [".pdf"]},
    {"name": "Microsoft Office Files", "extension": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".mdb", ".accdb"]},
    {"name": "Text Files", "extension": [".txt", ".md", ".csv", ".html"]},
    {"name": "System Files", "extension": [".bin", ".log", ".iso", ".exe", ".dll", ".sys"]},
    {"name": "Audio Files", "extension": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"]},
    {"name": "Video Files", "extension": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".mpeg", ".webm"]},
    {"name": "Programming Files", "extension": [".py", ".java", ".cpp", ".c", ".cs", ".js", ".css", ".php", ".rb", ".go", ".rs", ".json"]},
    {"name": "Compressed Files", "extension": [".zip", ".rar", ".7z", ".tar.gz", ".bz2", ".xz"]}
]

            