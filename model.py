def retrieve_pf():
    try:
        with open("layouts/template1/index.html") as f:
            pf_data = f.read()
        with open("layouts/template1/projects.html") as f:
            projects_data = f.read()
    except:
        print("File Not Found!?")
        pf_data = "FNF"
        projects_data = "FNF"
    return(pf_data, projects_data)
