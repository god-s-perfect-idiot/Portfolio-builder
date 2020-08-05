import model

def update_pf(Data, pc, tc):
    pf,projects = model.retrieve_pf()
    pf = pf.split("/n")
    projects = projects.split("/n")
    print(pf,projects)
