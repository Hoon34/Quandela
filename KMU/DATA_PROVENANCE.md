# 데이터 출처와 가공 기록

## 원본 데이터

이 실습의 실험 용해도 값은 **Quandela가 새로 측정하거나 보유한 기업 협력 데이터가 아니라**, 아래 공개 문헌 데이터셋에서 가져왔습니다.

- **데이터셋:** *BigSolDB 2.2: A Comprehensive Dataset of Solubility Values for Organic Compounds in Organic Solvents and Water at Various Temperatures*
- **저자:** Lev Krasnov, Dmitry Malikov, Marina Kiseleva, Sergei Tatarin, Sergey Sosnin, Stanislav Bezzubov
- **공개일:** 2026-09-07. Zenodo 레코드의 버전 표기는 `v3`, 데이터셋 명칭은 `BigSolDB 2.2`입니다.
- **버전 고정 DOI:** https://doi.org/10.5281/zenodo.22648301
- **공식 제공 페이지:** https://zenodo.org/records/22648301
- **데이터 제공자가 인용을 요청한 관련 논문:** https://doi.org/10.1038/s41597-025-05559-8
- **데이터 라이선스:** Creative Commons Attribution 4.0 International, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

데이터셋 자체가 여러 원 논문의 측정값을 수집한 것입니다. 개별 측정값의 원 논문 DOI는 원본의 `Source` 열에 있습니다.
이 실습은 원 논문의 측정값을 직접 새로 측정한 것으로 표현하지 않습니다.

## 사용한 원본 파일

필터링에 사용한 파일은 같은 버전 레코드의 아래 두 파일입니다. 원본 전체를 이 저장소에 복사하지 않고 실습용 가공 데이터를 배포합니다.

| 원본 파일 | 역할 | 제공 페이지의 MD5와 일치 확인한 값 |
|---|---|---|
| [BigSolDBv2.2.csv](https://zenodo.org/records/22648301/files/BigSolDBv2.2.csv?download=1) | 분자 SMILES, 용매, 온도, 용해도, 원 측정 논문 DOI | `a1e12ae9575319ac4f89fea6a63a6422` |
| [BigSolDBv2.2_methods.csv](https://zenodo.org/records/22648301/files/BigSolDBv2.2_methods.csv?download=1) | 원 논문별 측정 프로토콜과 용해도 실험 구분 | `4e7a688055d0e8ebf4c8c3a202b29b7c` |

원본 보관 파일의 SHA-256:

```text
BigSolDBv2.2.csv
6b63f86601369f92530bedf6b93c3fb92a2731390b28a0aabf55ad005acba401

BigSolDBv2.2_methods.csv
1ed6e3aadfd6095c4ff3e5f9307087ba7ec4a688201b94e8b5efc4827a635eae
```

## 이 세미나에서 추가한 처리

1. `BigSolDBv2.2.csv`에 측정 방법 정보를 원 논문 DOI로 연결했습니다.
2. 용매가 **물**, 온도가 **298.15 K(25°C)**, 용해도 실험 구분이 **평형(equilibrium)**인 기록을 선별했습니다.
3. 유효한 SMILES, 유효한 몰분율과 유한한 변환 로그 용해도를 갖는 기록을 사용했습니다.
4. 최종 **645개 측정 기록**을 RDKit의 canonical isomeric SMILES로 묶고, 각 분자의 보고된 로그 용해도 **중앙값**을 정답으로 사용해 **554개 분자**로 집계했습니다.
5. RDKit으로 분자량, MolLogP, TPSA, 수소결합 공여체 수, 회전 가능한 결합 수, 고리 수를 계산했습니다.
6. 고정한 분자 연결 구조 그룹 분할로 개발 **443개**, 평가 **111개**를 나눴습니다. 같은 연결 구조를 양쪽에 중복 배치하지 않았습니다.

반복 측정을 집계한 **뒤의 한 행은 분자 하나**입니다. 원래의 측정 기록 하나와 구별하세요.
`data/molecules.csv`의 `measurement_count`, `measurement_range`, `source_dois`에 집계한 기록 수·보고값 범위·원 측정 논문 DOI를 보존했습니다.
파이프라인의 가공 데이터 해시는 `data/protocol.json`과 노트북의 내장 자산 목록에 있습니다.

## 입력과 정답의 의미

- 입력은 구조에서 계산한 **분자 특성 6개**입니다. 정답이나 다른 모델 예측을 입력에 넣지 않습니다.
- 정답은 `LogS(mol/L)`의 분자별 중앙값입니다. 원본의 mol/L 환산은 순수 용매의 밀도를 사용하므로 **용매 1 L당 용질 몰수**이며 용액 1 L 기준과 구분합니다.
- `y = log10(S)`. `y=-1`은 `S=0.1`, `y=-3`은 `S=0.001`입니다.
- pH·고체 형태·출처별 실험 조건을 모두 동일하게 맞춘 데이터는 아닙니다. 이 차이는 예측의 한계입니다.

## 배포 파일별 출처 구분

| 파일 / 출력 | 출처 |
|---|---|
| `data/molecules.csv`와 노트북의 내장 분자 표 | BigSolDB 2.2를 위 절차로 필터링·집계하고 계산 특성·분할을 추가한 **가공 데이터** |
| `data/reference_predictions.csv` | 이 세미나의 고전/광자 특징 모델이 계산한 **자체 예측 결과**. 원본 실험 측정값으로 인용하지 않음 |
| `data/reservoir_config.json` | 개발 데이터에서 선택한 이 세미나의 **회로·위상 인코딩 설정** |
| `data/protocol.json` | 이 세미나의 **전처리·분할·단위·설정 기록** |
| 노트북의 분자 구조 그림 | 공개 SMILES를 RDKit으로 렌더링한 그림 |
| 회로 그림 | 이 세미나의 선택 회로를 Perceval로 렌더링한 그림 |
| 회귀 직선, 기여도, 확률 분포와 예측 산점도 | **이 세미나의 자체 계산 및 분석 결과**. 원 논문의 Figure를 복제한 것이 아님 |

참고용 기준 예측은 모든 모델의 학습·예측이 끝난 뒤 재현 확인 단계에서만 읽습니다.
현재 결과는 이상적 시뮬레이션이며 실제 QPU의 측정 결과가 아닙니다.

## 재배포 시 보존할 내용

데이터 저자·버전·DOI, CC BY 4.0 링크, 위의 가공 여부를 함께 표시하세요.
원저자가 Quandela나 이 세미나의 모델을 보증·후원한다고 표현하지 않습니다.
이 저장소의 데이터 표시는 제3자 소프트웨어의 라이선스를 변경하지 않습니다.

짧은 인용 문구:

> Data: Krasnov et al., *BigSolDB 2.2* (2026), https://doi.org/10.5281/zenodo.22648301, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Filtered, aggregated and processed. Related paper: https://doi.org/10.1038/s41597-025-05559-8. Model predictions and figures: seminar analysis.
