# Global Energy Transition Pipeline - 실행 가이드

> 본 문서는 HDP 3.0.1 Sandbox 환경에서 빅데이터 파이프라인을 처음부터 끝까지 에러 없이 실행하기 위한 단계별 가이드라인입니다.

---

### 1단계: 프로젝트 디렉터리 이동
cd ~/bigdata-project

### 2단계: 원본 데이터 다운로드 및 HDFS 분산 적재
cd ~
wget [https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv](https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv)

hdfs dfs -mkdir -p /user/project/raw_data/energy/

hdfs dfs -put ~/owid-energy-data.csv /user/project/raw_data/energy/owid_energy_data.csv

### 3단계: PySpark 분산 전처리 및 Parquet 마트 생성
spark2-submit ~/bigdata-project/src/pipeline/process_data.py

### 4단계: HDFS 권한 강제 개방 (★계정 간 권한 충돌 예방)
hdfs dfs -chmod -R 777 /user/project/processed_data/energy_transition

### 5단계: Hive 데이터 웨어하우스 구축 및 고속 질의
hive -f ~/bigdata-project/src/analyze/analysis.hql

### 6단계: GitHub용 500줄 샘플 데이터 동기화
hdfs dfs -cat /user/project/raw_data/energy/owid_energy_data.csv 2>/dev/null | head -n 500 > ~/bigdata-project/data/energy_sample.csv

hdfs dfs -cat /user/project/raw_data/co2/owid_co2.csv 2>/dev/null | head -n 500 > ~/bigdata-project/data/owid_co2_sample.csv

hdfs dfs -cat /user/project/raw_data/gdp/gdp.csv 2>/dev/null | head -n 500 > ~/bigdata-project/data/gdp_sample.csv
