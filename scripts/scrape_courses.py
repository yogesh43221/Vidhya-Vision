import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

# Base URL of Analytics Vidhya's free courses page
BASE_URL = "https://courses.analyticsvidhya.com/collections/courses"

# Function to extract course rating from a soup object
def extract_rating(soup):
    """Extract course rating."""
    rating_match = re.search(r'(\d\.\d)/5', soup.get_text())
    return rating_match.group(1) if rating_match else 'N/A'

# Function to extract course level from a soup object
def extract_level(soup):
    """Extract course level."""
    levels = ["Beginner", "Intermediate", "Advanced"]
    for level in levels:
        if soup.find(string=re.compile(level, re.IGNORECASE)):
            return level
    return 'N/A'

# Function to extract course curriculum from a soup object
def extract_curriculum(soup):
    """Extract course curriculum/topics."""
    # Find the section containing the course chapters
    curriculum_section = soup.find('ul', class_='course-curriculum__chapter-list')
    if not curriculum_section:
        return 'N/A'

    # Initialize an empty list to store curriculum content
    curriculum = []

    # Loop through each chapter
    chapters = curriculum_section.find_all('li', class_='course-curriculum__chapter')
    for chapter in chapters:
        chapter_title = chapter.find('h5', class_='course-curriculum__chapter-title')
        if chapter_title:
            curriculum.append(chapter_title.get_text(strip=True))  # Add chapter title

        # Extract lesson titles within the chapter
        lessons = chapter.find_all('span', class_='course-curriculum__chapter-lesson')
        for lesson in lessons:
            lesson_title = lesson.get_text(strip=True)
            if lesson_title:
                curriculum.append(lesson_title)  # Add lesson title

    # Join all curriculum topics with commas, and return the result
    return ', '.join(curriculum) if curriculum else 'N/A'

# Function to parse an individual course page
def parse_course_page(course_url):
    """Fetch and parse details from an individual course page."""
    response = requests.get(course_url)
    if response.status_code != 200:
        print(f"Failed to fetch course page: {course_url}")
        return {
            'course_description': 'N/A',
            'course_duration': 'N/A',
            'course_rating': 'N/A',
            'course_level': 'N/A',
            'instructor_name': 'N/A',
            'who_should_enroll': 'N/A',
            'course_curriculum': 'N/A'  # Add the curriculum here
        }

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract course description
    course_description = soup.find('section', class_='section__body')
    course_description = course_description.get_text(strip=True) if course_description else 'N/A'

    # Extract course duration
    duration_tag = soup.find('h4', text=re.compile(r'^\d+\s\w+', re.IGNORECASE))
    course_duration = duration_tag.get_text(strip=True) if duration_tag else 'N/A'

    # Extract course rating
    course_rating = extract_rating(soup)

    # Extract course level
    course_level = extract_level(soup)

    # Extract instructor name
    instructor_tag = soup.find('h4', class_='section__subheading')
    instructor_name = instructor_tag.get_text(strip=True) if instructor_tag else 'N/A'

    # Extract "Who Should Enroll" section
    who_should_enroll = 'N/A'
    enroll_heading = soup.find('h3', string=re.compile(r'Who Should Enroll', re.IGNORECASE))
    if enroll_heading:
        enroll_section = enroll_heading.find_next('ul')
        if enroll_section:
            enroll_items = enroll_section.find_all('li')
            who_should_enroll = ', '.join(item.get_text(strip=True) for item in enroll_items) if enroll_items else 'N/A'

    # Extract course curriculum
    course_curriculum = extract_curriculum(soup)

    return {
        'course_description': course_description,
        'course_duration': course_duration,
        'course_rating': course_rating,
        'course_level': course_level,
        'instructor_name': instructor_name,
        'who_should_enroll': who_should_enroll,
        'course_curriculum': course_curriculum  # Add curriculum in the return data
    }

# Function to extract course data from a single page
def get_course_data(page_url):
    response = requests.get(page_url)
    if response.status_code != 200:
        print(f"Failed to fetch page: {page_url}")
        return []

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    course_items = soup.find_all('li', class_='products__list-item')
    courses = []

    for item in course_items:
        course_data = {}

        # Extract course title
        title_tag = item.find('h3')
        course_data['course_title'] = title_tag.get_text(strip=True) if title_tag else 'N/A'

        # Extract course URL
        url_tag = item.find('a', class_='course-card')
        relative_url = url_tag['href'] if url_tag else 'N/A'
        course_data['course_url'] = (
            relative_url if relative_url.startswith('http')
            else 'https://courses.analyticsvidhya.com' + relative_url
        ) if relative_url != 'N/A' else 'N/A'

        # Extract lesson count
        lesson_count_tag = item.find('span', class_='course-card__lesson-count')
        lesson_count = lesson_count_tag.get_text(strip=True) if lesson_count_tag else 'N/A'
        course_data['lesson_count'] = int(re.search(r'\d+', lesson_count).group()) if re.search(r'\d+', lesson_count) else 0

        # Extract price
        price_tag = item.find('span', class_='course-card__price')
        course_data['price'] = price_tag.get_text(strip=True) if price_tag else 'Free'

        # Extract reviews
        reviews_tag = item.find('span', class_='review__stars-count')
        reviews = reviews_tag.get_text(strip=True) if reviews_tag else 'No reviews'
        course_data['reviews'] = (
            int(re.search(r'-?\d+', reviews).group()) if re.search(r'-?\d+', reviews) else 'No reviews'
        )
        if isinstance(course_data['reviews'], int) and course_data['reviews'] < 0:
            course_data['reviews'] = abs(course_data['reviews'])

        # Fetch additional details from the course page
        if course_data['course_url'] != 'N/A':
            detailed_data = parse_course_page(course_data['course_url'])
            course_data.update(detailed_data)

        courses.append(course_data)

    return courses

# Function to save cleaned data to CSV with the correct column order
def save_to_csv(courses, filename="courses_data11.csv"):
    # Specify the improved column order
    column_order = [
        'course_title',
        'course_url',
        'course_description',
        'course_curriculum',
        'course_level',
        'course_rating',
        'lesson_count',
        'price',
        'reviews',
        'course_duration',
        'instructor_name',
        'who_should_enroll'  # Ensure this is at the end as it's more descriptive
    ]
    
    # Ensure the data directory exists
    output_file = os.path.join("data", filename)  # Save to 'data' folder
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Create a DataFrame from the courses data
    df = pd.DataFrame(courses)
    
    # Ensure the DataFrame has the correct column order
    df = df[column_order]
    
    # Save the DataFrame to the specified location
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Data saved to {output_file}")


# Main function to scrape all courses across multiple pages
def scrape_all_courses():
    all_courses = []
    current_page = 1
    while True:
        page_url = f"{BASE_URL}?page={current_page}"
        print(f"Scraping page {current_page}...")
        courses = get_course_data(page_url)
        
        # If no courses are found on this page, break the loop (end of pagination)
        if not courses:
            print(f"No courses found on page {current_page}. Ending the scraping process.")
            break
        
        all_courses.extend(courses)
        current_page += 1  # Move to the next page

    return all_courses


# Main execution
if __name__ == "__main__":
    print("Starting the scraping process...")
    courses = scrape_all_courses()
    save_to_csv(courses)
