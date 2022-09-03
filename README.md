# 5FOLD

![image](https://user-images.githubusercontent.com/70372577/180336315-65835efe-81e6-4d24-8ed7-91174ba7ef4b.png)

![image](https://user-images.githubusercontent.com/70372577/180336239-ebb22df6-b671-4ea2-8533-2d436f091988.png)

![image](https://user-images.githubusercontent.com/70372577/180336248-0b3dbd51-124e-496b-b1c5-c5fbe7c8cdb3.png)

![image](https://user-images.githubusercontent.com/70372577/180336256-7bf1dccc-d4fe-4f2a-8c54-f63be2294832.png)



### 2-1 학습진행방법

→ [Code] Feature_engineering.ipynb 진행하여 데이터 생성

→ [Code] [modeling.py](http://modeling.py) 진행

### 2-2 모델 로드 및 예측 진행방법

weights.7z 압축풀기 → weights.taraa~weights.tarbf 분할압축풀기

ubuntu 7z & tar 압축해제코드

```python
# 7z 파일 압축풀기위한 library
sudo apt install p7zip-full

# weights.7z압축풀기
7za x weights.7z

cat weights.tar* | tar xvf -
```
