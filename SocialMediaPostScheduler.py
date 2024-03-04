from datetime import datetime
from typing import List
import random
import json


# Define the Post data structure
class Post:
    def __init__(self, content: str, scheduled_date: datetime, platform: str, author: str):
        self.content = content
        self.scheduled_date = scheduled_date
        self.platform = platform
        self.author = author
        self.engagement_metrics = {
            "views": 0,
            "likes": 0,
            "comments": 0
        }


# Placeholder API functions for posting on each platform
def postToTwitter(content: str) -> bool:
    print("Posting to Twitter:", content)
    return True


def postToFacebook(content: str) -> bool:
    print("Posting to Facebook:", content)
    return True


def postToInstagram(content: str) -> bool:
    print("Posting to Instagram:", content)
    return True


# Functional modules
def addPost(post: Post, posts: List[Post]) -> List[Post]:
    return posts + [post]


def removePost(post: Post, posts: List[Post]) -> List[Post]:
    return [p for p in posts if p != post]


def listPosts(posts: List[Post]) -> None:
    if not posts:
        print("No posts scheduled.")
    else:
        print("\nScheduled Posts:")
        print("-" * 60)
        for i, post in enumerate(posts, start=1):
            print(f"  {i}. Platform: {post.platform} "
                  f"\nAuthor: {post.author} "
                  f"\nContent: {post.content} "
                  f"\nScheduled Date: {post.scheduled_date} "
                  f"\nEngagement Metrics: {post.engagement_metrics}")
            print("-" * 60)


# Function to schedule and post all pending posts
def scheduleAndPost(posts: List[Post]) -> None:
    for post in posts:
        if post.scheduled_date <= datetime.now():
            if post.platform == "Twitter":
                postToTwitter(post.content)
            elif post.platform == "Facebook":
                postToFacebook(post.content)
            elif post.platform == "Instagram":
                postToInstagram(post.content)

            # Simulate engagement metrics
            post.engagement_metrics["views"] = random.randint(100, 1000)
            post.engagement_metrics["likes"] = random.randint(10, 100)
            post.engagement_metrics["comments"] = random.randint(5, 50)
            print("Engagement metrics updated for the post.")

# Function to update a post
def updatePost(posts: List[Post], index: int) -> None:
    if 0 <= index < len(posts):
        post = posts[index]
        print("\nCurrent post details:")
        print(f"  Platform: {post.platform}, "
              f"Content: {post.content}, "
              f"Scheduled Date: {post.scheduled_date}")

        # Prompt user for updated information
        content = input("Enter updated content (press Enter to keep current content): ")
        platform = input("Enter updated platform (press Enter to keep current platform): ")
        scheduled_date_str = input(
            "Enter updated scheduled date and time (YYYY-MM-DD HH:MM), press Enter to keep current date: ")

        # Update post with new information
        if content:
            post.content = content
        if platform:
            post.platform = platform
        if scheduled_date_str:
            post.scheduled_date = datetime.strptime(scheduled_date_str, "%Y-%m-%d %H:%M")

        print("Post updated.")
    else:
        print("Invalid index.")


# Menu function
def menu() -> None:
    posts = []
    while True:
        # Display menu options

        print("\nSocial Media Post Scheduler")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        print("| 1. Add a post                              |")
        print("| 2. Remove a post                           |")
        print("| 3. Update a post                           |")
        print("| 4. List all posts                          |")
        print("| 5. Schedule and post pending posts         |")
        print("| 6. Exit                                    |")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a post
            content = input("Enter post content: ")
            platform = input("Enter platform (Twitter/Facebook/Instagram): ")
            scheduled_date = input("Enter scheduled date and time (YYYY-MM-DD HH:MM): ")
            scheduled_date = datetime.strptime(scheduled_date, "%Y-%m-%d %H:%M")
            author = input("Enter author's name: ")
            posts.append(Post(content, scheduled_date, platform, author))
            print("Post added.")

        elif choice == "2":
            # Remove a post
            listPosts(posts)
            index = int(input("Enter the number of the post to remove: ")) - 1
            if 0 <= index < len(posts):
                posts.pop(index)
                print("Post removed.")
            else:
                print("Invalid index.")

        elif choice == "3":
            # Update a post
            listPosts(posts)
            index = int(input("Enter the number of the post to update: ")) - 1
            updatePost(posts, index)

        elif choice == "4":
            # List all posts
            listPosts(posts)

        elif choice == "5":
            # Schedule and post pending posts
            scheduleAndPost(posts)

        elif choice == "6":
            # Exit
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



if __name__ == "__main__":
    menu()