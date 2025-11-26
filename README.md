# 🐍 재미로 보는 관상 분석 프로그램 (Face-Reading App)이 프로젝트는 Python의 OpenCV와 Dlib 라이브러리를 활용하여 웹캠으로 촬영된 얼굴을 실시간으로 분석하고, 측정된 특징(코의 길이, 눈썹 길이, 입술 두께)을 바탕으로 재미있는 관상 해설을 제공하는 데모 프로그램입니다. 

🎭✨ 주요 기능실시간 얼굴 인식: 웹캠을 통해 사용자의 얼굴을 감지합니다.

Dlib 랜드마크 분석: 얼굴의 주요 특징점(68개)을 추출하여 코, 눈썹, 입술의 위치를 정확히 파악합니다.관상 요소 측정:코 길이: 재물운 분석 (Wealth)눈썹 길이: 인복/형제운 분석 (Luck)입술 두께: 애정운/의식주 분석 (Affection)한글 결과 출력: Pillow (PIL) 라이브러리를 사용하여 OpenCV의 한글 출력 문제를 해결하고, 분석 결과를 한글로 표시합니다.

 💻 실행 환경 및 설치이 프로젝트는 Conda 환경에서 설치하는 것을 권장하며, 특정 폰트 파일이 필요합니다.
 
 1. Conda 환경 설정안정적인 실행을 위해 Python 3.8 또는 3.9 환경을 사용합니다.Bash# 1. 새로운 Conda 환경 생성
conda create -n face_env python=3.9 

# 2. 환경 활성화
 conda activate face_env 
2. 필수 라이브러리 설치face_env 환경이 활성화된 상태에서, 다음 라이브러리를 설치합니다.Bash# OpenCV, Dlib, numpy, imutils 설치
 conda install -c conda-forge dlib opencv numpy imutils

# 한글 출력을 위한 Pillow (PIL) 설치
conda install pillow
3. 필수 파일 준비프로젝트 폴더 (face_reading_project) 안에 다음 두 파일이 반드시 존재해야 합니다.파일명용도다운로드 링크shape_predictor_68_face_landmarks.datDlib의 얼굴 랜드마크 예측 모델Download Link (다운로드 후 압축 해제 필요)malgun.ttf (또는 다른 한글 폰트)결과 화면에 한글을 출력하기 위한 폰트Windows 사용자: C:\Windows\Fonts에서 복사🚀 프로그램 실행 방법VS Code 실행: 프로젝트 폴더에서 face_reading_app.py 파일을 엽니다.환경 확인: VS Code 터미널에서 **(face_env)**가 활성화되어 있는지 확인합니다.실행: 다음 명령어를 입력하여 프로그램을 실행합니다.Bashpython face_reading_app.py

종료: 프로그램 실행 중 q 키를 누르면 종료됩니다.💡 코드 참고 사항한글 출력: cv2.putText 대신 Pillow 라이브러리를 사용하여 이미지를 처리하기 때문에 한글이 정상적으로 출력됩니다.관상 기준: 관상 분석에 사용된 길이(픽셀 수) 기준은 재미를 위한 임의의 값이며, 실제 관상학적 해석과는 다를 수 있습니다.주의: 폰트 경로 (FONT_PATH = "malgun.ttf")를 사용하는 폰트 파일 이름으로 정확히 수정해야 합니다.
