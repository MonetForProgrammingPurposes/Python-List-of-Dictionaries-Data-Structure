Introduction

In this activity, create different lists of dictionaries in Python. Each dictionary stores information about certain things like products, employees, books, universities, and restaurants. After creating these lists, I needed to display the details by printing them in the console. This documentation will explain the step-by-step process and my learnings.

1: Setting Up Python Environment

First, I made sure I had a Python environment ready. I used VSCode as my code editor. You can also use Replit or any other online IDE if you prefer. Then, I created a new Python file and named it master_list_of_dictionaries.py.

2: Creating Lists of Dictionaries

In Python, a dictionary is like a container that holds information in a key-value format. For example, in a product dictionary, we might have a key called product_name and its value could be "Laptop". I created five lists, each containing dictionaries for the different categories: Products, Employees, Books, Universities, and Restaurants.

Here’s the code where I created each list with 5 dictionaries:

# List of product dictionaries
products = [
    {"product_name": "Laptop", "price": 50000},
    {"product_name": "Smartphone", "price": 30000},
    {"product_name": "Tablet", "price": 20000},
    {"product_name": "Headphones", "price": 5000},
    {"product_name": "Monitor", "price": 10000}
]

# List of employee dictionaries
employees = [
    {"name": "Alice", "job_title": "Software Engineer"},
    {"name": "Bob", "job_title": "Data Analyst"},
    {"name": "Charlie", "job_title": "Product Manager"},
    {"name": "Diana", "job_title": "UX Designer"},
    {"name": "Eve", "job_title": "HR Specialist"}
]

# List of books dictionaries
books = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Moby Dick", "author": "Herman Melville"}
]

# List of university dictionaries
universities = [
    {"name": "Harvard University", "location": "Cambridge, MA"},
    {"name": "Stanford University", "location": "Stanford, CA"},
    {"name": "MIT", "location": "Cambridge, MA"},
    {"name": "UC Berkeley", "location": "Berkeley, CA"},
    {"name": "Oxford University", "location": "Oxford, UK"}
]

# List of restaurant dictionaries
restaurants = [
    {"name": "The French Laundry", "cuisine_type": "French"},
    {"name": "Gordon Ramsay's", "cuisine_type": "British"},
    {"name": "Nobu", "cuisine_type": "Japanese"},
    {"name": "Joe's Pizza", "cuisine_type": "Italian"},
    {"name": "Taco Bell", "cuisine_type": "Mexican"}
]


3: Printing the Details

After creating the lists, I needed to print the information stored in each dictionary. To do that, I created a function called print_details. It prints the details for any given list of dictionaries. Here’s how I did it:

# Function to print details
def print_details(data, label):
    print(f"\n--- {label} Details ---")
    for item in data:
        print(item)

# Print all details
print_details(products, "Product")
print_details(employees, "Employee")
print_details(books, "Books")
print_details(universities, "University")
print_details(restaurants, "Restaurant")


This function accepts two things:

data: the list of dictionaries (e.g., products, employees).

label: the category name (e.g., "Product", "Employee") to organize the printed output.

4: Running the Program

Go to your project directory using cd , then use python “name of your python app (.py)“

When ran the program, it printed all the details from the dictionaries. Below is an example of the output:

--- Product Details ---
{'product_name': 'Laptop', 'price': 50000}
{'product_name': 'Smartphone', 'price': 30000}
{'product_name': 'Tablet', 'price': 20000}
{'product_name': 'Headphones', 'price': 5000}
{'product_name': 'Monitor', 'price': 10000}

--- Employee Details ---
{'name': 'Alice', 'job_title': 'Software Engineer'}
{'name': 'Bob', 'job_title': 'Data Analyst'}
{'name': 'Charlie', 'job_title': 'Product Manager'}
{'name': 'Diana', 'job_title': 'UX Designer'}
{'name': 'Eve', 'job_title': 'HR Specialist'}

--- Books Details ---
{'title': '1984', 'author': 'George Orwell'}
{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
{'title': 'Pride and Prejudice', 'author': 'Jane Austen'}
{'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
{'title': 'Moby Dick', 'author': 'Herman Melville'}

--- University Details ---
{'name': 'Harvard University', 'location': 'Cambridge, MA'}
{'name': 'Stanford University', 'location': 'Stanford, CA'}
{'name': 'MIT', 'location': 'Cambridge, MA'}
{'name': 'UC Berkeley', 'location': 'Berkeley, CA'}
{'name': 'Oxford University', 'location': 'Oxford, UK'}

--- Restaurant Details ---
{'name': 'The French Laundry', 'cuisine_type': 'French'}
{'name': 'Gordon Ramsay's', 'cuisine_type': 'British'}
{'name': 'Nobu', 'cuisine_type': 'Japanese'}
{'name': 'Joe's Pizza', 'cuisine_type': 'Italian'}
{'name': 'Taco Bell', 'cuisine_type': 'Mexican'}


5: GitHub Commits

Initialized Git Repository: I reinitialized the existing Git repository.

Staged Changes: I added all the changes to be committed.

Committed Changes:

Message: "Initial commit."

I changed 3 files, adding and deleting some lines.

Remote Repository: I tried to add a remote origin that already existed.

Pushed Changes: I pushed my changes to the remote repository and set the master branch to track origin/master.

6: Learnings and Conclusion

Through this activity, I learned how to store data using dictionaries in Python. It’s also interesting to see how we can manage different kinds of information (products, employees, books, etc.) all in one program. Printing the data using loops helped me understand how to access each dictionary item easily.

I also realized the importance of organizing data and using proper function structures like print_details. It makes the code easier to manage and reuse for different lists.

