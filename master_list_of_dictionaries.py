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
