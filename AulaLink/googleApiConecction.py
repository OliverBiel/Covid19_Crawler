from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from Abrir_aula import abrir_aula

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly",
          "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly",
          "https://www.googleapis.com/auth/classroom.announcements.readonly",
          "https://www.googleapis.com/auth/classroom.coursework.me",
          "https://www.googleapis.com/auth/classroom.announcements"]


def main():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])
    coursework = service.courses().announcements().list(courseId="253088987193", pageSize=3).execute()
    assignments = service.courses().courseWork().list(courseId="253087118700", pageSize=3).execute()

    # if not courses:
    #     print('No courses found.')
    # else:
    #     print('Courses:')
    #     for course in courses:
    #         print(course['name'], course['id'])
    #
    # print(courses)
    # print(courseworkget)

    #Modelagem e Projeto de Banco de Dados - Turma: UN 253087118700
    #Álgebra e Geometria Analítica - Turma: UN 253088987193

    announcement_ids = []
    assignments_ids = []
    algebra_link = None
    db_link = None
    db_link_activity = None


    for assignment in assignments['courseWork']:            #registra todos os assignments ID's
        assignments_ids.append(assignment['id'])

    for id in assignments_ids:                             #Faz a busca pelo link
        assignmentget = service.courses().courseWork().get(courseId="253087118700", id=id).execute()
        materials = assignmentget['materials']
        try:
            db_link = materials[0]["link"]['url']
            if len(db_link) > 8:
                db_link_activity = assignmentget["alternateLink"]
                break

        except:
            continue

    for announcement in coursework['announcements']:        #registra todos os announcements ID's
        announcement_ids.append(announcement['id'])

    for id in announcement_ids:                             #Faz a busca pelo link
        courseworkget = service.courses().announcements().get(courseId="253088987193", id=id).execute()
        materials = courseworkget['materials']
        try:
            algebra_link = materials[0]["link"]['url']
            if len(algebra_link) > 8:
                break

        except:
            continue

    return algebra_link, db_link, db_link_activity

# courseworkget = service.courses().announcements().get(courseId="253088987193",
#                                                                           id=announcement_id).execute()
#                     materials = courseworkget['materials']
#                     print(materials)
#                     counter = 0
#                     try:
#                         class_link = materials[0]["link"]['url']
#                         if len(class_link) > 8:
#                             return class_link
#
#                     except:
#                         continue

if __name__ == '__main__':
    links = main()
    abrir_aula(links[0], links[1], links[2])
