Here’s the full content for your `app.py` file. You can copy and paste this into the GitHub file editor when creating the new file:

```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Time Series Oral Exam", layout="centered")

st.title("📊 Time Series Oral Exam")
st.write("Answer each question in the box below. The app will evaluate your response and provide feedback.")

questions = [
    {
        "question": "What is a time series, and how is it different from other types of data?",
        "keywords": ["sequence", "time", "chronological", "trend", "temporal"]
    },
    {
        "question": "What is a time plot, and what kind of patterns can it reveal?",
        "keywords": ["trend", "seasonal", "fluctuation", "time", "axis"]
    },
    {
        "question": "Interpret the following time plot of NYC temperatures. What trend do you observe?",
        "keywords": ["increase", "warming", "trend", "temperature", "rise"],
        "graph": True
    },
    {
        "question": "Using the regression equation y = -1.636 + 0.029x, what is the predicted temperature in 2020?",
        "keywords": ["24.944", "25", "prediction", "regression"]
    }
]

if "step" not in st.session_state:
    st.session_state.step = 0

step = st.session_state.step
q = questions[step]

st.subheader(f"Question {step + 1}")
st.write(q["question"])

if q.get("graph"):
    years = np.arange(1869, 2011)
    temps = -1.636 + 0.029 * years + np.random.normal(0, 0.5, len(years))
    fig, ax = plt.subplots()
    ax.plot(years, temps, label="Annual Mean Temp")
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Annual Mean Temperature in NYC (1869–2010)")
    st.pyplot(fig)

response = st.text_area("Your Answer", height=150)

if st.button("Submit Answer"):
    if not response.strip():
        st.warning("Please enter a response before submitting.")
    else:
        score = sum(1 for kw in q["keywords"] if kw.lower() in response.lower())
        total = len(q["keywords"])
        percent = int((score / total) * 100)
        st.success(f"✅ Your score: {percent}%")
        if percent >= 70:
            st.info("Great job! You covered the key concepts.")
        else:
            st.info("Keep reviewing the material to improve your understanding.")
        if step + 1 < len(questions):
            st.button("Next Question", on_click=lambda: st.session_state.update(step=step + 1))
        else:
            st.balloons()
            st.write("🎉 You've completed the oral exam!")
```

Let me know once you've pasted and committed this file, and I’ll help you finish the deployment!
