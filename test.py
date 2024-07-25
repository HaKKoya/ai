import streamlit as st

st.title('_중간고사 대체 시험_')
st.session_state.sum=0

a = st.radio(
    "**1번.** 1 + 1 = ?",
    ["1", "2", "3", "4"],
    index=None,
)
st.write("고른 답 : ", a)
st.session_state.q1 = a
if st.session_state.q1 == '2':
    st.session_state.sum+=5

b = st.radio(
    "**2번.** 1 + 3 = ?",
    ["1", "2", "3", "4"],
    index=None,
)
st.write("고른 답 : ", b)
st.session_state.q2 = b
if st.session_state.q2 == '4':
    st.session_state.sum+=5

c = st.radio(
    "**3번.** 0 + 1 = ?",
    ["1", "2", "3", "4"],
    index=None,
)
st.write("고른 답 : ", c)
st.session_state.q3 = c
if st.session_state.q3 == '1':
    st.session_state.sum+=5

d = st.radio(
    "**4번.** 1 + 2 = ?",
    ["1", "2", "3", "4"],
    index=None,
)
st.write("고른 답 : ", d)
st.session_state.q4 = d
if st.session_state.q4 == '3':
    st.session_state.sum+=5

@st.experimental_dialog("제출 하시겠습니까?")
def vote(item):
    st.write(f"제출 후 수정이 불가능 합니다.")
    if st.button("Submit"):
        st.session_state.vote = {"item": item}
        st.switch_page("pages/result.py")


st.write("수고하셨습니다")
if st.button("제출하기"):
    vote("A")
