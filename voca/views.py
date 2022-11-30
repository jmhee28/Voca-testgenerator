from django.shortcuts import render
import os
import random
# Create your views here.
def index(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'wordmaster2000.txt')
    if request.method == 'POST':
        f = open(file_path, 'r', encoding = 'utf-8')
        
        startday = 1
        endday = 10
        vocanum = 50

        try:
            startday = request.POST['start']
            endday = request.POST['end']
            vocanum = int(request.POST['voca']) + 1
        except: 
            startday = 1
            endday = 10
            vocanum = 50
            
        startline = int(startday) * 20 - 20
        endline  = int(endday) * 20
        entire_voca_list=[]
        data = f.readlines()[startline:endline]
        for i in data:
            vocab = i.split(",")
            vocab[0] = vocab[0] +"\n"
            entire_voca_list.append(vocab[0])
            entire_voca_list.append(vocab[1])
        f.close()

        testvocalist = []
        used_idx = []
        total_size = len(entire_voca_list)
        for i in range(1,vocanum):
            num = 0
            while(True):
                num = random.randrange(0,total_size-1)
                if num not in used_idx:
                    break
            used_idx.append(num)
            wr = entire_voca_list[num]
            
            testvocalist.append(wr[:-1])
        
        return render(request, 'voca/WTG.html', {'testlist' : testvocalist})


    return render(request, 'voca/WTG.html')