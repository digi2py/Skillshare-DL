import sys, os
from skillshare import Skillshare, splash
from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare(“skillshare_user_= 9699a81e8b0e631c8f556e9c145aeaef44abac46a”)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
