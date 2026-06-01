# Global Energy Transition & Economic Analysis Pipeline

> **한 줄 요약:** PySpark와 Hive(Tez)를 활용하여 대용량 글로벌 에너지·탄소·경제 지표 데이터를 분산 처리 및 분석하는 빅데이터 엔지니어링 파이프라인 구축 프로젝트입니다.

---

## Tech Stack & Environment
- **Platform:** Hortonworks Data Platform (HDP 3.0.1 Sandbox)
- **Storage:** Hadoop Distributed File System (HDFS)
- **Processing:** Apache Spark 2.x (PySpark)
- **Data Warehouse:** Apache Hive 3.1 (Execution Engine: **Tez**)
- **Language:** Python

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
