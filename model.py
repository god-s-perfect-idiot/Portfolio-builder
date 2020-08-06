def retrieve_pf():
    try:
        with open("layouts/template1/index.html") as f:
            pdf = []
            pf_data = f.readline()
            while(pf_data!=""):
                pdf.append(pf_data)
                pf_data = f.readline()
        with open("layouts/template1/projects.html") as f:
            pd = []
            projects_data = f.readline()
            while(projects_data != ""):
                pd.append(projects_data)
                projects_data = f.readline()
    except:
        print("File Not Found!?")
        pdf = "FNF"
        pd = "FNF"
    return(pdf, pd)
