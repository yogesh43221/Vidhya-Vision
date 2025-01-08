import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("Visualizations")
    st.write("Explore various insights about the courses.")

    # Load the data
    data_path = "data/courses_data_final.csv"
    df_courses = pd.read_csv(data_path, encoding='ISO-8859-1')  # Adjust encoding if necessary

    # Course Rating Distribution Visualization
    st.subheader("Course Rating Distribution")
    fig, ax = plt.subplots()
    df_courses['course_rating'].hist(bins=10, ax=ax, color='skyblue')
    ax.set_xlabel("Rating")
    ax.set_ylabel("Number of Courses")
    ax.set_title("Distribution of Ratings")
    st.pyplot(fig)

    # Bar chart for ratings distribution
    ratings_dist = df_courses['course_rating'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(ratings_dist.index, ratings_dist.values, color='skyblue')
    ax.set_title("Ratings Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Number of Courses")
    st.pyplot(fig)

    # Featured Courses: Top courses with rating 4.5 or higher
    st.markdown("### Featured Courses")
    top_courses = df_courses[df_courses['course_rating'] >= 4.5].head(3)
    for index, course in top_courses.iterrows():
        st.markdown(f"**{course['course_title']}** - {course['course_rating']} ⭐")
        st.write(f"Price: {course['price']}")
        st.write(f"[Access Course]({course['course_url']})")

    # Course Comparison Feature
    selected_courses = st.multiselect(
        "Select courses to compare", df_courses['course_title'].tolist()
    )

    if len(selected_courses) > 1:
        comparison_df = df_courses[df_courses['course_title'].isin(selected_courses)]
        st.markdown("### Comparison of Selected Courses")
        for index, course in comparison_df.iterrows():
            st.markdown(f"**{course['course_title']}** - {course['course_rating']} ⭐")
            st.write(f"Price: {course['price']}")
            st.write(f"Level: {course['course_level']}")
            st.write(f"[Access Course]({course['course_url']})")
