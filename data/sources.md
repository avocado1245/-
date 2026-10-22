# 공공데이터 및 공간정보 원자료 출처 (Data Sources & Provenance)

한겨레 × 재단법인 숲과나눔 「AI와 함께하는 교통문제 해결을 위한 데이터 분석 공모전」(2026) 출품작(**팀 SSY**)에서 활용한 총 12종 공공데이터의 공식 출처, 고유 데이터셋 번호, 기준 시점 및 라이선스 안내입니다.

| 연번 | 데이터명 | 제공기관 | 형식 | 기준 시점 | 고유 식별자 / 공식 다운로드 URL | 공공누리 유형 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **서울시 수치지도 표고점·등고선** (1:5,000) | 국토지리정보원 / 서울특별시 | SHP (ZIP, 100MB) | 2025~2026 | [서울 열린데이터광장 (OA-22241)](https://data.seoul.go.kr/dataList/OA-22241/F/1/datasetView.do) | 제1유형 (출처표시) |
| 2 | **국가기본도 보도중심선** | 국토지리정보원 | SHP (ZIP, 60MB) | 2025~2026 | [브이월드 국토관리/지역개발 (DS00019)](https://www.google.com/search?q=https://www.vworld.kr/dtmk/dtmk_ntads_s002.do%3FdsId%3D20250121DS00019) | 오픈API/오픈공간정보 |
| 3 | **수치지도 계단 공간정보** (`N3A_C0390000`) | 국토지리정보원 | SHP (ZIP, 3.5MB) | 2025~2026 | [브이월드 연속수치지도 (DS30164)](https://www.vworld.kr/dtmk/dtmk_ntads_s002.do?dsId=30164) | 오픈공간정보 |
| 4 | **보행자우선도로 공간정보** (`C_UQ164_RF`) | 국토지리정보원 | SHP (ZIP, 3.9MB) | 2025~2026 | [브이월드 도시계획 (DS30085)](https://www.google.com/search?q=https://www.vworld.kr/dtmk/dtmk_ntads_s002.do%3FdsId%3D30085) | 오픈공간정보 |
| 5 | **서울시 버스전용차선 공간정보** (`A058_L`) | 행정안전부 / 서울특별시 | SHP (ZIP, 272KB) | 2026.02 | [공공데이터포털 (15138636)](https://www.google.com/search?q=https://www.data.go.kr/data/15138636/fileData.do) | 제1유형 |
| 6 | **서울시 정류장마스터 정보** | 서울특별시 | CSV (1.1MB) | 2026 | [공공데이터포털 (15000303)](https://www.google.com/search?q=https://www.data.go.kr/data/15000303/fileData.do) | 제1유형 |
| 7 | **2026년 9월 버스노선별·정류장별·시간대별 승하차 인원** | 서울특별시 | CSV (15MB) | 2026.09 | [서울 열린데이터광장](https://data.seoul.go.kr/dataList/OA-12912/S/1/datasetView.do) | 제1유형 |
| 8 | **[내국인] 서울 생활인구 (250m 격자)** | 서울특별시 / KT | CSV (56MB) | 2026.10 | [서울 열린데이터광장 (OA-22784)](https://data.seoul.go.kr/dataList/OA-22784/S/1/datasetView.do) | 제1유형 |
| 9 | **행정동별 성별·연령별 주민등록 인구수** | 행정안전부 | CSV (2.5MB) | 2026.09 | [공공데이터포털 (15097972)](https://www.data.go.kr/data/15097972/fileData.do) | 제1유형 |
| 10 | **서울시 역사마스터 정보** | 서울특별시 | CSV (40KB) | 2026 | [서울 열린데이터광장 (OA-21232)](https://data.seoul.go.kr/dataList/OA-21232/S/1/datasetView.do) | 제1유형 |
| 11 | **한국철도공사 역 위치 및 출입구 정보** | 한국철도공사 | CSV (7.3KB) | 2024.04 | [공공데이터포털 (15127532)](https://www.data.go.kr/data/15127532/fileData.do) | 제1유형 |
| 12 | **서울시 지하철 출입구 리프트 위치정보** | 서울특별시 | CSV (11KB) | 2025~2026 | [공공데이터포털 (15098149)](https://www.google.com/search?q=https://www.data.go.kr/data/15098149/fileData.do) | 제1유형 |
| 13 | **서울특별시 자치구 횡단보도 정보** | 서울특별시 | CSV (5.7MB) | 2025~2026 | [공공데이터포털 (15159202)](https://www.google.com/search?q=https://www.data.go.kr/data/15159202/fileData.do) | 제1유형 |

## 대용량 GIS 압축 파일 재현 가이드
- 저장소 내 `data/pipeline/` 폴더에 이미 전처리와 3D 보간이 완료된 최종 결과 CSV 2종(`seoul_250m_grid_3d_result_8566.csv`, `seoul_bus_stop_3d_3grade_7110.csv`)이 커밋되어 있어, 대용량 파일 다운로드 없이도 파이프라인과 검산 테스트(`tests/test_pipeline.py`)를 즉시 실행할 수 있습니다.
- 원본 3D IDW 보간을 처음부터 재현하고자 하는 경우, 위의 링크 1번(`서울시 경사도.zip`)과 2번(`국가기본도_보도중심선.zip`)을 내려받아 `data/` 폴더에 위치시킨 후 실행하면 자동으로 압축 해제 및 3D 공간 연산이 수행됩니다.
