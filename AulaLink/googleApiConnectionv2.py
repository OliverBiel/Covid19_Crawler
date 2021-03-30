from googleapiclient.discovery import build
from fetch import Fetch


get_credit = Fetch()
credit = get_credit() #my credentials

service = build('classroom', 'v1', credentials=credit)
get_data = service.courses()
soup = get_data.list().execute()

data = soup['courses']

name_course = [name['name'] for name in data] #name of the course
course_id = [id['id'] for id in data] #course ID

announcement = get_data.announcements()
announcement_data = announcement.list(course_id[0], page_token=10).execute()
print(announcement_data)