from exif import Image, DATETIME_STR_FORMAT
from datetime import date, datetime

class imageClient:
  def get_int_input(prompt, min_, max_, type_=int):
    while True:
      try:
        user_input = int(input(prompt))
        if isinstance(user_input, type_):
          if min_ <= user_input <= max_:
            break
          else:
            print(f"{user_input} must be between {min_} and {max_}")
      except ValueError:
        print("Input type must be a valid integer")
    return user_input
  
  # Open an image file and return as an exif.Image instance
  def get_image(self, file_location, file_name):
    with open(f'{file_location}/{file_name}', "rb") as f:
      img = Image(f)
      if img.has_exif:
        print(f"{file_name} has EXIF data\n")
      else:
        print(f"{file_name} does not have EXIF data\n")
    return img
  
  # Replace a file's data, create it if it doesn't already exist and add data
  def replace_file(self, file_location, file_name, img):
    with open(f'{file_location}/{file_name}', 'wb') as f:
      f.write(img.get_file())
    print(f"Replaced '{file_name}' at '{file_location}/{file_name}'\n")
  
  # Replace a file's date and time taken based off a datetime.datetime object
  def replace_given_time(self, img, new_time):
    old_time = img.get("datetime_original")
    img.set("datetime_original", new_time)
    
    print(f"Changed time of '{file_name}'\nPrevious time: {old_time}\n New time: {new_time}\n")
    return img
  
  # Replace a file's date and time taken based off numerical inputs
  def replace_input_time(self, file_name, img):
    old_time = img.get("datetime_original")

    yr = self.get_int_input("Enter the year: ", 0, 3000, int)
    mth = self.get_int_input("Enter the month: ", 1, 12, int)
    dy = self.get_int_input("Enter the day: ", 1, 31, int)
    hr = self.get_int_input("Enter the hour: ", 0, 24, int)
    mins = self.get_int_input("Enter the minute: ", 0, 60, int)
    sec = self.get_int_input("Enter the second: ", 0, 60, int)
    new_time = datetime(year=yr, month=mth, day=dy, hour=hr, minute=mins, second=sec)
    img.set("datetime_original", new_time)

    print(f"Changed time of '{file_name}'\nPrevious time: {old_time}\n New time: {new_time}\n")
    return img

  # Open an image file and return the EXIF time data
  def get_image_time(self, file_name, img):
    time = img.get("datetime_original")
    print(f"{file_name}'s EXIF time: {time}\n")

  # Open an image file and return the EXIF data
  def get_image_data(self, file_name, img):
    print(f"{file_name}'s EXIF data: {sorted(img.list_all())}\n")
