import model

def update_pf(Data, pc, tc):

    pf,projects = model.retrieve_pf()
    print(Data)

    pf[4] = "   <title>"+Data[0]+"</title>"
    pf[32] = "      <a class=\"navbar-brand js-scroll\" href=\"#page-top\">"+Data[0]+"</a>"
    pf[68] = "          <h1 class=\"intro-title mb-4\">"+Data[0]+"</h1>"
    pf[69] = "          <p class=\"intro-subtitle\"><span class=\"text-slider-items\">"+Data[1]+","+Data[2]+","+Data[3]+","+Data[4]+"</span><strong class=\"text-slider\"></strong></p>"
    pf[91] = "                      <p><span class=\"title-s\">Name: </span> <span>"+Data[0]+"</span></p>"
    pf[92] = "                          <p><span class=\"title-s\">Profile: </span> <span>"+Data[1]+"</span></p>"
    pf[93] = "                          <p><span class=\"title-s\">Email: </span> <span>"+Data[5]+"</span></p>"
    pf[94] = "                          <p><span class=\"title-s\">Phone: </span> <span>"+Data[6]+"</span></p>"
    
