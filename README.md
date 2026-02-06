# 클라우드 서버 api 활용 자동화
NHN Cloud 환경에서 **VPC, Subnet, Security Group, Key Pair, Instance**를 한 번의 실행으로 자동으로 구축하는 스크립트

## 구성 환경
- **Language**: Python3.8+
- **OS**: Ubuntu 24.04 LTS
- **Instance Type**: m2.c1m2

## 파일 구조
- `nhncloud_main.py`: 전체 프로세스 제어 및 사용자 입력 처리
- `nhncloud_util.py`: NHN Cloud API 호출 및 리소스 생성 로직
- `nhncloud_config.py`: API 엔드포인트 및 사용자 인증 정보

## 장점
<img width="1024" height="1024" alt="Gemini_Generated_Image_8o47dn8o47dn8o47" src="https://github.com/user-attachments/assets/f886a80f-90c5-4fc6-bfec-0bf309e18977" />


## 시작하기

### 모듈 다운로드
- `pip install requests`


### .env 파일 설정
- `cp ./20260205/.env.example ./20260205/.env`로 복사 후 `.env`파일 수정
### 실행하기
- `nhncloud_main.py` 파일 실행
