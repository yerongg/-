# Global Energy Transition & Economic Analysis Pipeline

> **프로젝트 요약:** PySpark와 Hive(Tez)를 활용하여 대용량 글로벌 에너지·탄소·경제 지표 데이터를 분산 처리 및 분석하는 빅데이터 엔지니어링 파이프라인 구축 프로젝트입니다.

---

## 1. 문제 정의 (Problem Definition)

### 글로벌 기후위기 및 경제 성장 영향도 분석
- **풀고자 하는 문제:** 전 세계적인 기후변화 대응 속에서 각 국가의 **재생에너지 전환율**이 실질적으로 **경제 성장(GDP)**에 제동을 거는지, 혹은 **탄소 배출 집약도 감소**에 얼마나 기여하는지 데이터 기반으로 실증 분석하고자 합니다.
- **수집 및 사용하는 데이터:**
  1. **글로벌 에너지 데이터셋** (Our World in Data Energy Data): 국가별/연도별 재생에너지, 화석연료 소비량 및 발전 비중 지표
  2. **글로벌 탄소 배출 데이터셋** (Our World in Data CO2 Data): 국가별 온실가스 및 이산화탄소 배출량 지표
  3. **글로벌 경제 지표 데이터셋** (GDP Data): 세계은행(World Bank) 기반 국가별 실질 GDP 성장률 지표

---

## 2. 기술 스택 (Tech Stack)

분산 환경에서의 안정적인 대용량 데이터 적재, 처리, 웨어하우징을 위해 HDP 프레임워크를 기반으로 인프라를 구성했습니다.

| 분류 | 기술 도구 |
| :--- | :--- | 
| **Platform** | HDP 3.0.1 Sandbox | 
| **Storage** | Hadoop HDFS | 
| **Processing**| Apache Spark 2.x (PySpark) |
| **Warehouse** | Apache Hive 3.1 (**Tez Engine**) |
---

## 3. 구현 계획 (Implementation Plan & Pipeline)

데이터 수집부터 전처리, 저장, 분석 마트 구축까지의 대략적인 엔지니어링 파이프라인 흐름은 다음과 같습니다.

### [Step 1: 데이터 수집 및 HDFS 적재]
- 웹 및 로컬 인프라에서 수집한 원본 데이터 3종(Energy, CO2, GDP)을 하둡 분산 파일 시스템의 지정된 원천 경로에 독립적으로 적재합니다.
  - *경로 예시:* `/user/project/raw_data/energy/owid_energy_data.csv`

### [Step 2: PySpark 분산 전처리 및 포맷 최적화]
- `spark2-submit` 엔진을 구동하여 HDFS의 원본 데이터를 읽어 들인 후, 국가(Country)와 연도(Year)를 기준으로 **삼중 분산 조인(Triple Join)**을 수행합니다.
- 결측치 처리 및 분석용 파생 변수 생성을 완료한 후, 디스크 I/O 속도와 데이터 압축률을 극대화하기 위해 컬럼형 저장 포맷인 **Parquet 구조**로 최종 변환하여 마트 영역에 저장합니다.

### [Step 3: Hive 고속 데이터 웨어하우스 구축]
- 저장된 Parquet 데이터 레이아웃을 Hive 내부의 `energy_db` 데이터베이스에 **외부 테이블(External Table)**로 스키마 매핑합니다.
- 복잡한 데이터 분석 집계 연산 시 맵리듀스(MapReduce) 대신 고속 분산 연산 엔진인 **Apache Tez**를 활성화하여 '국가별 재생에너지 비중 대비 탄소집약도 추이' 통계 마트를 최종 추출합니다.

## AI Tool Usage
- Gemini: PySpark 실행 및 Hive HDFS 권한 에러(`AccessControlException`) 디버깅, Git 푸시 오류 해결, README.md 구조화 및 실행 가이드 작성, 발표 슬라이드 제작 도움
  
---

## Repository Structure
```directory
bigdata-project/
├── data/                            
│   ├── energy_sample.csv
│   ├── owid_co2_sample.csv
│   └── gdp_sample.csv
├── src/
│   ├── pipeline/
│   │   └── process_data.py           
│   └── analyze/
│       └── analysis.hql             
└── README.md           
