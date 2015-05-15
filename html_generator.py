

NOTES = """Title: How the Web Works
Description: A user opens a browser on a device and searches for a website. The browser should then connect to the internet if not already connected. The internet then retrieves the website from a server using HTTP.

Title: Key Things to Know
Description:  HTML: Hypertext Markup Language (Main type of document on the web).
Types of files found on web: Plain text, HTML, images, video, music, and more.

HTML Elements
HTML Markup - Example: Bold and italicize text

HTML Attributes - Example: Creating Weblinks

Images - Example: Adding Images

Title: Whitespace
Description: There are inline and block elements. Block elements have an invisible box around the content inside of them. This will be discussed later on in the course.

Title: Computers are "stupid"
Description: Computers depend on performing instructions given to them by programmers. A small syntax error caused by a human will cause a major issue in a computer program.

Title: Ideas and Summaries
Description: - HTML is the building block for a webpage. It allows you to add images, text, and links to a webpage.

- CSS allows the programmer to change the style of the webpage. It allows you to change the "look" of the webpage by changing the colors, fonts, and styles.

- View a webpage as an organized set of blocks on a grid. Each block can have blocks within them. Blocks can consist of an image, header, menu,or other items.Each block can therefore be defined to have it's on width, font, or other assigned style class.

- Scratchpad.io, CodePen.io and Sublime each have their strengths and weaknesses for text editing. We will use scratchpad for the time being and utilize CodePen to share our webpages.

Title: Repetition
Description: Repetition is strongly discouraged for the following reasons:

Programming Errors: The more lines of code that is written, the more likely an error will be made by the programmer. Syntax errors are one of the main types of errors and this can be minimized by the use of CSS which will be discussed below.

Visual Consistency: When creating a webpage, you want it to look appealing and easy to follow. To do this, CSS allows class styles to be formed for boxes that have the same style throughout the webpage. This allows headers, body text, titles and so forth to have a consistent look and feel.

Webpage Bandwidth: Webpage bandwidth and size depends on the number of lines of HTML code among other things such as image size. To reduce the amount of lines of code, CSS allows the programmer to write a class style and refer to that repeatedly instead of writing repetitive lines of code.

Title: The Use of CSS
Description: CSS is an acronym for Cascading Style Sheets. It allows programmers to change the style and "feel" of related HTML elements. Similar HTML elements are given the same "class" name. Each class has it's own defined style where the programmar can select the font weight, font style, as well as other items.

Title: Programming Languages
Description: Programming languages differ from spoken languages. A spoken language, such as English, can be interpreted many diffferent ways. A programming language has to maintain consistency and be interpreted in only one specific way in order to avoid confusion and give direct instructions to the computer. A programming language also reduces the amount of verbiage required when creating code. An example of a programming language is Python.

Title: Python
Description: Python is a very widely used programming language. It will be taught in this nanodegree and serve as a foundation for future programming techniques. Python code is written by an individual and it is then compiled and executed to show the result.

Title: Python Expressions
Description: The format for Python arithmetic expressions is as follows:

addition: "Number" + "Number"

multiplication: "Number" * "Number"

subtraction: "Number" - "Number"

division: "Number" / "Number"

The format for Python variable expressions is as follows:

"Name" = "Expression"

Title: What is a Variable?
Description: A variable allows a programmer to store a value as a name, also known as assigning. The name can be used throughout a program, with some restriction, but it can also be modified using arithmetic operands.

Title: Assign a Value to a Variable
Description: To assign a value such as 10 to the variable called num_Value. The code would be as follows:

num_Value = 10

Difference in Equals Sign =
The equals sign can have a number of meanings as shown below:

Example 1: 5+5=10 This equals means "is the same as".

Example 2: num_Value = 10 This equals means "takes the value of".

Title: How are Variables Useful?
Description: Variables can be used in a number of different ways:

It allows us to store values by giving it a name that makes sense to whoever is creating and/or modifying the code.
It also allows us to change the value of the variable using arithmeic operands.
Example 2: num_Value = 10 This equals means "takes the value of".

What is the difference between 2 + 2 and "2" + "2"?
Variables can be used in a number of different ways:

2 + 2: The 2 is a number or in Python it is known as an integer. This code would add the two integers together and return 4.

"2" + "2": The "2" in quotations means that it is a string. This code will Concatenate the two strings together and return "22".

Title: What is a function (Dave calls them "procedures")?
Description: A function takes one or more inputs, mainuplates/processes those inputs, and outputs one or more things.

Title: What is the difference between making and using a function?
Description: To make a function you need to start you code with the word def followed by a function name and parameters. These parameters will be replaced by another value when the function is used. The body of the function includes the instructions for how to process the parameters and what to return.

Example: def function_Name(parameters)

To use the function, you write the name of the function and include your parameter(s) in the parentheses.

Example: def function_Name(Actual Parameters)

Title: How do functions help programmers avoid repetition?
Description: Functions call be called over and over again by the programmer throughtout the program. This reduces the amount of code a programmer needs to write and it minimizes the risk of making syntax errors while writing the program.

Title: What happens if a function doesn't have a return statement?
Description: If a function does not have a return statement, the function is essentially not producing an output that can be used outside of the function itself. If the function is called, the output would be None. """

def num_topics(text):
    lists = text.split()
    count = 0
    for word in lists:
        if word == "Title:":
            count += 1
    return count

def concept_chunk(text):
    start_location = text.find("Title:")
    end_location = text.find("Title", start_location + 1)
    concept = text[start_location:end_location]
    return concept

def get_title(concept):
    start_location = concept.find("Title:")
    end_location = concept.find("Description")
    title = concept[start_location:end_location - 1]
    return title

def get_desc(concept):
    start_location = concept.find("Description")
    desc = concept[start_location:]
    return desc

def index_title_desc(text):
    index = []
    concept = concept_chunk(text)
    index.append(get_title(concept))
    index.append(get_desc(concept))
    return index

def generate_html_portion(text):
    index = index_title_desc(text)
    html1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + index[0]
    html2 = '''
    </div>
    <div class="concept-description">
        ''' + index[1]
    html3 = '''
    </div>
</div>'''

    full_html = html1 + html2 + html3
    return full_html

def generate_html_full(text):
    count = 1
    topic_count = num_topics(text)
    html = ''
    while count <= topic_count:
        concept = generate_html_portion(text)
        count += 1
        html += concept
        text = text[text.find("Title:") + 1:]
    return html

print generate_html_full(NOTES)
