import re, json

def save_data(data, filename):
    """
    Save data to a JSON file.
    Args:
        data (list): The data to be saved.
        filename (str): The name of the file where the data will be saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        # Set ensure_ascii=False to handle non-ASCII characters which may be present in the user-created data
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_data(filename):
    """
    Load data from a JSON file.
    
    Args:
        filename (str): The name of the JSON file from which to load the data.
    Returns:
        list: The data loaded from the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
    
def clean_data(input_filename, output_filename):
    """
    Further clean the raw JSON data by extracting program types and comments.

    Args:
        input_filename (str): The name of the raw JSON file to clean.
        output_filename (str): The name of the file where the cleaned data will be saved.
    """

    # Load the raw JSON data
    data = load_data(input_filename)

    # List of program types that may appear at the end of the program name
    program_types = ["PhD", "Masters", "MFA", "MBA", "JD", "EdD", "Other", "PsyD"]
    # Create a regex pattern to match the program types at the end of the program name
    pattern = re.compile(rf"({'|'.join(program_types)})$")

    # Loop through each applicant's data
    for applicant in data:
        # Extract the program name and type
        prog_name = applicant.get("Program Name")
        if prog_name:
            match = pattern.search(prog_name)
            # If a match (i.e., program type) is found, extract the program type
            if match:
                prog_type = match.group(1)
                # Remove the type from the end of the string
                new_prog_name = pattern.sub("", prog_name).strip(" ,;-")
                # Update the applicant's data
                applicant["Program Name"] = new_prog_name #Update program name without type
                applicant["Program Type"] = prog_type #Update program type
            else:
                applicant["Program Type"] = None

        # Get rid of any line breaks in the comments
        comments = applicant.get("Comments")
        if comments is not None:
            # Remove \n characters
            comments = comments.replace("\n", " ")
            applicant["Comments"] = comments # Update comments

    # Save the cleaned data to the output JSON file
    save_data(data, output_filename)

