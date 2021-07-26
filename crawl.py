page = '<h1>Python Programming for Computer Science (Test Page)</h1><p>This page is for testing purposes, it is the demo page used on the <a href="https://www.udemy.com/course/draft/3542398/learn/?instructorPreviewMode=student_v4" target="_blank">Python Programming for Computer Science beginner course</a>. </p> <p>It includes many links that the web crawler that we are programming in the course should crawl. </p> <p>This is an exemple of links sending the visitor to "<a href="https://www.astateofdata.com/python-programming/computer-science-using-python-programming/">course description</a>" page. </p> <p>We do not need to worry about paragraphs, grammar, and writing style, what is important here is to find the links like this one linking to the <a href ="https://www.astateofdata.com/python-programming/python-projects-for-beginners-learn-with-examples/">Python Projects For Beginners</a> page.</p> <p>Although the content quality, writing style, and many other factors are important for SEO to get the page ranked higher in SERP, we are not going to focus on that as this is a Python Programming For Computer Science course, but not an SEO course.   </p>'
start_link = page.find ('<a href=') 
start_quote = page.find ('"', start_link) 
end_quote = page.find ('"', start_quote + 1) 
url = page[start_quote + 1 : end_quote]
print (url)

page = page[end_quote:]
start_link = page.find ('<a href=') 
start_quote = page.find ('"', start_link) 
end_quote = page.find ('"', start_quote + 1) 
url = page[start_quote + 1 : end_quote]
print (url)

page = page[end_quote:]
start_link = page.find ('<a href =') 
start_quote = page.find ('"', start_link) 
end_quote = page.find ('"', start_quote + 1) 
url = page[start_quote + 1 : end_quote]
print (url)
