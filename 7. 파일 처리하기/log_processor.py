import logging
import re

# 1. 로그 파일 생성 및 설정
def setup_logger(filename):
    """로거를 설정하고 샘플 로그를 기록합니다."""
    # 로거 인스턴스 생성
    logger = logging.getLogger('my_app_logger')
    logger.setLevel(logging.DEBUG)  # 모든 레벨의 로그를 처리하도록 설정

    # 파일 핸들러 설정 ('w' 모드는 실행 시마다 파일을 새로 씀)
    # datefmt로 날짜/시간 포맷을 지정
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler = logging.FileHandler(filename, mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # 이전에 추가된 핸들러가 있다면 제거 (중복 출력 방지)
    if logger.hasHandlers():
        logger.handlers.clear()
    
    logger.addHandler(file_handler)

    # 샘플 로그 기록
    logger.warning("메모리 사용량이 높습니다")
    logger.info("사용자 'admin'이 로그인했습니다.")
    logger.error("데이터베이스 연결 실패")
    logger.debug("SQL 쿼리 실행")
    logger.warning("디스크 공간 부족")
    logger.error("파일을 찾을 수 없음")
    
    print("로그 파일이 생성되었습니다.")

# 2. 파일에서 특정 레벨 로그 필터링
def filter_logs_by_level(filename, level):
    """로그 파일에서 특정 레벨의 로그 라인만 추출합니다."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # 정규표현식을 사용하여 정확히 해당 레벨의 로그만 찾음
            # 예: " - ERROR - " 패턴이 포함된 라인
            pattern = f" - {level} - "
            filtered_lines = [line.strip() for line in f if pattern in line]
            return filtered_lines
    except FileNotFoundError:
        print(f" '{filename}' 파일을 찾을 수 없습니다.")
        return []

# --- 메인 프로그램 실행 ---
log_filename = 'app.log'

# 로그 파일 생성
setup_logger(log_filename)

# ERROR 레벨 로그 필터링 및 출력
error_logs = filter_logs_by_level(log_filename, 'ERROR')
print("\nERROR 레벨 로그들:")
if error_logs:
    for log in error_logs:
        print(log)

# WARNING 레벨 로그 필터링 및 출력
warning_logs = filter_logs_by_level(log_filename, 'WARNING')
print("\nWARNING 레벨 로그들:")
if warning_logs:
    for log in warning_logs:
        print(log)