import sys
import ipaddress
import nhncloud_util as utils

def validate_vpc_cidr():
    allowed = ["10.0.0.0/16", "172.16.0.0/16", "192.168.0.0/16"]
    while True:
        val = input(f"\n[VPC] 대역 입력 ({', '.join(allowed)}): ")
        if val in allowed: return val
        print("❌ 허용되지 않은 대역입니다.")

def main():
    print("🚀 NHN Cloud 인프라 생성 자동화")
    
    # 1. 입력 수집
    key_name = input("키 페어 이름: ")
    vpc_name = input("VPC 이름: ")
    vpc_cidr = validate_vpc_cidr()
    sub_name = input("서브넷 이름: ")
    sub_cidr = input(f"서브넷 대역 (예: {vpc_cidr[:-3]}/24): ")
    sg_name = input("보안 그룹 이름: ")
    allow_ip = input("SSH 허용 IP (예: 0.0.0.0/0): ")
    inst_name = input("인스턴스 이름: ")

    # 2. 인증 및 실행
    token = utils.get_auth_token()
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

    # 3. 인프라 조립
    utils.create_keypair(headers, key_name)
    
    vpc_id, err = utils.create_vpc(headers, vpc_name, vpc_cidr)
    if err: print(f"❌ VPC 생성 실패: {err}"); sys.exit()
    
    sub_id, err = utils.create_subnet(headers, sub_name, vpc_id, sub_cidr)
    if err: print(f"❌ 서브넷 생성 실패: {err}"); sys.exit()
    
    utils.create_security_group(headers, sg_name, allow_ip)
    
    success, msg = utils.create_instance(headers, inst_name, vpc_id, sg_name, key_name)
    if success:
        print(f"\n✅ 모든 인프라 생성 성공! 인스턴스명: {inst_name}")
    else:
        print(f"❌ 인스턴스 생성 실패: {msg}")

if __name__ == "__main__":
    main()