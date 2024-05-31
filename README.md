# Django-Web-Application-for-Uploading-Processing-and-Emailing-CSV-Data

Title: Django Web Page for Uploading Excel/CSV Files and Generating Summary Report 
Objective: Develop a Django-based web page that allows users to upload Excel/CSV files. 
Process the uploaded data to generate a summary report and email it to specified recipients. 
Components: 
1. Django Project Setup: 
o Created a new Django project. 
o Added a new app to handle file upload and processing. 
2. Model Definition: 
o Defined a Django model Uploaded Data to store the uploaded data. 
o Fields: state, dpd, count. 
3. Form Creation: 
o Developed a form using Django's forms,Form class. 
o Included a File Field to allow users to upload files. 
4. View Function: 
o Implemented a view function to handle file upload. 
o Utilized panda’s library to process the uploaded file. 
o Generated a summary report based on the uploaded data. 
o Saved the summary data to the database using the defined model. 
o Utilized Django's email functionality to send the summary report as the body 
text to specify email addresses. 
5. HTML Templates: 
o Created HTML templates for the upload form and success message. 
o Used Django's templating language to render form fields and messages. 
6. Error Handling: 
o Implemented basic error handling to handle invalid file uploads or processing 
errors. 
o Displayed appropriate error messages to users. 
Usage: 
1. Run the Django development server. 
2. Access the web page in a browser. 
3. Upload an Excel/CSV file using the provided form. 
4. Upon successful upload, a success message is displayed, and the summary report is 
emailed to the specified recipients. 
Further Improvements: 
 Implement client-side and server-side validation for file uploads. 
 Enhance error handling to provide more detailed feedback to users. 
 Add user authentication and permissions for accessing the upload feature. 
 Improve the design and layout of HTML templates for better user experience. 
Conclusion: The Django-based web page provides a simple and efficient way for users to 
upload Excel/CSV files and generate summary reports. By leveraging Django's built-in 
features and libraries like pandas, the application ensures robustness and scalability for 
handling large datasets. ![upload page](https://github.com/nikhilbari63/Django-Web-Application-for-Uploading-Processing-and-Emailing-CSV-Data/assets/160225662/4e8f4782-1aa6-4c80-b073-cb395af20e3c)
![result page](https://github.com/nikhilbari63/Django-Web-Application-for-Uploading-Processing-and-Emailing-CSV-Data/assets/160225662/4adf93ba-e6a8-4d13-8b71-5658257b9b6c)

