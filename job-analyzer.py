def read_file(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        return file.read()
    
def extract_keywords(text):
    text=text.lower()
    for ch in [",",".","(",")",":",";"]:
        text.replace(ch,"")
    
    words=text.split()

    return set(words)

def compare_keywords(resume_text,job_text):
    resume_keywords=extract_keywords(resume_text)
    job_keywords=extract_keywords(job_text)

    matched=resume_keywords.intersection(job_keywords)

    if len(job_keywords)==0:
        match_percentage=0
    else:
        match_percentage=(len(matched)/len(job_keywords))*100
    
    missing=job_keywords-resume_keywords

    return match_percentage,missing

def main():
    resume_path=input("Enter resume file path: ")
    job_path=input("Enter job description file path: ")

    resume_text=read_file(resume_path)
    job_text=read_file(job_path)
    
    match_percentage,missing=compare_keywords(resume_text,job_text)

    print("\n" + "="*30)
    print("\nMatch Score = ",match_percentage,"%")
    print("\n" + "="*30)

    if missing:
        print("\nMissing Keywords = ")
        for word in list(missing):
            print("-",word)
    else:
        print("\nNo missing keywords, it is a strong match")


   

if __name__=="__main__":
    main()
   