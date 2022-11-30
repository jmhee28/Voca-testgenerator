from django.shortcuts import render
from django.conf import settings
import os
import random
# Create your views here.
def index(request):
    filelist = os.listdir(settings.DATAS_DIR)
    # print(filelist)

    filenames ={}
    # highfile =[]
    # middlefile = []
    # elementfile = []
    # toeicfile = []
    # toflefile = []      
    # for file in filelist:
    #     tempfile = os.path.splitext(file)
    #     if "고" in tempfile[0]:
    #         highfile.append(tempfile[0])
    #     elif "중" in tempfile[0]:
    #         middlefile.append(tempfile[0])
    #     elif "초" in tempfile[0]:
    #         elementfile.append(tempfile[0])
    #     elif "토익" in tempfile[0]:
    #         highfile.append(tempfile[0])
    #     elif "토플" in tempfile[0]:
    #         highfile.append(tempfile[0])
    #     filenames[tempfile[0]] = file

    

    print(filenames)
    if request.method == 'POST':
        filename = request.POST.get('filename', None)
        print(filename)
        file_path = os.path.join(settings.DATAS_DIR, filename) 
        f = open(file_path, 'r', encoding = 'utf-8')
        try:
            startday = "unit"+request.POST['start']
            endday = "unit"+request.POST['end']
            vocanum = int(request.POST['voca']) + 1
        except: 
            startday = 1
            endday = 10
            vocanum = 50
            
        entire_voca_list=[] #시험범위의 모든 단어

        while True:  
            line = f.readline()
            line = line[:-1]
            if startday in line: 
                while(1):
                    nline = f.readline()
                    nline = nline[:-1]
                    if "unit" not in nline:
                        entire_voca_list.append(nline)
                    if endday in nline:
                        while(1):
                            nline = f.readline()                    
                            if "unit" in nline:
                                break
                            nline = nline[:-1]
                            entire_voca_list.append(nline)
                        break
                break

            if not line: break

        f.close()

        testvocalist = {} #최종 시험 단어
        used_idx = []
        total_size = len(entire_voca_list)
        for i in range(1,vocanum):
            num = 0
            while(True):
                num = random.randrange(0,total_size-1)
                if num not in used_idx:
                    break
            used_idx.append(num)
            voca = entire_voca_list[num].split(",")
           
            testvocalist[voca[0]] = voca[1]
        # print(testvocalist)
        return render(request, 'voca/index.html', {'testlist' : testvocalist, 'filenames': filenames})


    return render(request, 'voca/index.html', {'filenames': filenames})