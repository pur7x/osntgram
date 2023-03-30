import tkinter as tk
import instaloader

L = instaloader.Instaloader()

username = ""
profile = instaloader.Profile.from_username(L.context, username)

root = tk.Tk()
root.title("User Information")

# Create labels to display the user information
username_label = tk.Label(root, text="Username: " + profile.username)
userid_label = tk.Label(root, text="User ID: " + str(profile.userid))
followers_label = tk.Label(root, text="Followers: " + str(profile.followers))
followees_label = tk.Label(root, text="Followees: " + str(profile.followees))
posts_label = tk.Label(root, text="Number of posts: " + str(profile.mediacount))

# Get the user's email, if available
try:
    profile_data = profile.graphql_profile()
    email = profile_data['profile']['business_email'] or profile_data['profile']['email'] or "N/A"
except Exception as e:
    email = "N/A"

# Get the user's city and country
try:
    city = profile.city_name or "N/A"
    country = profile.country_name or "N/A"
except Exception as e:
    city = "N/A"
    country = "N/A"

# Get the user's stories
try:
    stories = [story.owner_username for story in profile.get_stories()]
    stories_label = tk.Label(root, text="Stories: " + str(stories))
except Exception as e:
    stories_label = tk.Label(root, text="Stories: N/A")

# Pack the labels into the window
username_label.pack()
userid_label.pack()
followers_label.pack()
followees_label.pack()
posts_label.pack()
tk.Label(root, text="Email: " + email).pack()
tk.Label(root, text="City: " + city).pack()
tk.Label(root, text="Country: " + country).pack()
stories_label.pack()

root.mainloop()
