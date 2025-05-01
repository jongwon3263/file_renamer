import os

# 파일이 있는 디렉토리 경로
directory = "files"

# 디렉토리의 모든 파일 이름을 가져옴
for filename in os.listdir(directory):
    # 뒤의 숫자만 추출하는 패턴
    parts = filename.split("_")
    if len(parts) >= 3:
        new_name = parts[-2] + "." + filename.split(".")[-1]  # 확장자 유지
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        # 파일 이름 변경
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")