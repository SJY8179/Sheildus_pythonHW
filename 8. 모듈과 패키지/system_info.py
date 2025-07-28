import os
import sys

# --- 1. sys와 os 모듈로 시스템 정보 확인 ---
print("## 1. 시스템 정보")
print(f"운영체제: {os.name} ({sys.platform})")
# sys.version은 상세 정보가 길기 때문에, 첫 부분만 잘라서 표시합니다.
print(f"파이썬 버전: {sys.version.split()[0]}")
print(f"현재 작업 디렉토리: {os.getcwd()}")
print("-" * 40)


# --- 2. os.path 모듈로 파일 경로 다루기 ---
print("## 2. 파일 경로 다루기")

# 운영체제에 맞는 경로 구분자(Windows: '\\', macOS/Linux: '/')를 사용하여
# 안전하게 경로를 만듭니다.
dir_name = "documents"
file_name = "report.docx"
full_path = os.path.join(dir_name, file_name)

print(f"디렉토리와 파일명을 조합한 경로: {full_path}")
print(f"경로에서 디렉토리명만 추출: {os.path.dirname(full_path)}")
print(f"경로에서 파일명만 추출: {os.path.basename(full_path)}")

# 현재 경로에 파일이 실제로 존재하는지 확인합니다.
print(f"'{full_path}' 파일이 실제로 존재하나요? {os.path.exists(full_path)}")