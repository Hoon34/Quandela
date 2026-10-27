# 분자 구조에서 용해도 예측까지

국민대학교 바이오융합학과 · Quandela 양자머신러닝 세미나 실습 · 2026-10-28

**데이터 출처:** Krasnov et al., [BigSolDB 2.2 (Zenodo, 2026)](https://doi.org/10.5281/zenodo.22648301), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). [관련 논문](https://doi.org/10.1038/s41597-025-05559-8). 물·25°C 조건 선별, 분자별 집계 및 특성 계산을 추가했습니다. **자세한 원본 파일·해시·가공 기록은 [DATA_PROVENANCE.md](DATA_PROVENANCE.md)를 참고하세요.**

발표의 순서에 맞춰 **데이터 불러오기 → 선형 회귀 → 광자 확률 특징 추출 → 그 특징으로 회귀 학습**을 직접 실행합니다.

**[노트북 미리보기](Kookmin_QML_Hub_Demo.ipynb)** · **[노트북 다운로드](https://github.com/Hoon34/Quandela/raw/refs/heads/main/Kookmin_QML_Hub_Demo.ipynb)** · **[전체 ZIP 다운로드](https://github.com/Hoon34/Quandela/archive/refs/heads/main.zip)**

<img src="share/github_qr.png" width="165" alt="QR code linking to https://github.com/Hoon34/Quandela">

학생용 공유 주소: **https://github.com/Hoon34/Quandela** · [발표용 QR PNG](share/github_qr.png) · [QR SVG](share/github_qr.svg)

## 가장 간단한 실행 방법

1. 이 저장소의 **`Kookmin_QML_Hub_Demo.ipynb`**를 다운로드합니다. GitHub의 노트북 미리보기에서 **Download raw file**을 사용하세요. 전체 저장소를 받으려면 **Code → Download ZIP**을 선택해도 됩니다.
2. [Quandela Hub](https://hub.quandela.com/)에서 Cloud로 이동해 로그인하고 [Web IDE](https://cloud.quandela.com/webide)를 엽니다.
3. 사용 가능한 **일반 Python 커널**의 노트북 환경에 `.ipynb`를 업로드해 엽니다.
4. **Restart Kernel and Run All Cells** 또는 **Run All**을 선택합니다. 처음에는 필요한 패키지를 설치하므로 시간이 걸릴 수 있습니다. 설치 후 커널 재시작을 요구하면 재시작 후 처음부터 실행하세요.
5. 셀 아래의 분자 그림, 특성표, 회로 그림, 확률 분포와 예측 산점도를 확인합니다.

노트북 **한 파일 안에 공개 데이터와 고정 회로 설정이 포함**되어 있습니다. `data/`를 함께 업로드하지 않아도 됩니다.
패키지가 이미 설치되어 있으면 데이터 다운로드나 인터넷 연결 없이 계산할 수 있습니다.
QPU 토큰·크레딧·GPU는 사용하지 않습니다. Hub에 로그인하는 것과 QPU 작업을 제출하는 것은 서로 다릅니다.

### Hub 실행 환경 확인

이 배포본은 **Python 3.13 / CPU**에서 전체 실행과 발표 결과 재현을 검증했습니다.
Hub → Cloud → Web IDE의 로그인 진입 경로는 확인했지만, **로그인 후 계정별 Python 커널에서의 실행은 아직 검증하지 않았습니다.**
Web IDE에서 임의 노트북 업로드와 PyTorch·RDKit·MerLin을 설치/실행할 수 있는 Python 커널이 필요합니다.
브라우저 전용 Python(Pyodide/JupyterLite)만 제공되는 경우 이 노트북의 PyTorch 부분을 그대로 실행할 수 없습니다.
해당 경우 아래의 로컬 Jupyter 방법을 사용하거나 교육 담당자에게 서버 Python 환경을 문의하세요.
메뉴 명칭과 커널 제공·패키지 설치 권한은 계정에 따라 다를 수 있습니다.

## 어떤 출력이 나오나요?

| 노트북 순서 | 발표와 연결되는 출력 |
|---|---|
| 데이터 불러오기 | 실제 분자 5개, 분자량·용해도 표와 분자 구조 그림 |
| SMILES → RDKit | Paracetamol의 특성 6개와 실제 숫자 벡터 |
| 선형 회귀 맛보기 | 실제 5개 분자로 점 표시 → 직선 맞춤 → 새 입력 예측 |
| 선형 Ridge 학습 | 개발 443개·평가 111개, 회귀 계수, 선형 모델 점수 |
| 예측 해석 | Paracetamol의 절편 −2.106 + 기여도 약 +0.396 = 예측 −1.709 |
| 광자 특징 추출 | 6모드·3광자·3층 회로와 분자별 입력 위상 |
| 확률 분포 | Paracetamol과 Naringenin의 전체 56개 출력 확률 비교 |
| 확률로 회귀 학습 | 확률 특징 56개에 Ridge 회귀 연결 |
| 최종 평가 | 동일 평가 분자 111개, 양쪽 축 −8~2의 산점도와 RMSE·R² |
| 재현 확인 | 기준 예측과 차이 확인, 결과와 그림을 `outputs/`에 저장 |

플롯은 Hub에서 별도 한글 폰트를 설치하지 않아도 읽히도록 영어 레이블을 사용하며, 설명과 코드는 한국어 안내를 제공합니다.
노트북에는 검증 실행의 출력도 저장되어 있어 GitHub에서 실행 전 결과를 미리 볼 수 있습니다.
학생이 Run All을 실행하면 **데이터에서부터 특징과 모델을 다시 계산**합니다. 저장된 예측을 결과로 대신 표시하지 않습니다.

## 기대 결과와 해석

| 모델 | 평가 RMSE ↓ | 평가 R² ↑ |
|---|---:|---:|
| Linear Ridge | 1.285 | 0.522 |
| Photonic reservoir + Ridge | 1.202 | 0.582 |

광자 회로는 고정하며 마지막 Ridge의 회귀 계수와 절편을 학습합니다. 양자 회로 파라미터의 gradient 학습, 양자 커널, PLS 잔차 보정은 이 실습에 포함하지 않습니다.
기존 평가 분할을 재사용한 후속 실험이며 **양자 우위의 입증이 아닙니다.** 같은 연구에서 RBF 모델의 RMSE는 1.182였습니다.
현재는 이상적 시뮬레이션이며 실제 QPU 측정 결과가 아닙니다. 한계와 불확실성은 노트북 마지막에 적었습니다.

## 로컬 Jupyter에서 실행

Python 3.10 이상이 필요합니다. 이미 사용 중인 Python 환경이 있으면 그 환경을 사용해도 됩니다.

```sh
python -m pip install -r requirements.txt jupyterlab
python -m jupyterlab
```

`Kookmin_QML_Hub_Demo.ipynb`를 열고 같은 환경의 Python 커널을 선택합니다.
정확한 검증 버전은 `requirements-verified.txt`이며 Python 3.13에서 검증한 버전 목록입니다.
이 목록을 다른 Python 버전에 무조건 설치할 필요는 없습니다. 노트북 준비 셀은 없는 패키지만 설치하며 기존 패키지를 일괄 업그레이드하지 않습니다.

## 데이터와 출처

Data: Krasnov, Malikov, Kiseleva, Tatarin, Sosnin & Bezzubov, *BigSolDB 2.2* (2026),
[Zenodo DOI](https://doi.org/10.5281/zenodo.22648301), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
관련 논문: [doi:10.1038/s41597-025-05559-8](https://doi.org/10.1038/s41597-025-05559-8).

물·298.15 K·평형 실험 기록을 선별하고, 같은 canonical isomeric SMILES의 로그 용해도를 중앙값으로 집계했습니다.
RDKit 특성과 고정 분할을 추가했습니다. 목표 단위는 **용매 1 L당 용질 mol의 log10**입니다.
데이터 저자·변경 기록·라이선스는 `DATA_SOURCE_AND_LICENSE.txt`에 있습니다. 재배포할 때 이 안내를 보존하세요.
데이터와 분석 결과가 원저자의 후원이나 보증을 의미하지 않습니다. 의존 라이브러리는 각각의 라이선스를 따릅니다.

## 파일

- `Kookmin_QML_Hub_Demo.ipynb`: 단독 실행 가능한 메인 노트북
- `data/`: 내장 데이터의 검토 가능한 원형. 모델 학습에는 분자 표·설정·분할을 사용하고 기준 예측은 마지막 검증에서만 읽습니다.
- `requirements.txt`: 호환 패키지 범위
- `requirements-verified.txt`: 실제 검증 버전 목록
- `DATA_SOURCE_AND_LICENSE.txt`: 데이터 출처·라이선스·변경 기록
- `DATA_PROVENANCE.md`: 원본 저자·파일 DOI·체크섬·가공 과정과 생성 데이터의 구분
- `share/`: 실제 GitHub 공유 링크와 PNG·SVG QR

발표 PPT나 기업 협력의 비공개 데이터는 포함하지 않습니다.
