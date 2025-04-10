"""
What to do:
1. Learn about csv.reader()
  Refer to https://docs.python.org/3/library/csv.html
2. Learn about open() at: https://www.w3schools.com/python/python_file_handling.asp
3. THe csv file is too long.  Take 10 rows and delete the rest of rows.  
  Save the file as proj1008-short.csv.  Modify open().
4. Insert print(csv_file), print(video_game_reader), and print(row) 
  in def load_video_game_data().  Run the code.  What happens?
5. Insert print("name, platform, and year_of_release are", name, platform, year_of_release)
  in def view_video_game_data().  Run the code.  What happens?
6. Insert print("game_name=", game_name, "  name=", name)
  in def search_video_game_data().  Run the code.  What happens?
7. Learn about the coding of 
    while True:   
        if ...:
        elif ...:
            break
  Refer to https://www.w3schools.com/python/python_while_loops.asp for while and break.
  
  """

from csv import reader


def load_video_game_data():
    video_game_data = []
    with open("proj1008-short.csv", mode="rt", newline="") as csv_file:
        print("csv_file is", csv_file)
        video_game_reader = reader(csv_file)
        print("video_game_reader is", video_game_reader)
        for row in video_game_reader:
            print(row)
            video_game_data.append(row)

    return video_game_data


def view_video_game_data(video_game_data):
    for data in video_game_data:
        name, platform, year_of_release = data
        print("name, platform, and year_of_release are", name, platform, year_of_release)
        print(f"In {year_of_release} {name} was released on {platform}")


def search_video_game_data(video_game_data, game_name):
    for data in video_game_data:
        name, platform, year_of_release = data
        if game_name in name:
            print("game_name=", game_name, "  name=", name)
            print(f"In {year_of_release} {name} was released on {platform}")


welcome_message = """
    Welcome to the 'Video Game Browser' app!

    In this app, you can view video game data including the
    year of release, the title, and the platform the game was
    released on. You can also search the data for titles that
    match a keyword of your choosing.
"""

options = """
    1.) View Video Game Data 2.) Search Video Game Data
    3.) Exit
"""

VIEW = 1
SEARCH = 2
EXIT = 3

video_game_data = load_video_game_data()
print("video_game_data is:", video_game_data)

print(welcome_message)

while True:
    user_choice = int(input(options))

    if user_choice == VIEW:
        view_video_game_data(video_game_data)
    elif user_choice == SEARCH:
        game_name = input("Enter your search term: ")
        search_video_game_data(video_game_data, game_name)
    elif user_choice == EXIT:
        break
