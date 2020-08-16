import model

def return_webpage(pf):
    pass

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
    pf[100] = "                  <span>"+Data[7]+"</span> <span class=\"pull-right\">"+Data[8]+"%</span>"
    pf[105] = "                  <span>"+Data[9]+"</span> <span class=\"pull-right\">"+Data[10]+"%</span>"
    pf[110] = "                  <span>"+Data[11]+"</span> <span class=\"pull-right\">"+Data[12]+"%</span>"
    pf[115] = "                  <span>"+Data[13]+"</span> <span class=\"pull-right\">"+Data[14]+"%</span>"
    pf[130] = Data[15]
    pf[163] = "              <h2 class=\"s-title\">"+Data[16]+"</h2>"
    pf[160] = "              <span class=\"ico-circle\"><i class="+Data[17]+"></i></span>"
    pf[165] = Data[18]
    pf[176] = "              <h2 class=\"s-title\">"+Data[19]+"</h2>"
    pf[178] = "              <span class=\"ico-circle\"><i class="+Data[20]+"></i></span>"
    pf[173] = Data[21]
    pf[189] = "              <h2 class=\"s-title\">"+Data[22]+"</h2>"
    pf[186] = "              <span class=\"ico-circle\"><i class="+Data[23]+"></i></span>"
    pf[191] = Data[24]
    pf[202] = "              <h2 class=\"s-title\">"+Data[25]+"</h2>"
    pf[199] = "              <span class=\"ico-circle\"><i class="+Data[26]+"></i></span>"
    pf[204] = Data[27]
    pf[215] = "              <h2 class=\"s-title\">"+Data[28]+"</h2>"
    pf[212] = "              <span class=\"ico-circle\"><i class="+Data[29]+"></i></span>"
    pf[217] = Data[30]
    pf[228] = "              <h2 class=\"s-title\">"+Data[31]+"</h2>"
    pf[225] = "              <span class=\"ico-circle\"><i class="+Data[32]+"></i></span>"
    pf[230] = Data[33]
    pf[249] = "              <p class=\"counter\">"+Data[34]+"</p>"
    pf[260] = "              <p class=\"counter\">"+Data[35]+"</p>"
    pf[271] = "              <p class=\"counter\">"+Data[36]+"</p>"
    pf[521] = "                      <li><a href="+Data[-4]+"><span class=\"ico-circle\"><i class=\"ion-social-linkedin\"></i></span></a></li>"
    pf[522] = "                      <li><a href="+Data[-3]+"><span class=\"ico-circle\"><i class=\"ion-social-github\"></i></span></a></li>"
    pf[523] = "                      <li><a href="+Data[-2]+"><span class=\"ico-circle\"><i class=\"ion-android-globe\"></i></span></a></li>"
    pf[524] = "                      <li><a href="+Data[-1]+"><span class=\"ico-circle\"><i class=\"ion-social-instagram\"></i></span></a></li>"

    current = 37
    updated_indx = 305
    for i in range(int(pc)):
        if(i<6):
            pf[updated_indx] = "                    <h2 class=\"w-title\">"+Data[current]+"</h2>"
            pf[updated_indx+2] = "                      <a href=""><span class=\"w-ctegory\">"+Data[current+1]+"</span> / <span class=\"w-date\">"+Data[current+2]+"</span></a>"
            if(i<5):
                updated_indx += 21
            elif(i==5):
                updated_indx += 11
        else:
            pf[updated_indx] += "\n<div class=\"col-md-4\"><div class=\"work-box\"><a href=\"img/work-5.jpg\" data-lightbox=\"gallery-mf\"><div class=\"work-img\"><img src=\"img/work-5.jpg\" alt=\"\" class=\"img-fluid\"></div><div class=\"work-content\"><div class=\"row\"><div class=\"col-sm-8\"><h2 class=\"w-title\">"+Data[current]+"</h2><div class=\"w-more\"><span class=\"w-ctegory\">"+Data[current+1]+"</span> / <span class=\"w-date\">"+Ddata[current+2]+"</span></div></div><div class=\"col-sm-4\"></div></div></div></a></div></div>\n"
        current += 3

    testi_indx = 439
    for i in range(int(tc)):
        if(i==0):
            pf[testi_indx] = "                <span class=\"author\">"+Data[current]+"</span>"
            pf[testi_indx+4] = Data[current+1]
            testi_indx+= 12
        else:
            pf[testi_indx]+="\n<div class=\"container\"><div class=\"row\"><div class=\"col-md-12\"><div id=\"testimonial-mf\" class=\"owl-carousel owl-theme\"><div class=\"testimonial-box\"><div class=\"author-test\"><img src=\"img/testimonial-2.jpg\" alt=\"\" class=\"rounded-circle b-shadow-a\"><span class=\"author\">"+Data[current]+"</span></div><div class=\"content-test\"><p class=\"description lead\">"+Data[current+1]+"</p><span class=\"comit\"><i class=\"fa fa-quote-right\"></i></span></div></div></div></div></div></div>\n"

        current += 2
    pf = pf[:updated_indx+10]+pf[422:]

    return pf
