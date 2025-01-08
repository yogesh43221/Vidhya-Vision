import streamlit as st
st.set_page_config(page_title="Course Finder", page_icon=":mag_right:", layout="wide")
import pandas as pd
from PIL import Image
import visualizations


# CSS for center alignment of images
center_image_css = """
<style>
.center-image {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
}
</style>
"""

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "visualizations"])

# Load your data
data_path = "data/courses_data_final.csv"
df_courses = pd.read_csv(data_path, encoding='ISO-8859-1')

# Display CSS for images center alignment
st.markdown(center_image_css, unsafe_allow_html=True)

# Navigate to selected page
if page == "Home":
    # Your existing app code
    st.title("Course Finder")

    # Add a larger logo at the top of the page
    logo_image_path = "images/VIDHYA_VISION.png"
    logo_image = Image.open(logo_image_path)
    st.markdown(
        "<h1 style='text-align: center;'>"
        "<span style='color: lightgreen;'>VIDHYA VISION</span> Course Finder</h1>",
        unsafe_allow_html=True
    )

    st.image(logo_image, use_container_width=True)

    theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])
    if theme == "Dark":
        st.markdown(
            """
            <style>
            body { background-color: #2E2E2E; color: white; }
            </style>
            """, unsafe_allow_html=True
        )


    if st.sidebar.button("Reset Filters"):
        st.rerun()

    # Sidebar: Filter for "Free" or "Paid" courses
    st.sidebar.title("Filter by Course Type")
    course_type = st.sidebar.selectbox("Select Course Type", ["All", "Free", "Paid"])

    # Sidebar: Rating filter
    st.sidebar.title("Filter by Rating")
    min_rating = st.sidebar.slider("Minimum Rating", min_value=0.0, max_value=5.0, value=0.0, step=0.1)

    # Sidebar: Course level filter
    st.sidebar.title("Filter by Course Level")
    course_level = st.sidebar.selectbox("Select Course Level", ["All", "Beginner", "Intermediate", "Advanced"])

    # Sidebar: Minimum duration filter
    st.sidebar.title("Filter by Duration")
    min_duration = st.sidebar.slider("Minimum Duration (in minutes)", min_value=0, max_value=3300, value=0, step=10)

    # Search box
    search_query = st.text_input("Search for a course:", "", help="Type and see suggestions")

    # Display search suggestions based on the query
    if search_query:
        search_suggestions = df_courses['course_title'].tolist()
        suggestions = [title for title in search_suggestions if search_query.lower() in title.lower()]
        if suggestions:
            st.write("Suggestions:", suggestions[:5])

    # Display header
    # Streamlit title with custom HTML styling
    st.markdown(
        """
        <style>
        .title {
            color: white;
            font-size: 36px;
            text-align: center;
        }
        .highlight {
            color: red;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="title">Smart Search Tool for <span class="highlight">ANALYTICS VIDHYA</span> Courses</h1>', unsafe_allow_html=True)
    st.markdown("Find courses based on your search preferences.")

    # Create a copy of the dataframe for filtering
    filtered_courses = df_courses.copy()

    # Show all courses if no filters are applied
    if (
        course_type == "All"
        and course_level == "All"
        and min_duration == 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses.copy()

    # Show only Free courses if course_type is "Free" and no other filters are applied
    elif (
        course_type == "Free"
        and course_level == "All"
        and min_duration == 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[df_courses["price"] == "Free"]

    # Show only Paid courses if course_type is "Paid" and no other filters are applied
    elif (
        course_type == "Paid"
        and course_level == "All"
        and min_duration == 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[df_courses["price"] != "Free"]

    # Filter by Course Level only
    elif (
        course_type == "All"
        and course_level != "All"
        and min_duration == 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            df_courses["course_level"].str.contains(course_level, case=False, na=False)
        ]

    # Filter by Minimum Duration only
    elif (
        course_type == "All"
        and course_level == "All"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[df_courses["course_duration"] >= min_duration]

    # Filter by Minimum Rating only
    elif (
        course_type == "All"
        and course_level == "All"
        and min_duration == 0
        and min_rating > 0.0
        and not search_query
    ):
        filtered_courses = df_courses[df_courses["course_rating"] >= min_rating]

    # Filter by Course Type and Course Level
    elif (
        course_type != "All"
        and course_level != "All"
        and min_duration == 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["price"] == course_type if course_type == "Free" else df_courses["price"] != "Free")
            & (df_courses["course_level"].str.contains(course_level, case=False, na=False))
        ]

    # Filter by Minimum Duration only for Beginner level
    elif (
        course_type == "All"
        and course_level == "Beginner"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["course_duration"] >= min_duration)
            & (df_courses["course_level"].str.contains("Beginner", case=False, na=False))
        ]

    # Filter by Minimum Duration only for Intermediate level
    elif (
        course_type == "All"
        and course_level == "Intermediate"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["course_duration"] >= min_duration)
            & (df_courses["course_level"].str.contains("Intermediate", case=False, na=False))
        ]

    # Filter by Minimum Duration only for Advanced level
    elif (
        course_type == "All"
        and course_level == "Advanced"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["course_duration"] >= min_duration)
            & (df_courses["course_level"].str.contains("Advanced", case=False, na=False))
        ]

    # Filter by Minimum Duration only for All levels
    elif (
        course_type == "All"
        and course_level == "All"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[df_courses["course_duration"] >= min_duration]

    # Filter Free courses by Minimum Duration and Beginner level
    elif (
        course_type == "Free"
        and course_level == "Beginner"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["price"] == "Free")
            & (df_courses["course_duration"] >= min_duration)
            & (df_courses["course_level"].str.contains("Beginner", case=False, na=False))
        ]

    # Filter Paid courses by Minimum Duration and Beginner level
    elif (
        course_type == "Paid"
        and course_level == "Beginner"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["price"] != "Free")
            & (df_courses["course_duration"] >= min_duration)
            & (df_courses["course_level"].str.contains("Beginner", case=False, na=False))
        ]

    # Filter Free courses by Minimum Duration and Intermediate level
    elif (
        course_type == "Free"
        and course_level == "Intermediate"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["price"] == "Free")
            & (df_courses["course_duration"] >= min_duration)
            & (df_courses["course_level"].str.contains("Intermediate", case=False, na=False))
        ]

    # Filter Paid courses by Minimum Duration and Intermediate level
    elif (
        course_type == "Paid"
        and course_level == "Intermediate"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["price"] != "Free")
            & (df_courses["course_duration"] >= min_duration)
            & (df_courses["course_level"].str.contains("Intermediate", case=False, na=False))
        ]

    # Filter Free courses by Minimum Duration and Advanced level
    elif (
        course_type == "Free"
        and course_level == "Advanced"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["price"] == "Free")
            & (df_courses["course_duration"] >= min_duration)
            & (df_courses["course_level"].str.contains("Advanced", case=False, na=False))
        ]

    # Filter Paid courses by Minimum Duration and Advanced level
    elif (
        course_type == "Paid"
        and course_level == "Advanced"
        and min_duration > 0
        and min_rating == 0.0
        and not search_query
    ):
        filtered_courses = df_courses[
            (df_courses["price"] != "Free")
            & (df_courses["course_duration"] >= min_duration)
            & (df_courses["course_level"].str.contains("Advanced", case=False, na=False))
        ]


    # Filter by all combined filters
    else:
        filtered_courses = df_courses.copy()

        # Filter by course type
        if course_type == "Free":
            filtered_courses = filtered_courses[filtered_courses["price"] == "Free"]
        elif course_type == "Paid":
            filtered_courses = filtered_courses[filtered_courses["price"] != "Free"]

        # Filter by course level
        if course_level != "All":
            filtered_courses = filtered_courses[
                filtered_courses["course_level"].str.contains(course_level, case=False, na=False)
            ]

        # Filter by minimum duration
        if min_duration > 0:
            filtered_courses = filtered_courses[
                filtered_courses["course_duration"] >= min_duration
            ]

        # Filter by minimum rating
        if min_rating > 0.0:
            filtered_courses = filtered_courses[
                filtered_courses["course_rating"] >= min_rating
            ]

        # Filter by search query
        if search_query:
            filtered_courses = filtered_courses[
                filtered_courses["course_title"].str.contains(search_query, case=False, na=False)
            ]

    # Display filtered courses
    if filtered_courses.empty:
        st.write("No courses found matching your criteria.")
    else:
        for index, course in filtered_courses.iterrows():
            st.markdown(
                f"""
                <div style="border: 1px solid #dddddd; padding: 15px; margin-bottom: 20px; border-radius: 10px;">
                    <h3 style="color: yellow;">{course['course_title']}</h3>
                    <ul>
                        {"".join([f"<li>{point.strip()}</li>" for point in course['course_description'].split('.') if point.strip()])}
                    </ul>
                    <p><strong>Price:</strong> <span style="color: {'#228B22' if course['price'] == 'Free' else '#FF8C00'};">{course['price']}</span></p>
                    <p><strong>Rating:</strong> <span style="color: #FFD700;">{course['course_rating']} ⭐</span></p>
                    <p><strong>Duration:</strong> {course['course_duration']} minutes</p>
                    <a href="{course['course_url']}" target="_blank" style="
                        display: inline-block;
                        background-color: #007BFF;
                        color: white;
                        padding: 8px 16px;
                        text-decoration: none;
                        border-radius: 5px;
                        font-weight: bold;
                        margin-top: 10px;">Access Course</a>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Dynamic Statistics
    st.sidebar.markdown("### Course Statistics")
    st.sidebar.write(f"Total Courses: {len(df_courses)}")
    st.sidebar.write(f"Average Rating: {df_courses['course_rating'].mean():.1f} ⭐")
    st.sidebar.write(f"Free Courses: {len(df_courses[df_courses['price'] == 'Free'])}")
    st.sidebar.write(f"Paid Courses: {len(df_courses[df_courses['price'] != 'Free'])}")


    # Footer note
    st.sidebar.markdown("Made with ❤️ by [Yogesh Jadhav](https://www.linkedin.com/in/yogesh-jadhav-60548020a/)")

    # Footer with center alignment
    footer_image_path = "images/FOOTER.png"
    footer_image = Image.open(footer_image_path)
    st.image(footer_image, use_container_width=True)

# Visualizations page logic
elif page == "visualizations":
    # Import visualizations here, avoiding circular import
    visualizations.show()

    # Footer with center alignment
    footer_image_path = "images/FOOTER.png"
    footer_image = Image.open(footer_image_path)
    st.image(footer_image, use_container_width=True)