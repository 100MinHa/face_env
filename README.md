# 🐍 파이썬으로 만드는 재미있는 관상 분석 프로그램 (OpenCV + Dlib)
카메라를 이용해 얼굴을 인식하고 주요 부위의 특징을 측정하여 재미있는 관상 해설을 제공하는 간단한 파이썬 프로그램의 기본 구조와 핵심 코드를 제시해 드립니다.

이 예시는 OpenCV를 사용하여 카메라에서 프레임을 가져오고, Dlib을 사용하여 얼굴과 랜드마크를 감지하는 데 중점을 둡니다.

🛠️ 1. 필수 라이브러리 설치
이 프로그램을 실행하려면 다음 라이브러리가 필요합니다.

Bash

pip install opencv-python dlib imutils numpy
Dlib 랜드마크 파일: Dlib의 68개 얼굴 랜드마크 모델 파일(shape_predictor_68_face_landmarks.dat)을 다운로드하여 코드와 같은 위치에 두어야 합니다.
