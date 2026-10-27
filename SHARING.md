# GitHub 배포와 QR

## 올릴 파일

이 폴더의 내용을 GitHub 저장소 최상단에 올리면 됩니다.
메인 파일은 `Kookmin_QML_Hub_Demo.ipynb`입니다. 데이터와 실행 출력이 포함되어 있으므로 GitHub에서 바로 미리 볼 수 있습니다.
`outputs/`나 실행 환경 폴더를 추가할 필요는 없습니다.

## 학생에게 줄 링크

저장소의 **메인 페이지 URL**을 권장합니다. README에서 다운로드·Hub 실행 순서를 함께 볼 수 있습니다.
GitHub 미리보기의 노트북 파일만 가리키는 링크도 가능하지만, 저장소 페이지를 주면 실행 안내를 놓치지 않습니다.

QR은 실제 공개 저장소 URL이 결정된 뒤 생성하세요. 정해지지 않은 저장소나 임시 주소를 학생에게 제공하지 마세요.

## QR 생성 도구

실제 GitHub 저장소 URL을 인자로 주면 `share/github_qr.png`와 `share/github_qr.svg`를 만듭니다.
QR 라이브러리는 배포 준비에만 필요하며 학생 실습에는 필요하지 않습니다.

```sh
python -m pip install "qrcode[pil]>=8,<9"
python tools/make_share_qr.py --repo-url YOUR_ACTUAL_GITHUB_REPOSITORY_URL
```

이 도구는 주소를 외부 QR 서비스로 전송하지 않고 로컬에서 QR을 생성합니다.
실행 후 휴대폰으로 QR을 읽어 로그인하지 않은 상태에서도 README와 노트북에 접근되는지 확인하세요.

## Hub에서 강의 전 확인할 것

1. 교육에 사용할 실제 Quandela 계정으로 [Cloud Web IDE](https://cloud.quandela.com/webide)에 로그인합니다.
2. 일반 Python 커널에서 메인 노트북만 업로드하고 Run All을 실행합니다.
3. 패키지 설치, RDKit 분자 그림, Perceval 회로 그림, 확률 56개, RMSE 1.285 / 1.202 출력을 확인합니다.

로컬 CPU 전체 실행은 검증됐지만 로그인한 Hub 커널에서의 실행은 별도 확인이 필요합니다.
이 실습은 QPU 제출 코드나 토큰을 포함하지 않습니다.
