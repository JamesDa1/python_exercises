import json

with open("company1.json", "r+") as file:
    data = json.loads(file.read())

    # Add the desired data to the dictionary
    data["employees"].append({
        "firstName": "George",
        "lastName": "Washington"
    })

    # Move cursor to the top of the file
    file.seek(0)

    # Writes to file and reduces the file size
    json.dump(data, file, indent=4, sort_keys=True)
    file.truncate()
    print("Operation complete")
