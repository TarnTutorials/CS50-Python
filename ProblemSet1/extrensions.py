# CS50P - Problem set 1 - 2022 course
# Tarn Montgomery 2024/06/05
# Checks a file name and outputs the file type

def main():
    fileName = input("Enter the file name. \n").lower().strip()
    fileType = checkType(fileName)
    print(f"{fileType}")

def checkType(fileName):
    fileExtension = fileName.split(".")
    fileExtension = fileExtension[-1]
    match fileExtension:
        case "doc":
            return "application/msword"
        case "gif":
            return "image/gif"
        case "html":
            return "text/html"
        case "jpg":
            return "image/jpeg"
        case "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "txt":
            return "text/plain"
        case "pdf":
            return "application/pdf"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()