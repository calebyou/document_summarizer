import os

def read_document_record(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Creating a new file with default content.")
        default_content = """
# document Record

## Alerts
_No alerts yet._

## Title
- **4:** What is bond?
- **5:** Understanding the bond
- **5:** What is compound rate?
"""
        with open(file_path, "w") as file:
            file.write(default_content)
        return default_content

    with open(file_path, "r") as file:
        return file.read()

def write_document_record(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

def format_document_record(document_info, alerts, title):
    record = "# document Record\n\n## document Information\n"
    for key, value in document_info.items():
        record += f"**{key}:** {value}\n"
    
    record += "\n## Alerts\n"
    print(alerts)
    if alerts:
        for alert in alerts:
            record += f"- **{alert['date']}:** {alert['note']}\n"
    else:
        record += "_No alerts yet._\n"
    
    record += "\n## Title \n"
    for key, value in title.items():
        record += f"- **{key}:** {value}\n"
    
    return record

def parse_document_record(markdown_content):
    document_info = {}
    alerts = []
    title = {}
    
    current_section = None
    lines = markdown_content.split("\n")
    
    for line in lines:
        line = line.strip()  # Strip leading/trailing whitespace
        if line.startswith("## "):
            current_section = line[3:].strip()
        elif current_section == "document Information" and line.startswith("**"):
            if ":** " in line:
                key, value = line.split(":** ", 1)
                key = key.strip("**").strip()
                value = value.strip()
                document_info[key] = value
        elif current_section == "Alerts":
            if "_No alerts yet._" in line:
                alerts = []
            elif line.startswith("- **"):
                if ":** " in line:
                    date, note = line.split(":** ", 1)
                    date = date.strip("- **").strip()
                    note = note.strip()
                    alerts.append({"date": date, "note": note})
        elif current_section == "title" and line.startswith("- **"):
            if ":** " in line:
                key, value = line.split(":** ", 1)
                key = key.strip("- **").strip()
                value = value.strip()
                title[key] = value
    
    final_record = {
        "document Information": document_info,
        "Alerts": alerts,
        "Title": title
    }
    print(f"Final parsed record: {final_record}")
    return final_record