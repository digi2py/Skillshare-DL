import sys, os
from skillshare import Skillshare, splash
from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare(“skillshare_user_=9699a81e8b0e631c8f556e9c145aeaef44abac46a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2218562958%22%3Bi%3A1%3Bs%3A28%3A%22wihiba%40livinginsurance.co.uk%22%3Bi%3A2%3Bi%3A7776000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A9%3A%22570603570%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222021-03-31%2017%3A00%3A10%22%3Bs%3A10%3A%22touch_time%22%3Bs%3A19%3A%222021-03-31%2017%3A00%3A51%22%3B%7D%7D”)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
