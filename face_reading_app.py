import cv2
import dlib
import numpy as np
from imutils import face_utils

# --- Dlib 설정 및 랜드마크 인덱스 ---
predictor_path = "shape_predictor_68_face_landmarks.dat" 

# Dlib 얼굴 인식기와 랜드마크 예측기 초기화
detector = dlib.get_frontal_face_detector()
try:
    predictor = dlib.shape_predictor(predictor_path)
except Exception as e:
    print(f"오류: 랜드마크 파일을 찾을 수 없습니다. 경로를 확인하세요: {predictor_path}")
    print("shape_predictor_68_face_landmarks.dat 파일을 다운로드하여 이 폴더에 넣어주세요.")
    exit()

# Dlib 68점 랜드마크 인덱스 (관상 분석에 사용)
NOSE_TIP = 30           # 코 끝 (준두)
NOSE_BRIDGE_TOP = 27    # 코 뿌리 (산근)
LEFT_EYEBROW_START = 17 # 왼쪽 눈썹 시작점
RIGHT_EYEBROW_END = 26  # 오른쪽 눈썹 끝점
MOUTH_TOP = 51          # 윗입술 중앙
MOUTH_BOTTOM = 57       # 아랫입술 중앙


# --- 관상 해설 함수 (결과 깨짐 방지를 위해 영문 사용) ---

def analyze_nose_length(nose_length):
    """코 길이에 따른 재미있는 재물운 해설 (Wealth)"""
    if nose_length > 100:
        return "Wealth: EXCELLENT! (Big Nose for Riches)"
    elif nose_length > 70:
        return "Wealth: GOOD! (Stable Fortune)"
    else:
        return "Wealth: OK! (Focus on People/Luck)"

def analyze_eyebrow_length(eyebrow_length):
    """눈썹 길이에 따른 재미있는 인복/형제운 해설 (Luck)"""
    if eyebrow_length > 150:
        return "Luck: EXCELLENT! (Great support from people)"
    elif eyebrow_length > 100:
        return "Luck: GOOD! (Harmonious family/friends)"
    else:
        return "Luck: NORMAL! (Need independent effort)"

def analyze_mouth_thickness(mouth_thickness):
    """입술 두께에 따른 재미있는 의식주/애정운 해설 (Affection)"""
    if mouth_thickness > 40:
        return "Affection: GREAT! (Passionate love/Stable life)"
    elif mouth_thickness > 25:
        return "Affection: GOOD! (Balanced love/life)"
    else:
        return "Affection: NORMAL! (Clear thinking, sometimes reserved)"


# --- 메인 루프 ---
def run_face_reading():
    cap = cv2.VideoCapture(0) # 0번 카메라 사용
    
    if not cap.isOpened():
        print("Error: 카메라를 열 수 없습니다. 카메라 연결 및 권한 설정을 확인하세요.")
        return

    print("카메라 실행. 'q'를 눌러 종료하세요.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 좌우 반전 (거울 모드) 및 그레이스케일 변환
        frame = cv2.flip(frame, 1) 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

        # 얼굴 감지
        faces = detector(gray, 0)

        # 감지된 모든 얼굴 처리
        for rect in faces:
            # 랜드마크 예측
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # 1. 얼굴 영역 좌표 추출 및 그리기
            x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # --- A. 코 길이 (재물운) 분석 ---
            pt_27 = shape[NOSE_BRIDGE_TOP]
            pt_30 = shape[NOSE_TIP]
            nose_length = np.abs(pt_30[1] - pt_27[1]) 
            result_nose = analyze_nose_length(nose_length)

            # --- B. 눈썹 길이 (인복/형제운) 분석 ---
            pt_eb_start = shape[LEFT_EYEBROW_START]
            pt_eb_end = shape[RIGHT_EYEBROW_END]
            eyebrow_length = np.abs(pt_eb_end[0] - pt_eb_start[0])
            result_eyebrow = analyze_eyebrow_length(eyebrow_length)

            # --- C. 입술 두께 (애정운/의식주) 분석 ---
            pt_m_top = shape[MOUTH_TOP]
            pt_m_bottom = shape[MOUTH_BOTTOM]
            mouth_thickness = np.abs(pt_m_bottom[1] - pt_m_top[1])
            result_mouth = analyze_mouth_thickness(mouth_thickness)
            
            # --- 결과 표시 ---
            
            # 1. 코 측정 지점 표시 (빨간색)
            cv2.circle(frame, tuple(pt_27), 3, (0, 0, 255), -1) 
            cv2.circle(frame, tuple(pt_30), 3, (0, 0, 255), -1) 
            
            # 2. 결과 텍스트 표시 (여러 줄로 분리)
            text_y_start = y + h + 20
            
            cv2.putText(frame, f"Nose (Wealth): {result_nose}", 
                        (x, text_y_start), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            cv2.putText(frame, f"Eyebrow (Luck): {result_eyebrow}", 
                        (x, text_y_start + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            cv2.putText(frame, f"Mouth (Affection): {result_mouth}", 
                        (x, text_y_start + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
        # 결과 화면 출력
        cv2.imshow("Funny Face Reading App", frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 종료 작업
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_face_reading()