import streamlit as st
import pandas as pd
import datetime
import os

# 제목
st.title("간단한 설문조사")

# 입력 폼
name = st.text_input("이름을 입력해 주세요:")
email = st.text_input("이메일 주소를 입력해 주세요:")
age = st.number_input("나이를 입력해 주세요:", min_value=0, max_value=120, step=1)
satisfaction = st.radio("서비스 만족도는?", ['매우 만족', '만족', '보통', '불만족'])

# 제출 버튼
if st.button("제출하기"):
    # 수집한 데이터 정리
    response = {
        '응답일시': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        '이름': name,
        '이메일': email,
        '나이': age,
        '만족도': satisfaction
    }

    # CSV 파일 저장
    save_path = "survey_results.csv"
    file_exists = os.path.isfile(save_path)
    df_new = pd.DataFrame([response])

    if file_exists:
        df_existing = pd.read_csv(save_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_csv(save_path, index=False, encoding='utf-8-sig')

    st.success("설문이 정상적으로 제출되었습니다. 감사합니다!")

# 관리자 데이터 확인 (선택적)
with st.expander("📊 수집된 데이터 보기"):
    if os.path.isfile("survey_results.csv"):
        df = pd.read_csv("survey_results.csv")
        st.dataframe(df)
        st.download_button("CSV 다운로드", data=df.to_csv(index=False, encoding='utf-8-sig'),
                           file_name='survey_results.csv', mime='text/csv')
    else:
        st.write("아직 수집된 데이터가 없습니다.")
