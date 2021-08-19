# Dataset Management Platform
A simple dataset management platform, with authentication system. Accounts are provided below.


# Technical Details
- User can upload a dataset, note that only `.zip` files are allowed.
- This uploaded dataset can be booked by any user
- User can book an uploaded dataset, note that one task can only booked by one user.
- User can revoke their own booking.
- A booked dataset can be downloaded, but only by a user who booked it.
- Any user can delete any uploaded dataset.
- Sample `.zip` files are provided in the `sample_zip` folder.


# How To Install and Run

1. Install [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/), depending on your Operating System.
2. Go inside `datasetmanagement` folder, where `docker-compose.yml` and `Dockerfile` are located.
  ```
  $ cd datasetmanagement
  ```
3. Build the application.
  ```
  $ docker-compose build
  ```
4. Run the application.
  ```
  $ docker-compose up
  ```
5. Open `localhost:8000` on your web browser.

# Accounts

| Email    | Password |
| ----------- | ----------- |
| anthony@anthony.com      | anthony       |
| ben@ben.com   | ben       |
| clara@clara.com   | clara      |
| dummy@dummy.com   | dummy       |

# Heroku Link