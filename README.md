**Application based on Django Framework**

In this application you can create publications (news or articles), edit and delete them. You can select categories at the moment of their creation (Sports, Travel, Movies/Music, Auto, Economy)

Publications can be displayed in a general list (pagination is used, no more than 10 publications are displayed per page), you can view a specific publication.  Filtering of publications by category, title, date of creation (later) and author's name using Django filters is implemented. You can select several criteria for filtering at once.

Additionally, a censor filter has been implemented that replaces characters in unwanted words with '*' (in publication titles and the text itself).

The start page offers registration with email address confirmation or authorization (using Django-allauth, or through a Google account using OAuth).

An authorized user can subscribe to categories of interest.

After registration you are offered to become an author to be able to create publications (later edit and delete them).  Unauthorized users can only view publications.

Through django shell or admin panel you can leave comments on news or articles. It is also possible to "like" a particular publication and a comment to a publication. On the basis of "likes" the authors' rating is implemented.

Subscribers are sent email notifications about new publications in their favourite categories. Also once a week a newsletter about new publications in favourite categories for the week is sent (Redis/Celery is used).

Logging is implemented in the project. Messages of DEBUG level and higher, WARNING and higher, ERROR and CRITICAL are output to the console. Messages of INFO level and higher are written to the file general.log. The errors.log file contains messages of the ERROR and CRITICAL levels. The security.log file contains security-related messages.

Visualisation is implemented on the basis of bootstrap-template. All other templates are inherited from the base template.
