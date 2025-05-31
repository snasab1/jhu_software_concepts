import re, json

def save_data(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
    
def clean_data(input_filename, output_filename):
    data = load_data(input_filename)
    program_types = ["PhD", "Masters", "MFA", "MBA", "JD", "EdD", "Other", "PsyD"]
    pattern = re.compile(rf"({'|'.join(program_types)})$")
    for applicant in data:
        prog_name = applicant.get("Program Name")
        if prog_name:
            match = pattern.search(prog_name)
            if match:
                prog_type = match.group(1)
                # Remove the type from the end of the string
                new_prog_name = pattern.sub("", prog_name).strip(" ,;-")
                applicant["Program Name"] = new_prog_name
                applicant["Program Type"] = prog_type
            else:
                applicant["Program Type"] = None
    save_data(data, output_filename)

