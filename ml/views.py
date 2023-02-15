from django.shortcuts import render
import joblib
import pandas as pd
import pickle

def inputdata(request):
    # 새로운 탬플릿 생성
    return render(request, 'ml/inputdata.html')

def ml_result(request):
    # 모델 로드
    cls = joblib.load('ml/tcl_model.pkl')

    df = pd.DataFrame(columns=[['fare_cat', 'age_cat', 'family', 'female', 'male',
       'town_C', 'town_Q', 'town_S']])
    
    # 빈 리스트 생성
    lis = []

    # 원-핫 인코딩 -> 칼람으로 쭉 나온건 원핫인코딩이다.
    lis.append(request.GET['fare_cat'])
    lis.append(request.GET['age_cat'])
    lis.append(request.GET['family'])
    lis.append(request.GET['female'])
    lis.append(request.GET['male'])
    lis.append(request.GET['town_C'])
    lis.append(request.GET['town_Q'])
    lis.append(request.GET['town_S'])

    df.loc[0,:] = lis
    ans = cls.predict(df)
    # 만약 0으로 나오면 대답을 Dead로 주고 아니면 Survived
    if ans == 0:
        ans == "Dead"
    else:
        ans = "Survived"
    return render(request, "ml/ml_result.html",{'lis':lis, 'ans':ans})