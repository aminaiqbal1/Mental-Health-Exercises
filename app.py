import streamlit as st
import datetime

# Title of the application
st.title("Mental Health App")

# Introduction
st.write("Welcome to the Mental Health App! This app helps you with mindfulness exercises, tracks your mood, and provides helpful resources.")

# Mindfulness exercises
st.header("Mindfulness Exercises")
st.write("Here are some exercises to help you relax and focus:")

exercises = [
    "1. Deep Breathing: Take deep breaths in and out slowly.",
    "2. Body Scan: Close your eyes and notice how each part of your body feels.",
    "3. Mindful Walking: Walk slowly and notice the sensations in your feet.",
    "4. Visualization: Imagine a peaceful place and focus on the details."
]

for exercise in exercises:
    st.write(exercise)

# Mood tracking
st. sidebar.header("Mood Tracking")
st. sidebar.write("Track how you are feeling today:")

mood = st. sidebar.selectbox("How are you feeling today?", ["Happy", "Sad", "Angry", "Anxious", "Relaxed", "Excited"])

# Save the mood to a list (In a real application, you would save this to a database)
mood_list = []
if st.button("Save Mood"):
    mood_list.append((datetime.date.today(), mood))
    st.write("Mood saved!")
else:
    st.write("Your mood is not saved yet. Click the button to save your mood.")

# Display past moods
st.write("Your mood history:")
for date, mood in mood_list:
    st.write(f"{date}: {mood}")

# Personalized recommendations
st.header("Personalized Recommendations")
st.write("Here are some resources to help you based on how you feel:")

if mood == "Happy":
    st.write("Keep up the good mood! Here are some ways to maintain your happiness:")
    st.write("- Spend time with loved ones.")
    st.write("- Do activities you enjoy.")
elif mood == "Sad":
    st.write("It's okay to feel sad sometimes. Here are some things that might help:")
    st.write("- Talk to a friend or family member.")
    st.write("- Write down your feelings in a journal.")
elif mood == "Angry":
    st.write("Feeling angry is normal. Try these tips to calm down:")
    st.write("- Take deep breaths.")
    st.write("- Take a break and walk away from the situation.")
elif mood == "Anxious":
    st.write("Anxiety can be tough. Here are some things you can try:")
    st.write("- Practice mindfulness exercises.")
    st.write("- Talk to someone you trust.")
elif mood == "Relaxed":
    st.write("It's great that you're feeling relaxed! Keep it up with these tips:")
    st.write("- Continue doing mindfulness exercises.")
    st.write("- Maintain a healthy lifestyle.")
elif mood == "Excited":
    st.write("Excitement is wonderful! Here are some ways to channel your energy:")
    st.write("- Start a new project or hobby.")
    st.write("- Share your excitement with friends.")

# Ending note
st.write("Remember, it's important to take care of your mental health. If you need more help, don't hesitate to reach out to a trusted adult or mental health professional.")

