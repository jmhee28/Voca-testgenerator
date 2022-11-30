from django.shortcuts import render
from django.conf import settings
import os
import random
# Create your views here.
def index(request):
    file_path = os.path.join(settings.DATAS_DIR, '고_능률_voca_어원편.txt')

    if request.method == 'POST':
        f = open(file_path, 'r', encoding = 'utf-8')
        
        startday = 1
        endday = 10
        vocanum = 50

        try:
            startday = "unit"+request.POST['start']
            endday = "unit"+request.POST['end']
            vocanum = int(request.POST['voca']) + 1
        except: 
            startday = 1
            endday = 10
            vocanum = 50
            
        entire_voca_list=[]

        while True:  
            line = f.readline()
            line = line[:-1]
            if line == startday: 
                while(1):
                    nline = f.readline()
                    nline = nline[:-1]
                    if "unit" not in nline:
                        entire_voca_list.append(nline)
                    if nline == endday:
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

        testvocalist = {}
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
           
            testvocalist[voca[0]] = voca[1].replace("|", ", ")
        print(testvocalist)
        return render(request, 'voca/index.html', {'testlist' : testvocalist})


    return render(request, 'voca/index.html')