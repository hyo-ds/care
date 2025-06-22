import streamlit as st
import pandas as pd
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ✅ Google Sheet 저장 함수
def save_to_google_sheet(data):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/169duC7FE_lXWBvTbwg6DHDF5078MXpJWOCzQij4Ls8w/edit")
    worksheet = spreadsheet.sheet1

    row = [
        data['응답일시'], data['응답자부서'], data['응답자연락처'],
        data['기관'], data['사업명'], data['카테고리'], data['주제'],
        data['가구'], data['나이'], data['정부24등록'],
        data['접수기관명'], data['지원대상'], data['지원내용'],
        data['신청방법'], data['문의처'], data['온라인URL']
    ]
    worksheet.append_row(row)

# ✅ 전체 저장 함수

def save_data(data):
    save_to_google_sheet(data)

# 🎯 예시 폼 구성 (간단 샘플)
st.title("경상북도 돌봄(보듬)사업 공고 설문조사")

st.markdown("##### 📌 작성자 정보")
부서명 = st.text_input("부서명")
연락처 = st.text_input("연락처")
기관 = st.text_input("기관명")
사업명 = st.text_input("사업명")
카테고리 = st.text_input("카테고리")
주제 = st.text_input("주제")
가구 = st.text_input("가구")
나이 = st.text_input("나이")
정부24등록 = st.selectbox("정부24 등록여부", ['예', '아니오'])
접수기관명 = st.text_input("접수기관명")
지원대상 = st.text_area("지원대상")
지원내용 = st.text_area("지원내용")
신청방법 = st.text_area("신청방법")
문의처 = st.text_input("문의처")
온라인URL = st.text_input("온라인 URL")

if st.button("제출하기"):
    data = {
        '응답일시': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        '응답자부서': 부서명,
        '응답자연락처': 연락처,
        '기관': 기관,
        '사업명': 사업명,
        '카테고리': 카테고리,
        '주제': 주제,
        '가구': 가구,
        '나이': 나이,
        '정부24등록': 정부24등록,
        '접수기관명': 접수기관명,
        '지원대상': 지원대상,
        '지원내용': 지원내용,
        '신청방법': 신청방법,
        '문의처': 문의처,
        '온라인URL': 온라인URL
    }

    save_data(data)
    st.success("성공적으로 Google Sheet에 저장되었습니다!")
