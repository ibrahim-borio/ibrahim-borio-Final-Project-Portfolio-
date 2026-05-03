# E1 
class Task:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__is_done = False

    def mark_as_done(self):
        self.__is_done = True

    def display(self):
        status = "DONE" if self.__is_done else "NOT DONE"
        print(f"Task: {self.__name} ({status})")
        print(f"Description: {self.__description}\n")


# Test Implementation
t1 = Task("Buy groceries", "Milk, eggs, bread")
t2 = Task("Finish report", "Quarterly report")
t3 = Task("Call friend", "Schedule weekend visit")

t2.mark_as_done()

for task in [t1, t2, t3]:
    task.display()
    
let photos = ["Photo1", "Photo2", "Photo3"];
let stack = [];

// المستخدم يتصفح الصور
photos.forEach(photo => stack.push(photo));

// Back functionality
while (stack.length > 0) {
    let current = stack.pop();
    console.log("Back to:", current);
}

#-- Create Tables
CREATE TABLE tasks (
    task_id INT PRIMARY KEY,
    task_name VARCHAR(100),
    created_date DATE,
    is_completed BOOLEAN
);

CREATE TABLE task_details (
    detail_id INT PRIMARY KEY,
    task_id INT,
    description TEXT,
    due_date DATE,
    priority VARCHAR(10) CHECK (priority IN ('Low','Medium','High')),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id) ON DELETE CASCADE
);

-- Insert Data
INSERT INTO tasks VALUES (1,'Complete project report','2023-11-15',FALSE);
INSERT INTO tasks VALUES (2,'Buy groceries','2023-11-10',FALSE);
INSERT INTO tasks VALUES (3,'Call friend','2023-11-12',FALSE);

INSERT INTO task_details VALUES (1,1,'Write conclusion section','2023-11-20','High');
INSERT INTO task_details VALUES (2,2,'Get milk and eggs','2023-11-11','Medium');
INSERT INTO task_details VALUES (3,3,'Schedule weekend visit','2023-11-13','Low');

-- Read Queries
SELECT * FROM tasks JOIN task_details USING(task_id);
SELECT * FROM tasks WHERE is_completed = FALSE;
SELECT * FROM task_details WHERE priority = 'High';
SELECT * FROM task_details WHERE due_date BETWEEN '2023-11-10' AND '2023-11-20';

-- Update
UPDATE tasks SET task_name = 'Finish report', is_completed = TRUE WHERE task_id = 1;

-- Delete
DELETE FROM task_details WHERE detail_id = 2;
DELETE FROM tasks WHERE task_id = 3;
#_________________________________________________

#E2

class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__available = True   # يبدأ متاح

    def check_out(self):
        self.__available = False

    def return_book(self):
        self.__available = True

    def display(self):
        status = "Yes" if self.__available else "No"
        print(f"Title: {self.__title}, Author: {self.__author}, Available: {status}")

    def is_available(self):
        return self.__available

    def get_title(self):
        return self.__title


class Member:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id

    def borrow(self, book):
        if book.is_available():
            book.check_out()
            print(f"Success: {self.__name} borrowed {book.get_title()}")
        else:
            print(f"Failed: {book.get_title()} is not available")


# Test Implementation
b1 = Book("Python Basics", "John Smith")
b2 = Book("Data Structures", "Alice Brown")
m1 = Member("Ibrahim", "M001")

m1.borrow(b1)
b1.display()
b2.display()

let orders = ["Pizza", "Burger", "Salad", "Drinks"];

// إضافة طلب جديد
orders.push("Ice Cream");

// حذف Burger
orders = orders.filter(order => order !== "Burger");

// طباعة القائمة
console.log("Order List:");
orders.forEach(order => console.log("-", order));


-- Create Tables
CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(50)
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author_id INT,
    available BOOLEAN,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE CASCADE
);

-- Insert Data
INSERT INTO Authors VALUES (1,'John Smith','USA');
INSERT INTO Authors VALUES (2,'Alice Brown','UK');

INSERT INTO Books VALUES (1,'Python Basics',1,TRUE);
INSERT INTO Books VALUES (2,'Data Structures',1,TRUE);
INSERT INTO Books VALUES (3,'Graphic Design Intro',2,FALSE);

-- Queries
SELECT * FROM Books WHERE available = TRUE;
SELECT * FROM Books WHERE author_id = 1;

-- Update
UPDATE Books SET available = FALSE WHERE book_id = 1;

-- Delete
DELETE FROM Authors WHERE author_id = 2;
-- (هيتم حذف كتب Alice Brown تلقائيًا بسبب CASCADE)
#___________________________________________________________________

# E3
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        print(f"Hello, I'm {self.__name} and I'm {self.__age} years old.")


class Student(Person):
    def __init__(self, name, age, grade, student_id):
        super().__init__(name, age)
        self.__grade = grade
        self.__student_id = student_id
        self.__subjects = []

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def introduce(self):
        print(f"Hello, I'm a student. Grade: {self.__grade}, ID: {self.__student_id}, Subjects: {self.__subjects}")


class Teacher(Person):
    def __init__(self, name, age, subject, teacher_id):
        super().__init__(name, age)
        self.__subject = subject
        self.__teacher_id = teacher_id

    def teach(self):
        print(f"Teaching {self.__subject}")

    def introduce(self):
        print(f"Hello, I'm a teacher. Subject: {self.__subject}, ID: {self.__teacher_id}")


# Test Implementation
p1 = Person("Ali", 30)
p1.introduce()

s1 = Student("Sara", 16, "10th Grade", "S001")
s1.add_subject("Math")
s1.add_subject("Science")
s1.introduce()

t1 = Teacher("Omar", 40, "Physics", "T001")
t1.introduce()
t1.teach()


let queue = ["Customer 1", "Customer 2", "Customer 3"];

// خدمة العملاء بالترتيب
while (queue.length > 0) {
    let customer = queue.shift(); // يطلع أول واحد في الطابور
    console.log("Served:", customer);
}

-- Create Tables
CREATE TABLE menu_items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(5,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    table_number INT,
    order_date DATE,
    status VARCHAR(20) CHECK (status IN ('Pending','Preparing','Served'))
);

CREATE TABLE order_details (
    detail_id INT PRIMARY KEY,
    order_id INT,
    item_id INT,
    quantity INT,
    special_requests TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id) ON DELETE CASCADE
);

-- Insert Data
INSERT INTO menu_items VALUES (1,'Margherita Pizza','Main',12.99);
INSERT INTO menu_items VALUES (2,'Pasta','Main',10.50);
INSERT INTO menu_items VALUES (3,'Salad','Starter',6.00);
INSERT INTO menu_items VALUES (4,'Soup','Starter',5.50);
INSERT INTO menu_items VALUES (5,'Ice Cream','Dessert',4.00);

INSERT INTO orders VALUES (1,5,'2023-11-15','Pending');
INSERT INTO orders VALUES (2,3,'2023-11-15','Preparing');
INSERT INTO orders VALUES (3,2,'2023-11-16','Served');

INSERT INTO order_details VALUES (1,1,1,2,'Extra cheese');
INSERT INTO order_details VALUES (2,1,3,1,'No onions');
INSERT INTO order_details VALUES (3,2,2,1,'Gluten free');
INSERT INTO order_details VALUES (4,3,5,2,'Chocolate flavor');

-- Read Queries
SELECT * FROM orders JOIN order_details USING(order_id) JOIN menu_items USING(item_id);
SELECT * FROM orders WHERE status='Pending';
SELECT * FROM menu_items WHERE category='Dessert';

-- Update
UPDATE menu_items SET price=13.99 WHERE item_id=1;
UPDATE orders SET status='Served' WHERE order_id=1;

-- Delete
DELETE FROM menu_items WHERE item_id=4;
DELETE FROM order_details WHERE detail_id=2;
#__________________________________________________________
# E4 
class Product:
    def __init__(self, name, description, price, stock):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__stock = stock

    def restock(self, amount):
        self.__stock += amount

    def sell(self, amount):
        if amount <= self.__stock:
            self.__stock -= amount
        else:
            print("Not enough stock!")

    def display(self):
        print(f"Product: {self.__name} (${self.__price})")
        print(f"Description: {self.__description}")
        print(f"Stock: {self.__stock}\n")


# Test Implementation
p1 = Product("Laptop", "15-inch laptop with 16GB RAM", 999.99, 10)
p2 = Product("Smartphone", "Latest model with 128GB storage", 699.99, 15)
p3 = Product("Headphones", "Noise-cancelling wireless headphones", 149.99, 25)

p1.restock(5)   # زيادة المخزون
p2.sell(3)      # بيع 3 وحدات

for product in [p1, p2, p3]:
    product.display()

let graph = {
    "Station A": ["Station B", "Station C"],
    "Station B": ["Station A", "Station D"],
    "Station C": ["Station A", "Station D"],
    "Station D": ["Station B", "Station C"]
};

for (let station in graph) {
    console.log(`${station} is connected to ${graph[station]}`);
}


-- Create Tables
CREATE TABLE Jobs (
    job_id INT PRIMARY KEY,
    title VARCHAR(100),
    department VARCHAR(50),
    salary_range VARCHAR(50)
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    hire_date DATE,
    job_id INT,
    FOREIGN KEY (job_id) REFERENCES Jobs(job_id) ON DELETE CASCADE
);

-- Insert Data
INSERT INTO Jobs VALUES (1,'Software Engineer','IT','3000-5000');
INSERT INTO Jobs VALUES (2,'HR Manager','HR','4000-6000');
INSERT INTO Jobs VALUES (3,'Sales Executive','Sales','2500-4000');

INSERT INTO Employees VALUES (1,'Ali','ali@email.com','2023-01-10',1);
INSERT INTO Employees VALUES (2,'Sara','sara@email.com','2023-02-15',1);
INSERT INTO Employees VALUES (3,'Omar','omar@email.com','2023-03-20',2);
INSERT INTO Employees VALUES (4,'Mona','mona@email.com','2023-04-05',3);
INSERT INTO Employees VALUES (5,'Ibrahim','ibrahim@email.com','2023-05-01',3);

-- Queries
SELECT Employees.name, Jobs.title FROM Employees JOIN Jobs USING(job_id);
SELECT * FROM Employees JOIN Jobs USING(job_id) WHERE department='IT';

-- Update
UPDATE Employees SET job_id=2 WHERE emp_id=1;

-- Delete
DELETE FROM Jobs WHERE job_id=3;
-- (هيتم حذف الموظفين اللي عندهم Sales Executive بسبب CASCADE)
