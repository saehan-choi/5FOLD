# 5FOLD

![image](https://user-images.githubusercontent.com/70372577/180336315-65835efe-81e6-4d24-8ed7-91174ba7ef4b.png)

![image](https://user-images.githubusercontent.com/70372577/180336239-ebb22df6-b671-4ea2-8533-2d436f091988.png)

![image](https://user-images.githubusercontent.com/70372577/180336248-0b3dbd51-124e-496b-b1c5-c5fbe7c8cdb3.png)

![image](https://user-images.githubusercontent.com/70372577/180336256-7bf1dccc-d4fe-4f2a-8c54-f63be2294832.png)


# 1. 파일 설명

### 1-1. [Code] Feature_engineering.ipynb : 피쳐엔지니어링 코드

- 가설을 바탕으로 feature engineering된 csv 파일 생성

### 1-2. [Code] Modeling.py : 학습 및 예측 코드

- 실행시 FOLD1 폴더가 생성, 하위에 Y_01~Y_14 모델 가중치 저장(약 3시간 소요)

### 1-3. [Code] Modeling_load.py : 미리 학습된 모델로드, 예측코드

- 가중치 로드 및 csv 파일 생성(약 10분 소요)

# 2. 진행방법

### 2-1 학습/예측 진행방법

- [Code] Feature_engineering.ipynb 실행하여 데이터 생성
- [Code] modeling.py 실행

### 2-2 사전학습 가중치/예측 진행방법

- weights.7z 압축해제
- weights.taraa~weights.tarbf 분할압축해제
- [Code] modeling_load.py 실행

# 3. 기타

### 3-1 **학습환경 권장사항**

- NVIDIA Geforce RTX 3070 이상
- 더 낮은 GPU로도 학습은 가능하나 학습중간 끊어지는 경우가 있음

### 3-2 학습이 끊어졌을시

- case1) [Code] Modeling.py로 학습하다 중간(예로들면 Y_06)에 메모리 문제로 학습이 중단되고 run이 끊겼다
    
    → FOLD1폴더의 Y_06Models-predict폴더를 삭제하고, 70라인의 주석을 참고하여 range(6, 15)로 변경하여 이어서 학습완료. 그러나 sample_submission을 다시 read 하므로, 생성되는 csv는 Y_01~Y_05 prediction이 누락되어 있음 
    
    → [Code] Modeling_load.py 14라인의 weights_path를 weights_path='./FOLD1/'으로 경로만 바꿔주고 실행하면 해당 모델로 Y_01~Y_14 모두를 예측한 csv 생성가능.
    

- case2) [Code] Modeling.py로 학습중인데 error가 발생하여 run중이지만 학습이 안되어(시간이 오래걸리고 cpu, gpu가 사용안되고 있음) 시간만 계속 흐르는 경우
→ run을 멈추고, case1 진행

### 3-3 Requirements

```python
conda create -n LB1 python=3.9.0
conda install -n LB1 ipykernel
conda activate LB1

pip3 install -U pip
pip3 install -U setuptools wheel
pip3 install filterpy

pip3 install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchtext==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu113

pip3 install autogluon**==0.5.3b20220811**
```

### 3-4 ubuntu 환경 7z & tar 압축해제코드

```python
# 7z 압축해제 library 설치
sudo apt install p7zip-full

# 7z 압축해제
7za x weights.7z

# tar 압축해제
cat weights.tar* | tar xvf -
```

### 3-5 Test list

- NVIDIA GeForce RTX 3070 - LB : 1.9090032119 (1등)
- NVIDIA GeForce GTX 1060 - LB : 1.9109867458 (1등 유지)
- NVIDIA GeForce RTX 3090 - LB : 1.9118771404 (1등 유지)
- **학습시 seed는 유지되나 하드웨어별로 결과가 바뀔 수 있음**
