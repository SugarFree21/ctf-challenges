<?php
$cookie_name = "user";
$cookie_value = "n00b";
$cookie_expiration = time() + 3600; // set the expiration time to 1 hour from now
$cookie_path = "/"; // set the cookie to be available in the entire domain

setcookie($cookie_name, $cookie_value, $cookie_expiration, $cookie_path);

if (isset($_COOKIE["user"]) && $_COOKIE["user"] == "admin") {
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Egyptian Tour Invitation</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          margin: 0;
          padding: 0;
          background-color: #f4f4f4;
          background-image: url(\'https://www.thetimes.co.uk/travel/wp-content/uploads/sites/6/2021/11/Cairo-Citadel-the-Mosque-Madrassa-of-Sultan-Hassan-Egypt_Credit_GettyImages-1296991101.jpg\');
          background-size: cover;
          background-position: center;
          background-attachment: fixed; /* Ensures the image covers the entire page */
        }
        header {
          background-color: #333;
          color: #fff;
          padding: 20px;
          text-align: center;
        }
        main {
          padding: 20px;
          color: #333;
          position: relative;
        }
        main::before {
          content: "";
          position: absolute;
          top: 0;
          bottom: 0;
          left: 0;
          right: 0;
          background-color: rgba(255, 255, 255, 0.7);
          z-index: -1;
        }
        h2, p {
          line-height: 1.6;
          position: relative;
          z-index: 1;
        }
        .cta-btn {
          display: inline-block;
          padding: 10px 20px;
          background-color: #ffcc00;
          color: #333;
          text-decoration: none;
          border-radius: 5px;
          margin-top: 20px;
        }
        .cta-btn:hover {
          background-color: #ffd633;
        }
      </style>
    </head>
    <body>
      <header>
        <h1>Admin</h1>
      </header>
      <main>
        <h2>Welcome to the Land of Pharaohs!</h2>
        <p>byuctf{Behold, I say unto you, obscurity never was security}</p>
      </main>
    </body>
    </html>
    ';
}
else {
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Egyptian Tour Invitation</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          margin: 0;
          padding: 0;
          background-color: #f4f4f4;
          background-image: url(\'https://www.thetimes.co.uk/travel/wp-content/uploads/sites/6/2021/11/Cairo-Citadel-the-Mosque-Madrassa-of-Sultan-Hassan-Egypt_Credit_GettyImages-1296991101.jpg\');
          background-size: cover;
          background-position: center;
          background-attachment: fixed; /* Ensures the image covers the entire page */
        }
        header {
          background-color: #333;
          color: #fff;
          padding: 20px;
          text-align: center;
        }
        main {
          padding: 20px;
          color: #333;
          position: relative;
        }
        main::before {
          content: "";
          position: absolute;
          top: 0;
          bottom: 0;
          left: 0;
          right: 0;
          background-color: rgba(255, 255, 255, 0.7);
          z-index: -1;
        }
        h2, p {
          line-height: 1.6;
          position: relative;
          z-index: 1;
        }
        .cta-btn {
          display: inline-block;
          padding: 10px 20px;
          background-color: #ffcc00;
          color: #333;
          text-decoration: none;
          border-radius: 5px;
          margin-top: 20px;
        }
        .cta-btn:hover {
          background-color: #ffd633;
        }
      </style>
    </head>
    <body>
      <header>
        <h1>Explore Egypt - A Journey through Time</h1>
      </header>
      <main>
        <h2>Welcome to the Land of Pharaohs!</h2>
        <p>Embark on an unforgettable adventure to Egypt, where ancient wonders and modern marvels collide. From the majestic pyramids of Giza to the serene Nile River cruises, immerse yourself in the rich history and culture of this mesmerizing land.</p>
        <p>Tour guides, please let us know when you find the site so we can give you access to the admin page</p>
        <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" class="cta-btn">Learn More</a>
      </main>
    </body>
    </html>
    ';
}
?>
