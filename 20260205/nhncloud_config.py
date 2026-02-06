from dotenv import load_dotenv
import os

load_dotenv()

# --- [1. 설정 정보] ---
AUTH_URL = "https://api-identity-infrastructure.nhncloudservice.com/v2.0/tokens"
TENANT_ID = os.getenv("nhn_cloud_tenantID")
USERNAME = os.getenv("nhn_cloud_id")
PASSWORD = os.getenv("nhn_cloud_pw")

# 리전 엔드포인트 및 이미지 UUID 설정
NW_URL = "https://kr1-api-network-infrastructure.nhncloudservice.com/v2.0"
COMPUTE_URL = f"https://kr1-api-instance-infrastructure.nhncloudservice.com/v2/{TENANT_ID}"

# 🌟 Ubuntu 24.04 이미지, 인스턴스 타입 UUID
UBUNTU_24_UUID = "7342b6e2-74d6-4d2c-a65c-90242d1ee218"
M2_C1M2_UUID = "a4b6a0f7-aeff-4d78-a8d5-7de9f007012d"